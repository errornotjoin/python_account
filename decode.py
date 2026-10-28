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

    data_value, key_value  = finding_the_key_and_data(file, master_key)

    encprtyed_data = getting_key(master_key, key_value)
    print(encprtyed_data)
    encrypt_value =  encrypt_data.Create_encprty(master_key, "nothing", encprtyed_data[0])
   # keys = getting_key(correct_master_key,  )
     #for x in range(len(account_info)):
     #    account_real.append(encrypt_value[0].decrypt(account_info[x]).strip())
#
     #if username == str(account_real[0], "utf-8") and password == str(account_real[1], "utf-8"):
     #    dashboard.show_dashboard(username, master_key)
     #else:
     #    print("There Is No Account With That Username/Password")
     #    import start
     #    start.login()

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



#decrypt_the_account("username", "password", "importing_files/Account.env", "Maxandbenjo12")