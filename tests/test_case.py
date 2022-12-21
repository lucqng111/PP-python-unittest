from core.case import CustomTestCase
import time

class SimpleTestCase(CustomTestCase):
    
    def setUp(self) -> None:
        return super().setUp()
    
    def test_func(self):
        """Test 1
        Args:
            test (_type_): _description_

        Returns:
            _type_: _description_
        """
        time.sleep(1)
        self.assertTrue(True)

    def test_func_2(self):
        """Test 2

        Args:
            test (_type_): _description_

        Returns:
            _type_: _description_
        """
        time.sleep(2)
        self.assertTrue(True)
        
    def test_new_assert(self):
        hello_world = "Hello World"
        self.assertString("Hello World", hello_world)
        
    def test_new_assert_2(self):
        hello_world = "Hello World~~"
        self.assertString("Hello World", hello_world)
