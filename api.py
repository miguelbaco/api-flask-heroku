from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def post(self):
        try:
           parser = reqparse.RequestParser()
           parser.add_argument('user',type=str,help='User address to create user')
           parser.add_argument('password',type=str,help='Password to create user')
           args=parser.parse_args()
           _userName=args['user']
           _userPassword=args['password']
           return {'Usuario': _userName, 'Password': _userPassword}

        except Exception as e:
           return {'error': str(e)}

api.add_resource(CreateUser, '/CreateUser')

if __name__ == '__main__':
    app.run(port=5003,debug=True)

