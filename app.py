from flask import Flask
from db import db
from models import StoreModel, ItemModel

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return "Практична робота 3 — SQLAlchemy One-to-Many"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Створюємо таблиці при запуску
    app.run(debug=True)
