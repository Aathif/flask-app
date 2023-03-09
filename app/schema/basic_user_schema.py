from app.settings import ma
from app.models.basic_user_model import User


class BasicUserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
