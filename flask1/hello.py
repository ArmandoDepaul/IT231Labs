from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Big Blue World!'
  
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'