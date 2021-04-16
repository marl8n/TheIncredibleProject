from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello I hope you\'ll hava a great day!!'
