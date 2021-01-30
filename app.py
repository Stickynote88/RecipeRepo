from flask import Flask 
from flask_restful import reqparse, abort, Api, Resource 
from flask import Flask, render_template

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
	return render_template('index.html')


class Recipe(Resource):
# adds restful functionality 
# link : https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example

	def get(self, recipe_id):
		# handles HTTP GET request at /recipe/<recipe_id>
		if True : 
			# if todo doesn't exist 
			abort(
				404, 
				message="recipe {} doesn't exist".format(recipe_id)
			)
		else :
			return "something"

	def put(self, recipe_id):
		# handles HTTP PUT request at /recipe/<recipe_id>
		return "something"

# registers Recipe object to handle /recipe
api.add_resource(Recipe, '/recipe/<recipe_id>')

if __name__ == '__main__':
	app.run(debug=True)