import os
import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = os.getenv('REDISTOGO_URL', 'redis://redis_server2:6379')

def run_worker():
    conn = redis.from_url(redis_url)
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        print("WORKING   KKKKK")
        worker.work()

if __name__ == '__main__':
    print("REDIS WORKER STARTED",'*'*200)
    run_worker()
