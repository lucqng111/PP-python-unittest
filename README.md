# Unittest in Python
[![standard-readme compliant](https://img.shields.io/badge/lucqng111-python3.8-brightgreen.svg?style=flat-square)](https://github.com/lucqng111/python_unittest_advanced/)

# Introduction

# Component
- `TestProgram`     :   The root of unittest in Python is located at `TestProgram` class. It initializes argurments that request send to.
- `TestLoader`      :   This class is belong to `TestProgram` class, its mission scan all `TestCase`(s) class in project or any module with specified pattern (by name, test_*, etc)
- `TestCase`        :   Simply, it is individual unit of testing.
- `TestTextRunner`  :   The coordinator where exec test and provide the result     
- `TestResult`      :   The object contains information of execution of `TestCase`s
- `TestSuite`       :   This is a collection of `TestCase` or `TestSuite`

# Customization and Application
