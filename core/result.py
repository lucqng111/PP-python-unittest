from unittest import TextTestResult
from redis_client import RedisClient
import time


class CustomTextTestResult(TextTestResult):    
    redis_client = RedisClient()
    redis_buffer  = {}
    
    
    def startTest(self, test):
        test.start_time = time.time()
        return super().startTest(test)
    
    def stopTestRun(self):
        print("\n")
        for k, v in self.redis_buffer.items():
            msg = f"""
Test case with func   : {k} 
Status                : {v["status"]}
Runtime               : {v["runtime"]}
                    """
            print(msg)
            print("-----------")
        
        return super().stopTestRun()
