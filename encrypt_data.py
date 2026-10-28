import os
import random
import subprocess
from cryptography.fernet import Fernet
import base64
import cryptography.hazmat.primitives.kdf.pbkdf2
import cryptography.hazmat.backends
import cryptography.hazmat.primitives.hashes
import decode




def encrypt_data(master_key):
    saved_lines = []
    with open("importing_files/Server_keys.env", "r") as f:
        for line in f:
            new_value = master_key.encrypt(line.encode("ascii"))
            saved_lines.append(new_value)
    with open("importing_files/Server_keys.env", "w") as f:
        for line in saved_lines:
            f.write(line.decode("ascii") + "\n")


def create_the_keys(Master_key):
    clean_list = []
    #sending request to the PHP server to get the encryption keys
    php_server = subprocess.run(["php", "../somthing\\server_side\\encrypts.php"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #decoding the server response and splitting it into lines
    the_server_value = php_server.stdout.decode().splitlines()
    #an for loop
    for Key in the_server_value:
        #removing unwanted characters from the server response
        remove_value = str.maketrans("", "", "[]\"")
        #splitting the cleaned line into individual items
        split_items = Key.translate(remove_value).split(",")
        for item in split_items:
            #printing each individual item
            clean_list.append(item)
    #creating a file called "Server_keys.env" and writing the cleaned items into it
    with open("importing_files/Server_keys.env", "w") as f:
        v = 0 
        for item in clean_list:
            f.write(f"Key_{v}=" + item + "\n")
            v += 1
    encrypt_data(Master_key)

def master_key(Master_key):

    master_key = cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC(
        algorithm=cryptography.hazmat.primitives.hashes.SHA256(),
        length=32,
        salt=b"" + Master_key.encode("ascii"),
        iterations=100000,
        backend=cryptography.hazmat.backends.default_backend()
    ).derive(Master_key.encode("ascii"))
    correct_master_key = Fernet(base64.urlsafe_b64encode(master_key))
    if not os.path.exists("importing_files/Server_keys.env"):
        create_the_keys(correct_master_key  )
        

    return correct_master_key

def get_random_decrypted_key(master_keys):


    # getting the master key for decrypting and encrypting 

    #sending the master key and the server keys to the decode function to get the decrypted keys

    decrypted_Keys = decode.decrypt_data(master_keys)

    split_items = random.choice(decrypted_Keys).split(b",")

    removemore = split_items[0].decode("ascii").split("=")

    return removemore


def Create_encprty ( encrypt_verson, get_this_key, removemore):

    if get_this_key == "ramdom_key":
       removemore = get_random_decrypted_key(encrypt_verson)
 

    
    if get_this_key == "ramdom_key":
        key_name = removemore[0]
        key_value = removemore[1]
    else: 
        key_value = removemore

    encrypt_data = cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC(
        algorithm=cryptography.hazmat.primitives.hashes.SHA256(),
        length=32,
        salt=f"f{key_value}".encode("ascii"),
        iterations=100000,
        backend=cryptography.hazmat.backends.default_backend()
    ).derive(key_value.encode("ascii"))
    encrypt_data = Fernet(base64.urlsafe_b64encode(encrypt_data))
    

    if get_this_key == "ramdom_key":
        return encrypt_data, key_name, key_value
    else:
        return encrypt_data, None, key_value
    return encrypt_data, key_name, key_value

def add_account(user, password, encrypt_version):
    encrypt_data, key_name, key_value = Create_encprty(encrypt_version, "ramdom_key", None)
    with open("importing_files/Account.env", "w") as f:
        user = encrypt_data.encrypt(user.encode('ascii')) 
        password = encrypt_data.encrypt(password.encode('ascii'))

        f.write(f"{str(user)}\n")
        f.write(f"{str(password)}\n")
        f.write(f"{key_name}\n")
    import start
    start.login()

def encprty_file(File, MasterPassword):
    print("ENCPRTYING THE FILE(NO RETURN)")
    