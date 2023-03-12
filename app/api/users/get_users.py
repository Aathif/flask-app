from app.api.users import user_blueprint
from app.models.user.user_model import User
from app.schema.user_schema.user_schema import UserSchema


@user_blueprint.route("/api/v1/users", methods=["GET"])
def index():
	user_schema = UserSchema(many=True, only=("id", "first_name", "last_name", "user_name", "email", "age", "date_created",))
	users = User.query.all()
	users_result_dump = user_schema.dump(users)
	return users_result_dump
