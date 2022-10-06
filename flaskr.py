from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_home():
    return render_template('index.html')

@app.route('/test')
def index_test():
    return "<p>helloworld</p>"

app.run(debug = True)