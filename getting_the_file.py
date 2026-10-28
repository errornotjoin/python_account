import os

def getting_the_files(Username, master_key):
    user_input = input("Enter the FULL addres of the file:")
    try: 
        if user_input.lower() == "Server_Keys.env" or user_input.lower() == "account.env":
            print("You CAN'T Use that FILE ")
        else:
            with open(user_input, "r") as file:
                dose_user_want_to_read_file = input("DO you want to read the file:")
                if dose_user_want_to_read_file.lower() == "y" or dose_user_want_to_read_file.lower() == "ye" or dose_user_want_to_read_file.lower() == "yes":
                    for line in file: 
                        print(line.replace("\n", " "))
                else:
                    print("Skiping displaying the File")
    
                new_user_input = input("Do You Want to encrpty This file Y/N: ")
    
                if new_user_input.lower() == "y" or new_user_input.lower() == "ye" or new_user_input.lower() == "yes":
                    print("This Will Remove the old File And Replace With encprtyed one\n")
                    print("And IF Server_keys Get CHANGE will make it imposable to decprtyed\n")
                    import encrypt_data       
                else:
                    import dashboard
                    dashboard.show_dashboard(Username, master_key)
    except FileNotFoundError:
        import dashboard
        print("NO FILE FOUND WITH THAT Name")
        print("RETURN TO dashboard")
        dashboard.show_dashboard(Username, master_key)
    except PermissionError:
        import dashboard
        print("This Program Can't read That File Becayse Of Permissions")
        print("RETURN TO dashboard")
        dashboard.show_dashboard(Username, master_key)
    except:
        print("Something went Wrong Plase Try Again")
        print("You have enter:"+ user_input)
    

