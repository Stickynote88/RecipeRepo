import pandas as pd 
import numpy as np
from flask import Flask 
from flask_restful import reqparse, abort, Api, Resource 
from flask import Flask, render_template

app = Flask(__name__)
api = Api(app)

web_data = pd.DataFrame(data={
	'A' : [1,2,3,4,5,5],
	'B' : [5,5,4,3,2,1],
	'C' : ['t','e','s','t','!']
})


@app.route('/')
def index():
	return web_data.to_html() 


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
	app.run(host='0.0.0.0',debug=True)