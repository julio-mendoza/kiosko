from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/api')

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug = True)
