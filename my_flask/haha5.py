from flask import Flask, request
from flask_restplus import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/todo/<string:todo_id>')
class Todo(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

todo_item = api.model('Todo', {
    'id': fields.String('id of the todo'),
    'data': fields.String('Describe your todo in a sentence.')
})

@api.route('/todo')
class Todos(Resource):
    @api.expect(todo_item)
    def post(self):
        todo_id = api.payload['id']
        todo_data = api.payload['data']
        todos[todo_id] = todo_data

        return {todo_id: todo_data}


