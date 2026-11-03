import encrypt_data
import os
def create_account(encrypt_verson):
    if os.path.exists("importing_files/Account.env"):
        print("An account already exists. Please log in.")
        return
    print("Creating a new account...")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    confirmation = input("Confirm your password: ")
    if password != confirmation:
        print("Passwords do not match. Account creation failed.")
        return
    else: 
        encrypt_data.add_account(username, password, encrypt_verson)
        print("Account created successfully.")
