from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from extensions import db
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    uri = os.getenv("DATABASE_URL", "sqlite:///shop.db")

    # Fix for Supabase / Render PostgreSQL
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "ragalia-secret-key-change-in-production"

    db.init_app(app)

    from routes.pages import pages_bp
    from routes.products import products_bp
    from routes.assistant import assistant_bp
    from routes.admin import admin_bp

    app.register_blueprint(pages_bp)
    app.register_blueprint(products_bp, url_prefix="/api")
    app.register_blueprint(assistant_bp, url_prefix="/api")
    app.register_blueprint(admin_bp)

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        if "/api/" in str(e):
            return jsonify({"error": "Not found"}), 404
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    # DB setup & seed
    with app.app_context():
        db.create_all()
        from seed import seed_products
        seed_products(db)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)