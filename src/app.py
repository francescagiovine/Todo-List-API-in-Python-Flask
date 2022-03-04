from flask import Flask, jsonify, request
app = Flask(__name__)
import json


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_data = request.data
    data = json.loads(request_data)
    todos.append(data)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)



    #print("Incoming request with the following body", request_body)
    #return 'Response for the POST todo'



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)