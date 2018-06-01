from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_httpauth import HTTPTokenAuth
import jwt

todos = {}

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

app = Flask(__name__)
api = Api(app, authorizations=authorizations, security='apikey')
app.config['SECRET_KEY'] = 'donottellanyone'
auth = HTTPTokenAuth('Bearer')

apikeys = ['key1', 'key2']
for key in apikeys:
    print('*** token for {}: {}\n'.format(key, jwt.encode({'apikey': key}, app.config['SECRET_KEY'])))

@auth.verify_token
def verify_token(token):
    try:
        key = jwt.decode(token, app.config['SECRET_KEY'])['apikey']
    except:
        return False
    
    return key in apikeys

todo_item = api.model('Todo', {'todo': fields.String('Describe your todo in a sentence.')})

@api.route('/todo/<int:todo_id>')
class Todo(Resource):
    @auth.login_required
    def get(self, todo_id):
        if not todo_id in todos:
            return {'message': 'invalid todo id'}, 401
        return {todo_id: todos[todo_id]}

@api.route('/todo')
class TodoList(Resource):
    @auth.login_required
    def get(self):
        return todos

    @api.expect(todo_item)
    @auth.login_required
    def put(self):
        todo_id = len(todos) + 1
        todos[todo_id] = api.payload['todo']
        return {todo_id: todos[todo_id]}