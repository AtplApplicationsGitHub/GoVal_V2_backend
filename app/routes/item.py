from flask import Blueprint, request, jsonify
from extensions import db
from flask_jwt_extended import jwt_required
from models.item import Item

item_bp = Blueprint('item', __name__)

# Create an item
@item_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item created successfully!"}), 201

# Get all items
@item_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description} for item in items]), 200

# Get single item
@item_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found!"}), 404
    return jsonify({"id": item.id, "name": item.name, "description": item.description}), 200

# Update an item
@item_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found!"}), 404

    data = request.json
    item.name = data['name']
    item.description = data.get('description', item.description)

    db.session.commit()
    return jsonify({"message": "Item updated successfully!"}), 200

# Delete an item
@item_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found!"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully!"}), 200
