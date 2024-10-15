from flask import Flask

from database.session import db
from routes.transaction import register_routes
from settings.config import Config


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config())

	db.init_app(app)

	with app.app_context():
		db.create_all()

	register_routes(app)

	return app
