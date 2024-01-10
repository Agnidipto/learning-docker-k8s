import redis
from flask import Flask, request, jsonify

cache = redis.Redis(host='rdb', port=6379)
app = Flask(__name__)

decoder = lambda x : x.decode("utf-8") if x!=None else ''

# Route for handling GET requests
@app.route('/', methods=['GET'])
def get_request():
    try:
      user = decoder(cache.get(name='user'))
      return jsonify({'user' : user})
    except redis.exceptions.ConnectionError as e :
      return jsonify({'error' : 'Error connecting to Redis server.'})

# Route for handling POST requests
@app.route('/', methods=['POST'])
def post_request():
    try:
        # Get JSON data from the request
        data = request.json

        # Check if 'data' key exists in JSON
        if 'user' in data:
            cache.set(name = 'user', value=data['user'])
            return jsonify({'message': 'Successful'})
        else:
            return jsonify({'error': 'No "data" key found in JSON'})
    except redis.exceptions.ConnectionError as e :
       return jsonify({'error' : 'Error connecting to Redis server.'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)