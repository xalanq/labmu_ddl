from flask import Flask
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import request

app = Flask(__name__)

user_info = {}


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return render_template('index.html')
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run()