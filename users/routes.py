# users/routes.py
from flask import Flask, request, jsonify
from users.models import User  # Corrigindo o import do modelo

app = Flask(__name__)

users = []


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(id=len(users) + 1, username=data['username'], email=data['email'])
    users.append(user)
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201


@app.route('/users', methods=['GET'])
def get_users():
    users_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(users_data)
