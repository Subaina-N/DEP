from flask import Blueprint, request, jsonify
from models import db, User
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
main = Blueprint('main', __name__)

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

@main.route('/users/<int:id>', methods=['GET'])
@auth.login_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'username': user.username})

@main.route('/users/<int:id>', methods=['PUT'])
@auth.login_required
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    if 'username' in data:
        user.username = data['username']
    if 'password' in data:
        user.set_password(data['password'])
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username})

@main.route('/users/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
