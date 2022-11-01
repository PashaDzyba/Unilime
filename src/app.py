from flask_marshmallow import Marshmallow
from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields
from core.config import system_config
from webargs.flaskparser import use_args

app = Flask(__name__)

#

# Base
app.config['SQLALCHEMY_DATABASE_URI'] = system_config.database_url
db = SQLAlchemy(app)

# Cache
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)
cache.init_app(app)
# Models
product_review = db.Table('product_review',
                          db.Column('product_id', db.Integer, db.ForeignKey(
                              'products.id'), primary_key=True),
                          db.Column('review_id', db.Integer, db.ForeignKey(
                              'reviews.id'), primary_key=True)
                          )


class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String, nullable=True)
    asin = db.Column(db.String, nullable=True)
    reviews = db.relationship("Reviews", secondary=product_review, backref=db.backref('reviews'), lazy='dynamic')


class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String, nullable=True)
    asin = db.Column(db.String, nullable=True)
    review = db.Column(db.String, nullable=True)
    products = db.relationship("Products", secondary=product_review, back_populates='reviews', overlaps="reviews")


migrate = Migrate(app, db)

# Schemas
ma = Marshmallow(app)


class ReviewSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    asin = fields.String()
    review = fields.String()


class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    asin = fields.String()

    reviews = fields.List(fields.Nested(ReviewSchema))


products_schema = ProductSchema(many=True)
review_schema = ReviewSchema()


@app.route("/get_data", methods=["GET"])
@cache.cached(timeout=5, query_string=True)
def get_data():
    products = db.session.query(Products).join(product_review).join(Reviews).all()
    result = products_schema.dump(products)
    return {"result": result}


@app.route("/updated_data/<int:id>", methods=['PUT'])
def update_review(id):
    query = db.session.query(Reviews).join(product_review).join(Products).filter(Products.id == id).first()

    title = request.json['title']
    review = request.json['review']

    query.title = title
    query.review = review

    db.session.commit()

    return review_schema.jsonify(query)


if __name__ == '__main__':
    app.run()
