from flask import Blueprint

basic_blueprint = Blueprint("basic_api", __name__)

from . import index
