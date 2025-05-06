from flask import Flask,render_template

app = Flask(__name__)
print(__name__)


@app.route('/<username>/<int:age>')
def hello(username = None, age = None):
    return  render_template('index.html', name = username, age = age)


@app.route('/form')
def form():
        return render_template('Form.html')