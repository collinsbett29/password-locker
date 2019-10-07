class User:
    """
    Class that generates new instances of the user.
    """

    user_list = []

    def __init__(self,username,password):
      """
      Helps define properties the objects.
      """
      self.username = username
      self.password = password

class Credentials:
    """
    class that generates new instances of the credentials
    """
    credentials_list = []

    def __init__(self,credentials,password):
      """
      Helps define properties the objects.
      """
      self.credentials = credentials
      self.password = password

    def store_credentials(self):

      '''
      store_credentials method stores credentials objects into credentials_list
      '''

      Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a credential that is no longer needed from the contact_list
        '''

        Credentials.credentials_list.remove(self)      

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list      












































# class User:
#     """
#     Class that generates new instances of the user.
#     """

#     user_list = []

#     def __init__(self,passwordlocker_details,username,password)):
#       """
#       Helps define properties the objects.
#       """
#         self.passwordlocker_details = details
#         self.username = username
#         self.user password = password
