from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json
import urllib.request

# urllib.request to make a request to api
import requests


app = Flask(__name__)

@app.route('/', methods =['GET'])
def finding():
	# source contain json data from api
	# communication from consumer service to fast API server here
	response = urllib.request.urlopen('http://service_pastry/pastries').read()
	# converting JSON data to a dictionary
	list_of_data = json.loads(response)
	data = {"pastries":list_of_data}
	return render_template('index.html', data = data)
	

if __name__ == '__main__':
	app.run(debug = True, port=8000)
