from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from subprocess import call

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("on", default=False)
parser.add_argument("off", default=False)
parser.add_argument("dim", default=False)
parser.add_argument("night", default=False)

class livingRoom(Resource):
	def post(self):
		args = parser.parse_args()
		if args.on == True:
			call("middle_earth.py living-room on")
		if args.off == True:	
			call("middle_earth.py living-room off")
		if args.dim == True:
			call("middle_earth.py living-room dim")	
		if args.night == True:
			call("middle_earth.py living-room night")
		return 201

class kittyCorner(Resource):
	def post(self):
		args = parser.parse_args()
		if args.on == True:
			call("middle_earth.py kitty-corner on")
		if args.off == True:
			call("middle_earth.py kitty-corner off")
		if args.dim == True:	
			call("middle_earth.py kitty-corner dim")
		if args.night == True:	
			call("middle_earth.py kitty-corner night")
		return 201

api.add_resurce(livingRoom, "/livingroom")
api.add_resurce(kittyCorner, "/kittycorner")

if __name__ == "__main__":
	app.run()
