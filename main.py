from flask import Flask, jsonify, request
from bd import users
from user_form import UserRegistrationForm


app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_user():
    return jsonify(users)


@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)


@app.route('/users/edit/<int:id>', methods=['PUT'])
def edit_user_by_id(id):
    edited_user = request.get_json()
    for index, user in enumerate(users):
        if user.get('id') == id:
            users[index].update(edited_user)
            return jsonify(users[index])


@app.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    for index, user in enumerate(users):
        if user.get('id') == id:
            del users[index]
            return jsonify(users)


@app.route('/users', methods=['POST'])
def register_user():
    json_request = request.get_json()
    form = UserRegistrationForm.from_json(json_request)
    valid_form = form.validate()
    print(form.errors)
    if valid_form:
        new_user = request.get_json()
        users.append(new_user)
        return jsonify(users)
    else:
        return form.errors
