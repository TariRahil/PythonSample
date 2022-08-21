from flask import Flask
from .config import Config
from json import load as json_load

def create_app(config_file=None):
	app=Flask(__name__)
	app.config.from_object(Config)
	if config_file is not None:
		app.config.from_file(config_file, load=json_load)
	
	print(app.config)
	return app
	
	
