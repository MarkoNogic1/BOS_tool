import unittest
from Main import getUserName

class MyTest (unittest.TestCase):
    def testing(self):
        self.assertTrue(getUserName("10227168"))