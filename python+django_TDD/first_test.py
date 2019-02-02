import unittest

def sum_two(a, b):
    return a + b

class MainTest(unittest.TestCase):

    def test_hello(self):
        print("Hello from the tests")
    
    def test_sum_two(self):
        print("Test 2 is working")