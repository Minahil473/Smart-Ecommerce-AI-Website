# 🛍️ Maison — RAG-Powered E-Commerce Store

A clean, minimal general store built with **Flask + SQLite** on the backend and **pure HTML/CSS/JS** (Jinja2 templates) on the frontend. Features a floating AI shopping assistant powered by **Claude** using **Retrieval-Augmented Generation (RAG)**.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🛒 Product browsing | Grid layout with category sidebar and price filters |
| 🔍 Live search | Filters products by name, description, and tags |
| 📄 Product detail pages | Full info, tags, breadcrumb navigation |
| 🤖 AI chat assistant | Floating bubble — asks Claude about any product |
| 🧠 RAG pipeline | Retrieves relevant products before every AI call |
| 💾 SQLite database | Zero setup, auto-seeded with 20 products on first run |
| 📱 Responsive | Works on desktop and mobile |

---

## 📁 Project Structure

```
ECOMMERCE-RAG/
├── app.py                  # Flask app factory + error handlers
├── seed.py                 # 20 sample products (auto-runs on startup)
├── requirements.txt        # Python dependencies
├── .env                    # Your API key goes here (never commit this)
├── extension.py                    
├── models/
│   └── product.py          # SQLAlchemy Product model
│
├── routes/
│   ├── pages.py            # GET /  and  GET /product/<id>  (HTML pages)
│   ├── products.py         # GET /api/products, /api/products/<id>, /api/categories
│   └── assistant.py        # POST /api/ask  (RAG + Claude)
│   └── admin.py
│
├── rag/
│   └── retriever.py        # Keyword scoring + context builder
│
├── templates/
├   |── admin/
│   |   └── dashboard.html 
│   |   └── login.html           
│   ├── base.html           # Shared layout: navbar + AI chat bubble
│   ├── index.html          # Shop page (product grid + filters)
│   ├── product.html        # Product detail page
│   └── 404.html            # Not found page
│
└── static/
|    └── css
|       └── admin.css           
│       └── style.css       # Full design system (CSS variables, animations)
|    └── js
|       └── main.js           
│       └── admin.js 

```

---

## 🚀 Quick Start

### 1. Clone / download the project
```bash
cd shop
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# Activate it:
# macOS / Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Anthropic API key
Open `.env` and replace the placeholder:
```
GROQ_API_KEY=sk-ant-your-real-key-here
```


### 5. Run the server
```bash
python app.py
```

### 6. Open in your browser
```
http://localhost:5000
```

The database is created and seeded with **all products** automatically on the first run.

---

## 🧠 How the RAG Pipeline Works

Every time a user sends a message in the chat:

```
User question
     ↓
retriever.py — tokenises the question, scores every product
     ↓
Top 5 most relevant products selected
     ↓
Products formatted into a context block
     ↓
Groq receives:  system prompt + context + user question
     ↓
Groq answers using ONLY the provided product data
```

The scoring considers:
- Keyword overlap between the question and product name / description / tags / category
- **Price-intent boost** — "cheap" / "budget" questions favour lower-priced products; "premium" / "best" questions favour higher-priced ones

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Shop home page |
| `GET` | `/product/<id>` | Product detail page |
| `GET` | `/api/products` | List products (supports `?search=`, `?category=`, `?max_price=`) |
| `GET` | `/api/products/<id>` | Single product JSON |
| `GET` | `/api/categories` | List all categories |
| `POST` | `/api/ask` | Ask the AI — body: `{"question": "..."}` |

### Example API call
```bash
curl -X POST http://localhost:5000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Best headphones under $300?"}'
```

---

## 🛠️ Customisation

### Add more products
Edit `seed.py` and add more `Product(...)` entries. Delete `instance/shop.db` and restart to re-seed.

### Change the AI model
In `routes/assistant.py`, change the `model` parameter:
```python
model="claude-opus-4-5"   # or claude-haiku-4-5-20251001 for faster/cheaper
```

### Upgrade retrieval to vector search
Replace the keyword scorer in `rag/retriever.py` with `sentence-transformers` embeddings for semantic search — the rest of the pipeline stays the same.

---

## 📦 Dependencies

```
flask            # Web framework
flask-sqlalchemy # ORM for SQLite
Groq Api        # Groq API client
python-dotenv    # Loads .env file
psycopg2-binary
```

---

## 🔒 Security Notes

- Never commit your `.env` file — add it to `.gitignore`
- The app runs in `debug=True` mode by default — set `debug=False` for production
- For production, use a proper WSGI server like `gunicorn`:  `gunicorn app:create_app()`
