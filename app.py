from flask import Flask, render_template

# Creating Flask object
app = Flask(__name__)

# Setting app starting index
@app.route('/')
# Displays index.html 
def index():
	return render_template('index.html')
@app.route('/test')
def testPage():
	return render_template('other.html')

# Log errors to web page
if __name__ == '__main__':
	app.run(debug=True)