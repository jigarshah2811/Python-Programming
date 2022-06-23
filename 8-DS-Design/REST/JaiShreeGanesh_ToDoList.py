#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask("__name__")
auth = HTTPBasicAuth()
authenticated_users = {
    "jigar": "secret",
    "krupa": "secret"
}


@auth.get_password
def get_password(username):
    if username in authenticated_users:
        return authenticated_users.get(username)
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error": "UnAuthorized Access"}), 403)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


def make_public_task(task):
    task_with_uri = {}
    for field in task:
        if field == 'id':
            task_with_uri['url'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            task_with_uri[field] = task[field]
    return task_with_uri

"""
TO DO LIST REST APIs
"""
tasks = [
    {
        'id': 1,
        'title': "Buy Grocerries",
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn python',
        'done': False
    }
]


@app.route("/todo/tasks", methods=['GET'])
def get_tasks():
    return jsonify({'tasks': map(make_public_task, tasks)})


@app.route("/todo/tasks/<int:task_id>", methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return abort(404)
    else:
        return jsonify({'tasks': make_public_task(task[0])})


@app.route("/todo/tasks", methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or 'title' not in request.json:
        abort(404)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': make_public_task(task)}), 201


@app.route("/todo/tasks/<int:task_id>", methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if not request.json:
        abort(404)
    if len(task) == 0:
        abort(404)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'tasks': make_public_task(task[0])}), 201


@app.route("/todo/tasks/<int:task_id>", methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
