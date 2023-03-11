from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .api.basic.users import user_blueprint
from .settings import ma, db
from .models.user import user_model


def create_app():
	app = Flask(__name__)
	app.config.from_pyfile("config.py")
	app.register_blueprint(user_blueprint)

	db.init_app(app)
	ma.init_app(app)

	# Settings for migrations
	migrate = Migrate()
	migrate.init_app(app, db)
	CORS(app)
	CORS(app, resources={r"/api/*": {"origins": "*"}})
	app.config["CORS_HEADERS"] = "Content-Type"
	return app
