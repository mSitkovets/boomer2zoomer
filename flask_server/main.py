from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/word-detect')
def serve_word_detect():
    return 'test: word-detect'
