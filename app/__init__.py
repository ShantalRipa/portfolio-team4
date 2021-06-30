import os
from flask import Flask, request, render_template, send_from_directory, Response, jsonify
from dotenv import load_dotenv
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

@app.route('/')
def index():
    # Ji-Oh just change the home.html to index.html to see your index.html
    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/health')
def starting_url():
    status_code = Response(status=200)
    return status_code

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title="MLH Fellow", url=os.getenv("URL"))
