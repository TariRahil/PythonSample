from flask import Blueprint, Flask
from .config import Config
from flask_restful import Api
from json import load as json_load
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint(name="apiv1_bp", import_name=__name__, url_prefix="/api/v1")
apiv1=Api(apiv1_bp)

from . import resource

def create_app(config_file = None):
	app=Flask(__name__)
	app.config.from_object(Config)
	if config_file is not None:
		app.config.from_file(config_file, load = json_load)
		
	db.init_app(app)
	mg.init_app(app , db)
	ma.init_app(app)
	
	"""print(app.config)"""
	app.register_blueprint(apiv1_bp)
	return app
	
	
