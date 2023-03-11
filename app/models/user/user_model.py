from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.settings import db
import uuid


class User(db.Model):
	id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	first_name = db.Column(db.String(20), unique=False, nullable=False)
	last_name = db.Column(db.String(20), unique=False, nullable=False)
	age = db.Column(db.Integer, nullable=False)
	user_name = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(30), unique=True, nullable=False)
	password = db.Column(db.String(256), nullable=False)
	date_created = db.Column(db.DateTime, server_default=func.now())

	def __init__(self, first_name, last_name, age, user_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.user_name = user_name
		self.email = email
		self.password = password

	def __repr__(self):
		return f"User : {self.first_name} {self.last_name}"
