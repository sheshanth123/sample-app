from flask import Flask
from flask import jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return "Success"
	
@app.route('/create')
def create_dir():
	os.mkdir(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
	return "done"
	
@app.route('/list')
def list_dir():
	return jsonify(dirlist = os.listdir())
	
if __name__ == '__main__':
	app.run()

