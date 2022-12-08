from unittest import TestProgram
from core.runner import CustomTextTestRunner
from tests import *

unittest_program = TestProgram(
    testRunner=CustomTextTestRunner
)