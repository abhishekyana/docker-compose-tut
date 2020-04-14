import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from TASKER import tasker

import redis
from rq import Queue

import numpy as np

app = Flask(__name__)

r = redis.Redis('redis_server')
q = Queue(connection=r)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

g = 0

@app.route("/")
def hello():
    return "Hello World!!!!!!! This is abhishek yanamandra"

@app.route("/ping")
def ping():
    return "PONG!!!!!!!"+str(np.random.randint(0,2000))

@app.route("/maketask")
def maketask():
    job = q.enqueue(tasker)
    q_len = len(q)
    return f"Task ({job.id}) added to queue at ({job.enqueued_at}). {q_len} tasks in the queue."

@app.route("/getback")
def getback():
    global g
    g+=1
    return jsonify({'d1':os.listdir('DATA'), 'd2':os.listdir('DATA2'), 'g':g})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
