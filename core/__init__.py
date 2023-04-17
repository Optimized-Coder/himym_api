from flask import Flask, jsonify

from dotenv import find_dotenv, load_dotenv
import os

from .extensions import db, migrate

load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_NAME')

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/404')
    def not_found():
        return 'Not Found'

    # MODELS
    from .models import Character

    # routes
    from .routes.api import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    return app