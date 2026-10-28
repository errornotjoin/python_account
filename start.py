import cryptography 
import random 
import requests 
import subprocess
import json
import sys
import getpass

import decode
import encrypt_data
import create_account
import os

##print("Request sent to server.")
##
##print(tste.stdout)

    
def login():

    Master_key = getpass.getpass("Enter your Main Password: ")
    encrypt_verson = encrypt_data.master_key(Master_key)

    if os.path.exists("importing_files/Account.env"):
        print(os.path.exists("importing_files/Account.env"))
        open("importing_files/Account.env", "r")
        file_keys = "importing_files/Account.env"

        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        if(username == "" or password == ""):
            print("Username or password cannot be empty.")
            login()
        else:
            {
                
                decode.decrypt_the_account(username, password,file_keys, encrypt_verson )
            }
    else:
        print("There Are NO Accounts .")
        print("Creating a new account...")
        create_account.create_account(encrypt_verson)
        return

#def Cheacking():
#    Sign = "Can You See This? Can You hear ME?"
#    sys.stdout.write(Sign)
#    sys.stdout.flush()
#
#    look_out = sys.stdin.readlines()
#    if look_out:
#        print(look_out)
#    else:
#        login()
if __name__ == '__main__':
    login()