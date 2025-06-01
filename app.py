from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required
from db import db
from models import UserModel, StoreModel, ItemModel
from resources.user import UserRegister, UserLogin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret"  # заміни у справжньому проєкті

db.init_app(app)
jwt = JWTManager(app)

@app.route("/")
@jwt_required()
def home():
    return {"message": "Тільки для авторизованих користувачів!"}

app.add_url_rule("/register", view_func=UserRegister.as_view("register"))
app.add_url_rule("/login", view_func=UserLogin.as_view("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
