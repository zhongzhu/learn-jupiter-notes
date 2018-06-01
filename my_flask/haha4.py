from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/todo/<string:todo_id>')
class Todo(Resource):
    def get(self, todo_id):
        print(todos)
        return {todo_id: todos[todo_id]}

@api.route('/todo')
class Todos(Resource):
    def post(self):
        # todo_id = request.form['id']
        # todo_data = request.form['data']

        j = request.get_json()
        todo_id = j['id']
        todo_data = j['data']
        todos[todo_id] = todo_data
        return {todo_id: todo_data}
