from flask import Flask 
from flask_restful import reqparse, abort, Api, Resource 
from flask import Flask, render_template

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
	return 'Hi Jonathan'


class Recipie(Resource):
	def get(self, recipie_id):
		if True : 
			# if todo doesn't exist 
			abort(
				404, 
				message="recipie {} doesn't exist".format(recipie_id)
			)
		else :
			return "something"

	def edit(self, recipie_id):
		return "something"

api.add_resource(Recipie, '/recipie/<recipie_id>')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)