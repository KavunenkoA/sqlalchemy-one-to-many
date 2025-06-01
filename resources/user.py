from flask import request, jsonify
from flask.views import MethodView
from models import UserModel
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserRegister(MethodView):
    def post(self):
        data = request.get_json()
        if UserModel.query.filter_by(username=data["username"]).first():
            return {"message": "User already exists."}, 400

        user = UserModel(
            username=data["username"],
            password=generate_password_hash(data["password"])
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully."}, 201

class UserLogin(MethodView):
    def post(self):
        data = request.get_json()
        user = UserModel.query.filter_by(username=data["username"]).first()

        if user and check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        return {"message": "Invalid credentials"}, 401
