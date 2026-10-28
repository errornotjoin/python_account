import getting_the_file
def show_dashboard(Username, master_key):
    print(f"Welcome to the dashboard, {Username}!") 
    list_of_items = ["Text", "cheack list", "run commands", "sign out"]
    for list_item in list_of_items:
        print(f"- {list_item}")
    user_choice = input("Please select an option: ")
    if user_choice.lower() == "sign out":
        print("Signing out...")
        return
    if user_choice.lower() == "look":

        getting_the_file.getting_the_files(Username, master_key)
    else:
        print(f"You selected: {user_choice}")
        show_dashboard(Username, master_key)
