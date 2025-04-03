import os

class Config:
    # Secret key for security
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is not set in the environment!")

    # Database configuration (default to PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is not set in the environment!")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY is not set in the environment!")

    # CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'https://dev.goval.app:2053')  # '*' for dev, specify in prod
