from unittest import TestCase
import time
from unittest.util import safe_repr

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

    def assertString(self, expected_string, string, msg=None):
        """Check that the expression is true."""
        if expected_string != string:
            msg = self._formatMessage(msg, f"{safe_repr(string)} is not same with {expected_string}" )
            raise self.failureException(msg)
