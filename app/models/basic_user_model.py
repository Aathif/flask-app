from sqlalchemy.dialects.postgresql import UUID
from app.settings import db
import uuid


class User(db.Model):
	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	name = db.Column(db.String(20), unique=False, nullable=False)
	age = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Name : {self.first_name}, Age: {self.age}"
