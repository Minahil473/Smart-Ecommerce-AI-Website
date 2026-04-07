from flask import Blueprint, jsonify, request
from models.product import Product

products_bp = Blueprint("products", __name__)


@products_bp.route("/products")
def get_products():
    search    = request.args.get("search",   "").strip()
    category  = request.args.get("category", "").strip()
    max_price = request.args.get("max_price", type=float)

    q = Product.query
    if search:
        like = f"%{search}%"
        q = q.filter(
            Product.name.ilike(like) |
            Product.description.ilike(like) |
            Product.tags.ilike(like)
        )
    if category:
        q = q.filter(Product.category == category)
    if max_price is not None:
        q = q.filter(Product.price <= max_price)

    return jsonify([p.to_dict() for p in q.all()])


@products_bp.route("/products/<int:pid>")
def get_product(pid):
    return jsonify(Product.query.get_or_404(pid).to_dict())


@products_bp.route("/categories")
def get_categories():
    rows = Product.query.with_entities(Product.category).distinct().all()
    return jsonify(sorted(r[0] for r in rows))
