from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, default="https://picsum.photos/200/300?grayscale", nullable=False)
    average_rating = db.Column(db.Float, default=0.0, nullable=False)
    departure_id = db.Column(db.Integer, db.ForeignKey("departure.id"), nullable=False)


class Departure(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tours = db.relationship("Tour", backref="departure", lazy=True)
