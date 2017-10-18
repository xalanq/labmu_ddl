from flask import Flask
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import request
import hashlib
import os

app = Flask(__name__)

user_auth = dict()
pass_salt = str(os.urandom(23333))


def my_password_hash(password):
	return hashlib.sha512((password + pass_salt).encode('utf-8')).hexdigest()


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		user_name = request.form.get('username', 'null')
		user_pass = my_password_hash(request.form.get('password', 'null'))
		if user_auth.get(user_name) == user_pass:
			return jsonify(name=user_name, message="Welcome!!")
		return jsonify(name='', message="Invalid Username or Password.")
	else:
		return render_template('index.html')


if __name__ == '__main__':
	user_auth['a'] = my_password_hash('123')
	user_auth['b'] = my_password_hash('123')
	user_auth['c'] = my_password_hash('123')
	# app.debug = True
	app.run()