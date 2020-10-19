from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<center><h1>Hello, MotherFu**er</h1></center>'


if __name__ == '__main__':
    app.run()