import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('prac.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/gibson')
def gibson():
    return render_template('gibson.html', title="MLH Fellow", url=os.getenv("URL"))
