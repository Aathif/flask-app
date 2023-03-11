from flask import Blueprint

user_blueprint = Blueprint("user_api", __name__)

from . import get_users, create_user
