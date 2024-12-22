from flask import Flask, render_template
from models import Tour, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["TEMPLATES_AUTO_RELOAD"] = True
db.init_app(app)

'''1. Додати контент в index.html (це нам не нада)
   2. Реалізувати сторінку турів (список)
   3. Реалізувати сторінку окремого тура
   4. Реалізувати сторінку додавання
   5. Зробити POST запит з обробкою тіла запиту (reqeust body). Приклад: {"name": "Києв",}'''

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tours")
def tours():
    tours = Tour.query.all()
    return render_template("tours.html")


@app.route("/add-departure", methods=["POST"])
def add_departure():
    pass


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)