from flask import Flask, jsonify, request
from bd import usuarios


app = Flask(__name__)


@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(usuarios)


@app.route('/usuario/<int:id>', methods=['GET'])
def obter_usuarios_por_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)


@app.route('/editar/<int:id>', methods=['PUT'])
def editar_usuario(id):
    usuario_alterado = request.get_json()
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_alterado)
            return jsonify(usuarios[indice])


@app.route('/deletar/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]
            return jsonify(usuarios)
        

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)
    return jsonify(usuarios)




