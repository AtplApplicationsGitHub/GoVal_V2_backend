# app/__init__.py
from flask import Flask
from config import Config
from extensions import db, migrate, jwt, cors
from flask_jwt_extended import JWTManager
from app.errors import register_error_handlers
from app.routes.auth import auth_bp
from flask_cors import CORS

def create_app(config_class=Config):
    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)             # Initialize SQLAlchemy
    migrate.init_app(app, db)    # Initialize Flask-Migrate for DB migrations
    jwt.init_app(app)            # Initialize JWTManager
    cors.init_app(app)           # Initialize CORS support

    # Register blueprints and routes
    # register_routes(app)         # Register all routes from the app

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Register custom error handlers
    register_error_handlers(app)

    # Enable CORS with specified origins (from config)
    CORS(app, origins=app.config['CORS_ORIGINS'].split(','))

    return app

def register_routes(app):
    from app.routes.auth import auth_bp
    from app.routes.item import item_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(item_bp, url_prefix='/api')
