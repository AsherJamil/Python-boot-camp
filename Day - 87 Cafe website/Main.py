from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Cafe(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(250), unique=True, nullable=False)
    map_url: str = db.Column(db.String(500), nullable=False)
    img_url: str = db.Column(db.String(500), nullable=False)
    location: str = db.Column(db.String(250), nullable=False)
    has_sockets: bool = db.Column(db.Boolean, nullable=False)
    has_toilet: bool = db.Column(db.Boolean, nullable=False)
    has_wifi: bool = db.Column(db.Boolean, nullable=False)
    can_take_calls: bool = db.Column(db.Boolean, nullable=False)
    seats: str = db.Column(db.String(250))
    coffee_price: str = db.Column(db.String(250))


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired(), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets')
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has WiFi')
    can_take_calls = BooleanField('Can Take Calls')
    seats = StringField('Seats')
    coffee_price = StringField('Coffee Price')
    submit = SubmitField('Submit')


@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )  # type: ignore
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/delete/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/api/cafes')
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify([{
        'id': cafe.id,
        'name': cafe.name,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'has_sockets': cafe.has_sockets,
        'has_toilet': cafe.has_toilet,
        'has_wifi': cafe.has_wifi,
        'can_take_calls': cafe.can_take_calls,
        'seats': cafe.seats,
        'coffee_price': cafe.coffee_price
    } for cafe in cafes])


if __name__ == '__main__':
    app.run(debug=True)
