import cryptography
from cryptography.fernet import Fernet, InvalidToken
import base64
import encrypt_data

import dashboard

def decrypt_data(master_key ):
    file="importing_files/Server_keys.env"
    try:
        new_list = []
        with open(file, "rb") as f:
            for line in f:
                new_list.append(master_key.decrypt(line).strip())
        return new_list
    except InvalidToken as e:
        print(f"Your decryption key is invalid.")
        exit()

def decrypt_the_account(username, password, file, master_key):
    

    key_value = []
    new_data_valye = []
    #this will get the data and key from the file
    data_value, key_value  = finding_the_key_and_data(file, master_key)
    #this find that key decrypted value from the key_value list
    encprtyed_data = getting_key(master_key, key_value)

    #this will create the same evenverment so the key can decrypt the data value
    key, value, encrypt_value =  encrypt_data.Create_encprty(master_key, "nothing", encprtyed_data[1])

    for x in range(len(data_value)):
        new_data_valye.append(key.decrypt(data_value[x]).strip().decode("utf-8"))

    if username == new_data_valye[0] and password == new_data_valye[1]:
        dashboard.show_dashboard(username, master_key)
    else:
        print("There Is No Account With That Username/Password")
        import start
        start.login()

def finding_the_key_and_data(file, master_key):
    Data_value = []
    key_value = []
    with open(file, "rb") as f:
            for line in f:
                if line.startswith(b"Key_"):
                    key_value.append(line)
                else:
                    Data_value.append(line.strip().replace(b"b'", b"").replace(b"'", b""))
    return Data_value, key_value

def getting_key(master_key, key_name):
      key_value = []
      decrypted_lines = decrypt_data(master_key)
      for line in decrypted_lines:
            if line.startswith(key_name[0].strip() + b"="):
                for part in line.decode("ascii").strip().split("="):
                    key_value.append(part)
      return  key_value 



