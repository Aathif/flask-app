import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:toor@localhost:5432/flask-app"
# os.environ.get("DATABASE_URI")
#     or 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_TRACK_MODIFICATIONS = False