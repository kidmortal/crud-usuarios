from flask import Flask, jsonify, request
from bd import users


app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_user():
    return jsonify(users)


@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)


@app.route('/edit/<int:id>', methods=['PUT'])
def edit_user_by_id(id):
    edited_user = request.get_json()
    for index, user in enumerate(users):
        if user.get('id') == id:
            users[index].update(edited_user)
            return jsonify(users[index])


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    for index, user in enumerate(users):
        if user.get('id') == id:
            del users[index]
            return jsonify(users)


@app.route('/register', methods=['POST'])
def register_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(users)
