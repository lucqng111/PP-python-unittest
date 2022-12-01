import unittest
from unittest import TestCase, TextTestResult, TextTestRunner, TestProgram, defaultTestLoader
from redis_client import RedisClient


class SimpleTestCase(TestCase):
    def test_func(self):
        self.assertTrue(True)

    def test_func_2(self):
        self.assertTrue(True)


class CustomTextTestResult(TextTestResult):    
    redis_client = RedisClient()
    redis_buffer  = {}
    
    
    def startTest(self, test):
        """
            Initial function run and add 
        """
        print(123)
        return super().startTest(test)

class CustomTextTestRunner(TextTestRunner):
    resultclass = CustomTextTestResult
    
    
unittest = TestProgram(
    testRunner=CustomTextTestRunner
)     


unittest.main(sys.*args())