import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Collins Bett","##@@collins1")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Collins Bett")
        self.assertEqual(self.new_user.password,"##@@collins1")

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Credentials("instagram") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.username,"James")
        self.assertEqual(self.new_credentials.password,"##@@james1"

if __name__ == '__main__':
    unittest.main()