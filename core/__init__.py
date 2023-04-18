from flask import Flask

from dotenv import find_dotenv, load_dotenv
import os

from .extensions import db, migrate

load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        os.environ.get('DB_NAME')

    db.init_app(app)
    migrate.init_app(app, db,
                     render_as_batch=True)

    @app.route('/404')
    def not_found():
        return 'Not Found'

    # MODELS
    from .models import Character, Episode, Quote

    # routes
    from .routes.api import characters as characters_bp
    app.register_blueprint(characters_bp,\
                            url_prefix='/api/characters')
    from .routes.api import episodes as episodes_bp
    app.register_blueprint(episodes_bp,\
                            url_prefix='/api/episodes')


    return app