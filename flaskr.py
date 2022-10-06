from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_home(name=None):
    return render_template('index.html', name=name)

@app.route('/test')
def index_test():
    return "<p>helloworld</p>"

app.run(debug = True)