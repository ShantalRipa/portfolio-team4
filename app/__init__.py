import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    # Ji-Oh just change the home.html to index.html to see your index.html
    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title="MLH Fellow", url=os.getenv("URL"))
