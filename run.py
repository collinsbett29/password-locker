#!/usr/bin/env python3.6
from user import User
from user import Credentials

def generate_temp_password(length):
    if not isinstance(length, int) or length < 8:
        raise ValueError("temp password must have positive length")

    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    from os import urandom
    return "".join(chars[ord(c) % len(chars)] for c in urandom(length))

def create_credentials(Credentials,password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(Credentials,password)
    return new_credentials

def store_credentials(redentials):
    '''
    Function to store credentials
    '''
    Credentials.store_credentials() 

def del_credentials(Credentials):
    '''
    Function to delete a credential
    '''
    Credentials.delete_credentials() 

def display_credentials():
    '''
    Function that returns all the stored credentials
    '''
    return Credentials.display_credentials()  

def main():
    print("Register")
    print('\n')

    print("username")
    username = input()

    print("password")
    password = input()



    while True:
            print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("Login")

                    print (Username)
                    username = input()

                    print(Password)
                    password = input()


                    save_credentials(create_credentials(Credentials,password)) # create and save new credential.
                    print ('\n')
                    print(f"New Credential created")
                    print ('\n')

                    elif short_code == 'dc':
                            if display_credentials():
                                    print("Here are all your credentials")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{credentials.credentials} {credentials.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("Your credentials list is empty")
                                    print('\n')


                    elif short_code == 'fc':

                            print("Search the credential")

                            search_credentials = input()
                            if check_existing_credentials(search_credentials):
                                    search_credentials = find_credentials(search_credentials)
                                    print(f"{search_credentials.username}")
                                    print('-' * 20)

                                    print(f"username.......{search_credentials}")
                            else:
                                    print("That credential does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
        
