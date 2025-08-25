import requests
import json
import random
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import threading
import time

app = Flask(__name__)
api = Api(app)

# Mock API Responses
responses = {
    'GET /users': {'status_code': 200, 'response': {'users': ['user1', 'user2', 'user3']}},
    'GET /users/1': {'status_code': 200, 'response': {'user': 'user1'}},
    'POST /users': {'status_code': 201, 'response': {'user': 'new_user'}},
    'PUT /users/1': {'status_code': 200, 'response': {'user': 'updated_user'}},
    'DELETE /users/1': {'status_code': 204, 'response': {}},
}

class API Simulator(Resource):
    def get(self, *args):
        response = responses.get(request.path)
        if response:
            return jsonify(response['response']), response['status_code']
        else:
            return jsonify({'error': 'Not Found'}), 404

    def post(self, *args):
        response = responses.get(request.path)
        if response:
            return jsonify(response['response']), response['status_code']
        else:
            return jsonify({'error': 'Not Found'}), 404

    def put(self, *args):
        response = responses.get(request.path)
        if response:
            return jsonify(response['response']), response['status_code']
        else:
            return jsonify({'error': 'Not Found'}), 404

    def delete(self, *args):
        response = responses.get(request.path)
        if response:
            return jsonify(response['response']), response['status_code']
        else:
            return jsonify({'error': 'Not Found'}), 404

api.add_resource(API Simulator, '/users', '/users/<int:user_id>')

def run_server():
    app.run(debug=True)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    print('API Simulator started. You can test the APIs using a tool like curl or Postman.')

    while True:
        time.sleep(1)