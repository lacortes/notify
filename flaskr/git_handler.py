from flask import request
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        body = request.get_json()
        return {'you_sent': body}, 201


