/* ── Edit Modal ── */
function openEdit(id, name, price, category, description, tags, imageUrl, inStock) {
  document.getElementById('edit-form').action = `/admin/edit/${id}`;
  document.getElementById('edit-name').value        = name;
  document.getElementById('edit-price').value       = price;
  document.getElementById('edit-category').value    = category;
  document.getElementById('edit-description').value = description;
  document.getElementById('edit-tags').value        = tags;
  document.getElementById('edit-image-url').value   = imageUrl;
  document.getElementById('edit-stock').checked     = inStock;

  document.getElementById('modal-overlay').classList.add('open');
  document.getElementById('edit-modal').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeEdit() {
  document.getElementById('modal-overlay').classList.remove('open');
  document.getElementById('edit-modal').classList.remove('open');
  document.body.style.overflow = '';
}

// Close modal on Escape key
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeEdit();
});

/* ── Table search ── */
function filterTable(query) {
  const q    = query.toLowerCase();
  const rows = document.querySelectorAll('#product-table tbody tr');
  rows.forEach(row => {
    const text = row.dataset.search || '';
    row.style.display = text.includes(q) ? '' : 'none';
  });
}

/* ── New category toggle ── */
function toggleNewCat(select) {
  const group = document.getElementById('new-cat-group');
  if (select.value === '__new__') {
    group.style.display = '';
    group.querySelector('input').required = true;
  } else {
    group.style.display = 'none';
    group.querySelector('input').required = false;
    group.querySelector('input').value = '';
  }
}

/* ── Auto-hide flash messages after 4s ── */
document.querySelectorAll('.flash').forEach(el => {
  setTimeout(() => {
    el.style.transition = 'opacity .5s';
    el.style.opacity = '0';
    setTimeout(() => el.remove(), 500);
  }, 4000);
});
