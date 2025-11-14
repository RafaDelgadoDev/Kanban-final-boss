from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# data base da memoria
tasks = []
next_id = 1

def find_task(task_id):
    return next((t for t in tasks if t['id'] == task_id), None)

@app.route('/')
def index():
    return jsonify({"message": "Task Manager API - TechFlow Solutions (demo)"}), 200

# criar um novo
@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({"error": "title is required"}), 400
    task = {
        "id": next_id,
        "title": title,
        "description": data.get('description',''),
        "status": data.get('status','todo'),
        "priority": data.get('priority','medium')
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

# ler todos
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200

# ;er so um
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    t = find_task(task_id)
    if not t:
        return jsonify({"error":"not found"}), 404
    return jsonify(t), 200

# so pra atualizar 
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    t = find_task(task_id)
    if not t:
        return jsonify({"error":"not found"}), 404
    data = request.get_json() or {}
    t['title'] = data.get('title', t['title'])
    t['description'] = data.get('description', t['description'])
    t['status'] = data.get('status', t['status'])
    t['priority'] = data.get('priority', t.get('priority','medium'))
    return jsonify(t), 200

# como inputar o delete
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    t = find_task(task_id)
    if not t:
        return jsonify({"error":"not found"}), 404
    tasks.remove(t)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
