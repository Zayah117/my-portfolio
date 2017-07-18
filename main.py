from flask import Flask
from flask import render_template, request, redirect, url_for, flash

app = Flask(__name__, static_url_path='/static/*')

@app.route('/')
def front():
	return render_template('front.html')
