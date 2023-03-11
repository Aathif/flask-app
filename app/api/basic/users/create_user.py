from flask import request
from marshmallow import ValidationError
from app.settings import db
from app.api.basic.users import user_blueprint
from app.models.user.user_model import User
from app.schema.user_schema.user_schema import UserSchema
import hashlib


@user_blueprint.route("/api/v1/user", methods=["POST"])
def create_user():
	try:
		user_schema = UserSchema(only=("first_name", "last_name", "user_name", "email", "age", "password",))
		request_params = user_schema.load(request.get_json())
	except ValidationError as err:
		return {"errors": err.messages}, 422

	hashed_password = hashlib.sha256(request_params["password"].encode()).hexdigest()

	user = User(first_name=request_params["first_name"], last_name=request_params["last_name"],
	            age=request_params["age"], user_name=request_params["user_name"], email=request_params["email"],
	            password=hashed_password)
	db.session.add(user)
	db.session.commit()
	success_return_schema = UserSchema(only=("first_name", "last_name", "user_name", "email", "age",))
	return_response = success_return_schema.dump(user)
	return return_response
