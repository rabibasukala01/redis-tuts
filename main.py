import redis
HOST = 'localhost'
PORT = 6379

def redis_connection():
    try:
        return redis.StrictRedis(host=HOST, port=PORT, decode_responses=True)
    except Exception as e:
        print(e)
        return None
    

def redis_set(r,key, value):
    return r.set(key, value)

def redis_get(r,key):
    return r.get(key)

def redis_del(r,key):
    return r.delete(key)

def redis_keys(r):
    return r.keys()

def redis_flush(r):
    return r.flushall()

def redis_set_expire(r,key, time,value):
    return r.setex(key, time,value)

# and so on....

r = redis_connection()
if r:
    print(redis_set_expire(r,'hydrogen', 10, '1'))

else:
    print('Redis connection failed')