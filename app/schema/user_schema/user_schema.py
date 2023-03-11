from app.settings import ma
from marshmallow import fields
from marshmallow.validate import Length
from app.models.user.user_model import User


class UserSchema(ma.Schema):
	id = fields.UUID(required=True, allow_none=False, data_key="id")
	first_name = fields.String(required=True, allow_none=False, data_key="firstName")
	last_name = fields.String(required=True, allow_none=False, data_key="lastName")
	age = fields.Integer(required=True, allow_none=False, data_key="age")
	user_name = fields.String(required=True, allow_none=False, data_key="userName")
	email = fields.Email(required=True, allow_none=False, data_key="email")
	password = fields.String(required=True, allow_none=False, data_key="password", validate=Length(min=8))
	date_created = fields.DateTime(required=True, allow_none=False, data_key="dateCreated")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
