from flask import Blueprint, jsonify, request
from .models import User, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Basic health check endpoint"""
    return jsonify({
        'status': 'healthy', 
        'message': 'Welcome to User Management Service'
    }), 200

@main_bp.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@main_bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    
    # Validate input
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409
    
    # Create new user
    new_user = User(
        username=data['username'], 
        email=data['email']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.to_dict()), 201