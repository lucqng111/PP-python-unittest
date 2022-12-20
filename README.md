# Unittest in Python
[![standard-readme compliant](https://img.shields.io/badge/lucqng111-python3.8-brightgreen.svg?style=flat-square)](https://github.com/lucqng111/python_unittest_advanced/)

# Introduction
This topic is mentioning about module unittest in python. However, I want to go deeply about it, understand how it works and how can we adjust and improve unittest. Some developers are using them without understanding mechanism, they thought python which owns magic as current reality. As the result, when project is scaling up, a big amount of function will be added to unittest, it's called "Problem is coming" and don't let your boss know that. :D
So, I wrote this topic to clarify unittest and hopefully it can help everyone who need. Also, this is my first topic.
# Diagrams

# Component
- `TestProgram`     :   The root of unittest in Python is located at `TestProgram` class. It initializes argurments that request send to.
- `TestSuite`       :   This is a collection of `TestCase` or `TestSuite`
- `TestLoader`      :   This class is belong to `TestProgram` class, its mission scan all `TestCase`(s) class in project or any module with specified pattern (by name, test_*, etc)
- `TestCase`        :   Simply, it is individual unit of testing.
- `TestTextRunner`  :   The coordinator where exec test and provide the result     
- `TestResult`      :   The object contains information of execution of `TestCase`s

# Customization and Application
## Visualize Unittest Result Log

    Imaging your project has being run a long time. Unit Test module is written with thoudsand lines code. We have to track the result, the performance of service function and save the logger to db like `Redis`. Write function execute every single time or write decorator then add to every function. Both of them are very messy and hard to maintain. So i suggest a solution that solves these problems
    
### How to customize ?

1. Create Class `CustomTextTestResult` that inherit from `TextTestResult`
    ```python
        class CustomTextTestResult(TextTestResult):
    ```
    Declare redis_client or redis_buffer as the temporarily memory
    ```python
        redis_client = RedisClient()
        redis_buffer  = {}
    ```
    Start counting time at `startTest` function
    ```python
        def startTest(self, test):
            test.start_time = time.time()
            return super().startTest(test)
    ```
    Compute and save to redis_buffer at `stopTestRun` function
    ```python
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
    ```

2. Custom TestCase by `CustomTestCase` class
    ```python
        class CustomTestCase(TestCase):
            start_time = 0

            def doCleanups(self):
                outcome = self._outcome
                result = outcome.result
                redis_buffer = result.redis_buffer
                redis_buffer[self._testMethodName] = {
                    "status": outcome.success,
                    "runtime": time.time() - self.start_time
                }
                self.start_time = 0
                return super().doCleanups()
    ```
    
3. Apply `CustomTextTestResult` to `CustomTextTestRunner`
    ```python
        class CustomTextTestRunner(TextTestRunner):
            resultclass = CustomTextTestResult
    ```
4. Add serveral unit tests
    ```python
        def test_func(self):
            time.sleep(1)
            self.assertTrue(True)

        def test_func_2(self):
            time.sleep(2)
            self.assertTrue(True)
    ```

5. Run code

    ``` $
        Test case with func   : test_func 
        Status                : True
        Runtime               : 1.0052433013916016
                            
        -----------

        Test case with func   : test_func_2 
        Status                : True
        Runtime               : 2.0030300617218018
                            
        -----------
    ```


## Create new assert

    Default assert in python is fine, but create new and use it is great.
    
### How to do ?
    
1. Step 1 : In custom TestCase class , add assert function
    
2. Step 2 : At unit test function , call it.
    
    Here is the result :D 
