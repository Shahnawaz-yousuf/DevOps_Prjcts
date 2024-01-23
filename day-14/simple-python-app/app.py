from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Shahnawaz DevOps_Engineer!!!'

if __name__ == '__main__':
    app.run()

