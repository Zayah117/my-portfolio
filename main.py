from flask import Flask
from flask import render_template, request, redirect, url_for, flash

import json

app = Flask(__name__, static_url_path='/static/*')

with open('data.json') as data_file:
	data = json.load(data_file)

@app.route('/')
def front():
	return render_template('front.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
