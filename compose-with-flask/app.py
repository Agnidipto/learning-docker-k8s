from flask import Flask
import redis
import time

app = Flask(__name__)   
cache = redis.Redis(host='redis', port = 6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello_world():
    count = get_hit_count()
    return 'Hello, World! You have visited page '+str(count)+' times.'

if __name__ == '__main__':
    count = 0
    app.run(debug=True)