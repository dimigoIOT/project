from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def index_test():
    if request.method == 'GET':
        print("GET!")
        return render_template('index2.html')
    else:
        return "<p>error</p>"

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)