from flask import Flask 
from flask_restful import reqparse, abort, Api, Resource 
from flask import Flask, render_template

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
	return render_template('index.html')


class Recipie(Resource):
# adds restful functionality 
# link : https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example

	def get(self, recipie_id):
		# handles HTTP GET request at /recipie/<recipie_id>
		if True : 
			# if todo doesn't exist 
			abort(
				404, 
				message="recipie {} doesn't exist".format(recipie_id)
			)
		else :
			return "something"

	def put(self, recipie_id):
		# handles HTTP PUT request at /recipie/<recipie_id>
		return "something"

# registers Recipie object to handle /recipie
api.add_resource(Recipie, '/recipie/<recipie_id>')

if __name__ == '__main__':
	app.run(debug=True)