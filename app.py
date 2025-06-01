from flask import Flask
from db import db
from models import StoreModel, ItemModel

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def home():
    return "One-to-Many SQLAlchemy demo"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
