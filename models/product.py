from extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(120), nullable=False)
    price       = db.Column(db.Float,  nullable=False)
    category    = db.Column(db.String(60),  nullable=False)
    description = db.Column(db.Text,   nullable=False)
    tags        = db.Column(db.String(255), default="")
    image_url   = db.Column(db.String(255), default="")
    in_stock    = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id":          self.id,
            "name":        self.name,
            "price":       self.price,
            "category":    self.category,
            "description": self.description,
            "tags":        self.tags,
            "image_url":   self.image_url,
            "in_stock":    self.in_stock,
        }
