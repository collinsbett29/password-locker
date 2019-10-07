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