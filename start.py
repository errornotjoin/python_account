import os
import getpass

import decode
import encrypt_data
import create_account


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

if __name__ == '__main__':
    login()