from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify, flash
from functools import wraps
from extensions import db
from models.product import Product

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# ── Change this password to whatever you want ──
ADMIN_PASSWORD = "12345"


# ── Login required decorator ──────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin.login"))
        return f(*args, **kwargs)
    return decorated


# ── Login / Logout ────────────────────────────────────────────
@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin.dashboard"))
        error = "Incorrect password. Try again."
    return render_template("admin/login.html", error=error)


@admin_bp.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin.login"))


# ── Dashboard ─────────────────────────────────────────────────
@admin_bp.route("/")
@login_required
def dashboard():
    products   = Product.query.order_by(Product.id.desc()).all()
    categories = sorted(set(p.category for p in products))
    total      = len(products)
    in_stock   = sum(1 for p in products if p.in_stock)
    return render_template("admin/dashboard.html",
                           products=products,
                           categories=categories,
                           total=total,
                           in_stock=in_stock)


# ── Add Product ───────────────────────────────────────────────
@admin_bp.route("/add", methods=["POST"])
@login_required
def add_product():
    name        = request.form.get("name",        "").strip()
    price       = request.form.get("price",       "0").strip()
    category    = request.form.get("category",    "").strip()
    new_cat     = request.form.get("new_category","").strip()
    description = request.form.get("description", "").strip()
    tags        = request.form.get("tags",        "").strip()
    image_url   = request.form.get("image_url",   "").strip()
    in_stock    = request.form.get("in_stock") == "on"

    # Allow custom category
    final_category = new_cat if new_cat else category

    if not name or not final_category or not description:
        flash("Name, category, and description are required.", "error")
        return redirect(url_for("admin.dashboard"))

    try:
        price_val = float(price)
    except ValueError:
        flash("Price must be a valid number.", "error")
        return redirect(url_for("admin.dashboard"))

    product = Product(
        name=name, price=price_val, category=final_category,
        description=description, tags=tags,
        image_url=image_url, in_stock=in_stock
    )
    db.session.add(product)
    db.session.commit()
    flash(f'✅ "{name}" added successfully!', "success")
    return redirect(url_for("admin.dashboard"))


# ── Get single product (for edit modal) ──────────────────────
@admin_bp.route("/product/<int:pid>", methods=["GET"])
@login_required
def get_product(pid):
    p = Product.query.get_or_404(pid)
    return jsonify(p.to_dict())


# ── Edit Product ──────────────────────────────────────────────
@admin_bp.route("/edit/<int:pid>", methods=["POST"])
@login_required
def edit_product(pid):
    p = Product.query.get_or_404(pid)

    p.name        = request.form.get("name",        p.name).strip()
    p.category    = request.form.get("category",    p.category).strip()
    new_cat       = request.form.get("new_category","").strip()
    p.description = request.form.get("description", p.description).strip()
    p.tags        = request.form.get("tags",        p.tags).strip()
    p.image_url   = request.form.get("image_url",   p.image_url).strip()
    p.in_stock    = request.form.get("in_stock") == "on"

    if new_cat:
        p.category = new_cat

    try:
        p.price = float(request.form.get("price", p.price))
    except ValueError:
        flash("Price must be a valid number.", "error")
        return redirect(url_for("admin.dashboard"))

    db.session.commit()
    flash(f'✅ "{p.name}" updated successfully!', "success")
    return redirect(url_for("admin.dashboard"))


# ── Delete Product ────────────────────────────────────────────
@admin_bp.route("/delete/<int:pid>", methods=["POST"])
@login_required
def delete_product(pid):
    p = Product.query.get_or_404(pid)
    name = p.name
    db.session.delete(p)
    db.session.commit()
    flash(f'🗑️ "{name}" deleted.', "success")
    return redirect(url_for("admin.dashboard"))
