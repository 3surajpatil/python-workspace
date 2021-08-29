from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def helloWorld():
    return "hello world"



if __name__ == '__main__':   
    app.run(host='localhost', port=6152)