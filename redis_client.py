from redis import Redis

class RedisClient:
    def __init__(self):
        self._redis = Redis(
            host="127.0.0.1",
            port="6379",
            db="0"
        )
        
    def get_vals(self, key, value):
        pass
    
    def set_vals(self, key, value):
        pass