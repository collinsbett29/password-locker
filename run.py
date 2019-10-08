#!/usr/bin/env python3.6
from user import User
from user import Credentials

def generate_temp_password(length):
    if not isinstance(length, int) or length < 8:
        raise ValueError("temp password must have positive length")

    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    from os import urandom
    return "".join(chars[ord(c) % len(chars)] for c in urandom(length))

def register_account(user_name,password):
    '''
    Function allow user create an account
    '''
    new_user = Credentials(user_name,password)
    return new_user

def Login(Username,password):
    '''
    Function to allow user login
    '''
    new_credential = Credentials(Credentials,password)
    return new_credential

def create_credentials(credential,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(credential,password)
    return new_credential   

def display_credentials():
    '''
    Function that diplays credentials
    '''
    return Credentials.display_credentials()    

def save_credentials(credentials,password):
    '''
    Function to store credentials
    '''
    new_credential = Credentials(credential,password)
    return new_credential   

    Credentials.save_credentials() 

def del_credentials(Credentials):
    '''
    Function that returns all the stored credentials
    '''
    return Credentials.display_credentials()  

def main():
        """
        main function
        """
        my_id=0
        entries = []
        print("\n")
        print("Register")
        print("-",*40)
while True:
        print("Enter:\n R to Register\n Lg to login\n cc to create credential\n dc to display credentials\n fc to find a credential\n ex to exit the credential list ")

        short_code = input().lower().strip()

        if short_code == 'R':
                print("Register to continue:"+"\n"+"-"+"\nUsername")
                user_name = input("Your username:")
                print("Password:")
                my_password = input("Password: ")

                print("\n")
                create_user(new_account(user_name,user_password,))
                print(f"{user_name} your account has been created successfuly.\nLogin to continue")
                entries.append(0)
                print("-",*30)


        if short_code == 'cc':
                print("New credential")

                print (credential)
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
                        print('-' *20)

                        print(f"username.......{search_credentials}")
                else:
                        print("That credential does not exist")

        elif short_code == "ex":
                print("Bye")
                break
        else:
                print("I really didn't get that. Please use the short codes")

