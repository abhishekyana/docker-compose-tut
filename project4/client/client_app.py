import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! from clientttt apppppppp"

@app.route("/getback")
def getback():
    return str(os.listdir('DATA'))+str(os.listdir('DATA2'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
