from flask import Flask, render_template
import os


# Create a Flask app:
app = Flask(__name__)


# Render index:
@app.route('/')
def index():
    return render_template('index.html')


# Main:
if __name__ == '__main__':
    app.run(debug=True)
