from flask import Flask, jsonify, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Cafe TABLE Configuration


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record


@app.route("/cafes", methods=["GET"])
def get_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

# HTTP POST - Create Record


@app.route("/cafes", methods=["POST"])
def add_cafe():
    new_cafe_data = request.get_json()
    new_cafe = Cafe(
        name=new_cafe_data["name"],
        map_url=new_cafe_data["map_url"],
        img_url=new_cafe_data["img_url"],
        location=new_cafe_data["location"],
        seats=new_cafe_data["seats"],
        has_toilet=bool(new_cafe_data["has_toilet"]),
        has_wifi=bool(new_cafe_data["has_wifi"]),
        has_sockets=bool(new_cafe_data["has_sockets"]),
        can_take_calls=bool(new_cafe_data["can_take_calls"]),
        coffee_price=new_cafe_data.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(message="Cafe added successfully"), 201

# HTTP PUT/PATCH - Update Record


@app.route("/cafes/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    update_data = request.get_json()
    if 'name' in update_data:
        cafe.name = update_data['name']
    if 'map_url' in update_data:
        cafe.map_url = update_data['map_url']
    if 'img_url' in update_data:
        cafe.img_url = update_data['img_url']
    if 'location' in update_data:
        cafe.location = update_data['location']
    if 'seats' in update_data:
        cafe.seats = update_data['seats']
    if 'has_toilet' in update_data:
        cafe.has_toilet = bool(update_data['has_toilet'])
    if 'has_wifi' in update_data:
        cafe.has_wifi = bool(update_data['has_wifi'])
    if 'has_sockets' in update_data:
        cafe.has_sockets = bool(update_data['has_sockets'])
    if 'can_take_calls' in update_data:
        cafe.can_take_calls = bool(update_data['can_take_calls'])
    if 'coffee_price' in update_data:
        cafe.coffee_price = update_data['coffee_price']

    db.session.commit()
    return jsonify(message="Cafe updated successfully"), 200

# HTTP DELETE - Delete Record


@app.route("/cafes/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(message="Cafe deleted successfully"), 200


if __name__ == '__main__':
    app.run(debug=True)
