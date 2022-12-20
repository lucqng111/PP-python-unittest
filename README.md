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

1. Visualize Unittest Result Log
    Imaging your project has being run a long time. Unit Test module is written with thoudsand lines code. We have to track the result, the performance of service function and save the logger to db like `Redis`. Write function execute every single time or write decorator then add to every function. Both of them are very messy and hard to maintain. So i suggest a solution that solves these problems
    
    How to customize ?
    Step 1 : Create Class `CustomTextTestResult` that inherit from `TextTestResult`
        
        Declare redis_client or redis_buffer as the temporarily memory
        Start counting time at `startTest` function
        Compute and save to redis_buffer at `stopTestRun` function

    Step 2 : Custom TestCase by `CustomTestCase` class
    Step 3 : Apply `CustomTextTestResult` to `CustomTextTestRunner`

    This is the result :D 

2. Create new assert
    Default assert in python is fine, but create new and use it is great.
    How to do ?
    Step 1 : In custom TestCase class , add assert function
    Step 2 : At unit test function , call it.
    Here is the result :D 
