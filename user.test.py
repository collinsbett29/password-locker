import unittest
from user import User
from user import Credentials
import pyperclip

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
        self.new_credentials = Credentials("instagram","##@@collins1") # creating credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials,"instagram")
        self.assertEqual(self.new_credentials.password,"##@@collins1")

    def test_store_credentials(self):
        '''
        test_store_credentials test case to test if the credentials object is stored into
         the credentials list
        '''
        self.new_credentials.store_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_display_all_credentials(self):
            '''
            method that returns a list of all contacts saved
            '''

            self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list) 

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential tat is not in from the credentials list
            '''
            self.new_credentials.store_credentials()
            test_credentials = Credentials("instagram","##@@collins1") # new credential
            test_credentials.store_credentials()

            self.new_credentials.delete_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_copy_credentials(self):
        '''
        Test to confirm that we are copying the credentials to the clipboard
        '''

        self.new_credentials.store_contact()
        Credentials.test_copy_credentials("instagram")

        self.assertEqual(self.new_credentials.credentials,pyperclip.paste())            

if __name__ ==  '__main__':
    unittest.main()        