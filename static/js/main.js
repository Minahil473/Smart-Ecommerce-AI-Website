/* ══════════════════════════════════════════
   NAVBAR
══════════════════════════════════════════ */
const nav = document.querySelector('.nav');
if (nav) {
  window.addEventListener('scroll', () =>
    nav.classList.toggle('scrolled', window.scrollY > 10)
  );
}

function toggleNav() {
  const menu = document.getElementById('mobile-menu');
  const ham  = document.getElementById('hamburger');
  if (!menu) return;

  const opening = !menu.classList.contains('open');
  menu.classList.toggle('open', opening);
  ham.classList.toggle('open', opening);
}
window.toggleNav = toggleNav;

// Close when a mobile link is clicked
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.mobile-link').forEach(function(link) {
    link.addEventListener('click', function() {
      document.getElementById('mobile-menu').classList.remove('open');
      document.getElementById('hamburger').classList.remove('open');
    });
  });

  // Close when clicking outside the nav
  document.addEventListener('click', function(e) {
    const menu  = document.getElementById('mobile-menu');
    const navEl = document.getElementById('main-nav');
    if (menu && menu.classList.contains('open') && !navEl.contains(e.target)) {
      menu.classList.remove('open');
      document.getElementById('hamburger').classList.remove('open');
    }
  });
});

/* ══════════════════════════════════════════
   MOBILE FILTER TOGGLE
══════════════════════════════════════════ */
window.toggleFilters = function() {
  const sidebar = document.querySelector('.sidebar');
  const btn     = document.querySelector('.filter-toggle');
  if (!sidebar) return;
  const open = sidebar.classList.toggle('filters-open');
  if (btn) btn.innerHTML = open
    ? 'Filters ▲'
    : 'Filters ▼';
};

/* ══════════════════════════════════════════
   SHOP PAGE
══════════════════════════════════════════ */
if (document.getElementById('product-grid')) {

  let allProducts    = [];
  let categories     = [];
  let activeSearch   = '';
  let activeCategory = new URLSearchParams(location.search).get('category') || '';
  let activeMaxPrice = '';

  async function fetchCategories() {
    const res  = await fetch('/api/categories');
    categories = await res.json();
    renderSidebar();
  }

  async function fetchProducts() {
    showSkeletons();
    const params = new URLSearchParams();
    if (activeSearch)   params.set('search',    activeSearch);
    if (activeCategory) params.set('category',  activeCategory);
    if (activeMaxPrice) params.set('max_price', activeMaxPrice);

    try {
      const res   = await fetch('/api/products?' + params);
      allProducts = await res.json();
      renderGrid(allProducts);
    } catch {
      document.getElementById('product-grid').innerHTML =
        '<div class="error-box"><strong>Could not load products.</strong> Make sure Flask is running on port 5000.</div>';
    }
  }

  function renderSidebar() {
    const el = document.getElementById('cat-filters');
    if (!el) return;
    el.innerHTML = `
      <button class="filter-btn ${!activeCategory ? 'active' : ''}" onclick="setCategory('')">All</button>
      ${categories.map(c => `
        <button class="filter-btn ${activeCategory === c ? 'active' : ''}"
          onclick="setCategory('${c}')">${c}</button>
      `).join('')}
    `;
  }

  function setCategory(cat) {
    activeCategory = cat;
    renderSidebar();
    fetchProducts();
  }
  window.setCategory = setCategory;

  function setMaxPrice(p) {
    activeMaxPrice = p;
    document.querySelectorAll('.price-btn').forEach(b =>
      b.classList.toggle('active', b.dataset.p === p)
    );
    fetchProducts();
  }
  window.setMaxPrice = setMaxPrice;

  function renderGrid(products) {
    const grid = document.getElementById('product-grid');
    const bar  = document.getElementById('results-count');
    if (bar) bar.textContent = `${products.length} product${products.length !== 1 ? 's' : ''}`;

    const clearBtn = document.getElementById('clear-btn');
    if (clearBtn) clearBtn.style.display = (activeSearch || activeCategory || activeMaxPrice) ? '' : 'none';

    if (!products.length) {
      grid.innerHTML = '<div class="empty"><p>No products found. Try different filters.</p></div>';
      return;
    }

    grid.innerHTML = products.map((p, i) => `
      <a href="/product/${p.id}" class="card" style="animation-delay:${i * 40}ms">
        <div class="card-img-wrap">
          <img class="card-img"
            src="${p.image_url || 'https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=500'}"
            alt="${p.name}"
            onerror="this.src='https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=500'" loading="lazy"/>
          <span class="card-cat">${p.category}</span>
          ${!p.in_stock ? '<span class="card-oos">Out of stock</span>' : ''}
        </div>
        <div class="card-body">
          <h3 class="card-name">${p.name}</h3>
          <p class="card-desc">${p.description.slice(0, 88)}…</p>
          <div class="card-footer">
            <span class="card-price">$${p.price.toFixed(2)}</span>
            <span class="card-cta">View →</span>
          </div>
        </div>
      </a>
    `).join('');
  }

  function showSkeletons() {
    document.getElementById('product-grid').innerHTML =
      Array.from({length: 8}).map(() => '<div class="skeleton"></div>').join('');
  }

  const searchForm  = document.getElementById('search-form');
  const searchInput = document.getElementById('search-input');
  if (searchForm) {
    searchForm.addEventListener('submit', e => {
      e.preventDefault();
      activeSearch = searchInput.value.trim();
      fetchProducts();
    });
  }

  window.clearFilters = function() {
    activeSearch = ''; activeCategory = ''; activeMaxPrice = '';
    if (searchInput) searchInput.value = '';
    renderSidebar();
    document.querySelectorAll('.price-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('.price-btn[data-p=""]')?.classList.add('active');
    fetchProducts();
  };

  fetchCategories();
  fetchProducts();
}

/* ══════════════════════════════════════════
   CHAT BUBBLE
══════════════════════════════════════════ */
(function initChat() {
  const fab      = document.getElementById('chat-fab');
  const panel    = document.getElementById('chat-panel');
  const closeBtn = document.getElementById('chat-close');
  const msgs     = document.getElementById('chat-msgs');
  const input    = document.getElementById('chat-input');
  const sendBtn  = document.getElementById('chat-send');
  const suggBox  = document.getElementById('chat-sugg');
  if (!fab) return;

  let isOpen    = false;
  let isLoading = false;

  function toggle() {
    isOpen = !isOpen;
    panel.classList.toggle('open', isOpen);
    fab.innerHTML = isOpen
      ? `<svg width="18" height="18" viewBox="0 0 20 20" fill="none">
           <path d="M5 5l10 10M15 5L5 15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
         </svg>`
      : `<svg width="21" height="21" viewBox="0 0 24 24" fill="none">
           <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"
             stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
           <circle cx="9" cy="10" r="1" fill="currentColor"/>
           <circle cx="12" cy="10" r="1" fill="currentColor"/>
           <circle cx="15" cy="10" r="1" fill="currentColor"/>
         </svg>
         <span class="fab-badge">AI</span>`;
    if (isOpen) setTimeout(() => input?.focus(), 150);
  }

  fab.addEventListener('click', toggle);
  closeBtn?.addEventListener('click', toggle);

  function scrollBottom() { msgs.scrollTop = msgs.scrollHeight; }

  function addMsg(role, text, isError = false) {
    const div = document.createElement('div');
    div.className = `msg ${role}`;
    div.innerHTML = role === 'assistant'
      ? `<div class="msg-avatar">R</div><div class="bubble${isError ? ' error' : ''}">${text}</div>`
      : `<div class="bubble">${text}</div>`;
    msgs.appendChild(div);
    scrollBottom();
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'msg assistant'; div.id = 'typing-indicator';
    div.innerHTML = '<div class="msg-avatar">R</div><div class="bubble typing"><span></span><span></span><span></span></div>';
    msgs.appendChild(div);
    scrollBottom();
  }
  function hideTyping() { document.getElementById('typing-indicator')?.remove(); }

  async function send(text) {
    const q = (text || input.value).trim();
    if (!q || isLoading) return;
    addMsg('user', q);
    input.value = '';
    isLoading = true;
    sendBtn.disabled = true;
    if (suggBox) suggBox.style.display = 'none';
    showTyping();

    try {
      const res  = await fetch('/api/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question: q}),
      });
      const data = await res.json();
      hideTyping();
      if (data.error) {
        addMsg('assistant', `⚠️ ${data.error}`, true);
        return;
      }
      addMsg('assistant', data.answer.replace(/\n/g, '<br>'));
    } catch (err) {
      hideTyping();
      addMsg('assistant', '⚠️ Could not reach the server. Make sure Flask is running on port 5000.', true);
    } finally {
      isLoading = false;
      sendBtn.disabled = false;
      input.focus();
    }
  }

  sendBtn?.addEventListener('click', () => send());
  input?.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); }
  });

  document.querySelectorAll('.sugg-btn').forEach(btn =>
    btn.addEventListener('click', () => send(btn.dataset.q))
  );

  window.addEventListener('open-chat', e => {
    if (!isOpen) toggle();
    if (e.detail?.question) { input.value = e.detail.question; input.focus(); }
  });
})();