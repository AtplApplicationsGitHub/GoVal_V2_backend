# app/models/user.py
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        """Hash the password before saving it to the database."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against a plain password."""
        return check_password_hash(self.password, password)
