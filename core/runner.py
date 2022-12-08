from unittest import TextTestRunner
from core.result import CustomTextTestResult

class CustomTextTestRunner(TextTestRunner):
    resultclass = CustomTextTestResult
