from flask import Flask
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)



@app.route('/hello')
@cross_origin()
def hello():
    return "hello world"



#if __name__ == '__main__':   
#    app.run(host='localhost', port=6152)

if __name__ == "__main__":
    app.run()
