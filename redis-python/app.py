import redis

cache = redis.Redis(host='localhost', port=6379)

try :
  # cache.set(name='user', value='Agni')
  user = cache.get(name='user')
  print(user)

except redis.exceptions.ConnectionError as e:
  print('Connection Error')


