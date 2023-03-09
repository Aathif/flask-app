from . import basic_blueprint
from app.models.basic_user_model import User
from app.schema.basic_user_schema import BasicUserSchema


@basic_blueprint.route("/api/v1/users", methods=["GET"])
def index():
	basic_user_schema = BasicUserSchema(many=True)
	users = User.query.all()
	users_result_dump = basic_user_schema.dump(users)
	return users_result_dump
