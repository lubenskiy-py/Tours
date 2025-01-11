from flask import Flask, render_template, request, redirect, url_for
from models import Tour, db, Departure
from forms import AddTourForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "bimba"
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tours")
def tours():
    tours = Tour.query.all()
    return render_template("tours.html")


@app.route("/add-departure", methods=["POST"])
def add_departure():
    data = request.json
    try:
        name = data["name"]
        if name == "":
            return {"error": "you_are_invalid(not me)"}, 400
        new_departure = Departure(name=name)
        db.session.add(new_departure)
        db.session.commit()
        return {"message": f"name {name} added"}, 201
    except KeyError:
        return {"error": "you_are_invalid(not me)"}, 400


@app.route("/add-tour", methods=["POST", "GET"])
def add_tour():
    form = AddTourForm()
    form.departure_id.choices = Departure.query.with_entities(Departure.id, Departure.name).all()
    if form.validate_on_submit():
        new_tour = Tour(
            title=form.title.data,
            price=form.price.data,
            description=form.description.data,
            image_url=form.image_url.data or None,
            departure_id=form.departure_id.data
        )
        print(form.image_url.data)
        print(type(form.image_url.data))
        db.session.add(new_tour)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_tour.html", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
