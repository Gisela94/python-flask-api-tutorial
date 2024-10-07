from flask import Flask
from flask import Flask, jsonify
from flask import request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text=jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Paso 1: Recibir la posición a eliminar
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400  # Manejar un índice fuera de rango

    # Paso 2: Eliminar la tarea de la lista 'todos'
    del todos[position]

    # Paso 3: Retornar la lista actualizada de todos
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)