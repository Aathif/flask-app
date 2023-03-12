from datetime import datetime, timedelta
from flask import request
from marshmallow import ValidationError

from app import config
from app.api.users import user_blueprint
from app.schema.user_schema.user_schema import UserSchema
from app.models.user.user_model import User
from app.utils.password_ops_utils import validate_password
import jwt


@user_blueprint.route("/api/v1/login", methods=["POST"])
def user_login():
	use_schema = UserSchema(only=("user_name", "password",))
	try:
		user_credentials = use_schema.load(request.get_json())
	except ValidationError as err:
		return {"errors": err.messages}, 422

	user = User.query.filter_by(user_name=user_credentials["user_name"]).first()
	if validate_password(user.password, user_credentials["password"]):
		token = jwt.encode({
			'user_id': str(user.id),
			'exp': datetime.utcnow() + timedelta(minutes=30)
		}, config.SECRET_KEY)

		success_return_schema = UserSchema(only=("user_name",))
		return_response = success_return_schema.dump(user)
		return_response["token"] = token
		return return_response

