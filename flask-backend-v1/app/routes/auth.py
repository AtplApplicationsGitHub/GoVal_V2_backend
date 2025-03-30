# app/routes/auth.py
from flask import Blueprint, request, jsonify
from extensions import db
from app.models.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

# Define Blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    # Check if the user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "User with this email already exists!"}), 400

    # Create new user and hash the password
    new_user = User(email=data['email'])
    new_user.set_password(data['password'])

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"User registered with email: {new_user.email}"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    # Check if the user exists and verify password
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({"message": "Invalid email or password!"}), 401

    # Generate JWT token for the user
    access_token = create_access_token(identity=str(user.id))
    
    return jsonify(access_token=access_token), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    print(f"JWT Identity: {user_id}")
    user = User.query.get(user_id)

    if user is None:
        return jsonify({"message": "User not found!"}), 404

    return jsonify({
        "id": user.id,
        "email": user.email
    })

@auth_bp.route('/profile/update', methods=['PUT'])
@jwt_required()
def update_profile():
    # Get current user from JWT token
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.json

    # Update email and/or password if provided
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.set_password(data['password'])

    db.session.commit()  # Save changes to the database

    return jsonify({
        "message": "Profile updated successfully",
        "email": user.email
    }), 200

@auth_bp.route('/profile/delete', methods=['DELETE'])
@jwt_required()
def delete_profile():
    # Get current user from JWT token
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)  # Delete the user from the database
    db.session.commit()  # Commit the changes

    return jsonify({"message": "Profile deleted successfully"}), 200
