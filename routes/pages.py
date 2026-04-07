from flask import Blueprint, render_template, abort
from models.product import Product

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def index():
    return render_template("index.html")


@pages_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)
