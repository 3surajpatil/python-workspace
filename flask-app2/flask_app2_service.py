from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)



@app.route('/hello')
@cross_origin()
def helloWorld():
    return "hello world..! i am from flask_app2_service "

if __name__ == '__main__':   
    app.run(host='0.0.0.0', port=6153)
