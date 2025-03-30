import os

class Config:
    # Secret key for security
    SECRET_KEY = os.environ.get('SECRET_KEY', 'bcf06bfb3fd5f2acc8182dc58e447618')
    # if not SECRET_KEY:
    #     raise ValueError("SECRET_KEY is not set in the environment!")

    # Database configuration (default to PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///mydatabase.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'c6e3602605372d41ba124b92e96c7dc15987ddf4f910ad0c1c4b8e4846ab71dc')
    # if not JWT_SECRET_KEY:
    #     raise ValueError("JWT_SECRET_KEY is not set in the environment!")

    # CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:*')  # '*' for dev, specify in prod