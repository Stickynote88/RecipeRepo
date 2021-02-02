import pandas as pd 
import numpy as np
from flask import Flask 
from flask_restful import reqparse, abort, Api, Resource 
from flask import Flask, render_template
import psycopg2
from pyconfig import host, database, user, password

app = Flask(__name__)
api = Api(app)


conn = psycopg2.connect(
  host=host,
  database=database,
  user=user,
  password=password
)

web_data =  pd.read_sql_query('''select * from public.food''', conn)


@app.route('/')
def index():
	return web_data.head(100).to_html() 


class Recipe(Resource):
# adds restful functionality 
# link : https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example

	def get(self, recipe_id):
		# handles HTTP GET request at /recipe/<recipe_id>
		return_df = web_data.loc[web_data['fdc_id'] == int(recipe_id)]
		if len(return_df.index) == 0:
			# if todo doesn't exist 
			abort(
				404, 
				message="recipe {} doesn't exist".format(recipe_id)
			)
		else :
			return return_df.to_json(orient='table')

	def put(self, recipe_id):
		# handles HTTP PUT request at /recipe/<recipe_id>
		return "something"

class RecipeSearch(Resource):

	def get(self, query_str):
		return_df = web_data.loc[ 
			web_data['description'].str.contains(query_str) 
		]
		if len(return_df.index) == 0:
			abort(
				404,
				message="found no recipes matching {}".format(query_str)
			)
		else:
			return return_df.to_json(orient='table')

# registers Recipe object to handle /recipe
api.add_resource(Recipe, '/recipe/<recipe_id>')
api.add_resource(RecipeSearch, '/recipe/search/<query_str>')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)