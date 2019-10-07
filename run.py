#!/usr/bin/env python3.6
from user import User
from user import Credentials

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
    print("Regiser")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

            short_code = input().lowe()

            if short_code == 'cc'
                    print("Register")

                    print (Username.....)
                    username = input()

                    print(Password....)
                    password = input()


                    save_contacts(create_credentials(Credentials,password)) # create and save new credential.
                            print ('\n')
                            print(f"New Credentials {credentials} {password} created")
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
        
