
def ui_initialmenu():
    print("")
    print("Please choose an option to continue:")
    print("A. Create a new account")
    print("B. Join an existing account")
    print("C. Quit")
    print("")
    return input("Type in your choice: ")
    
def ui_createaccount():
    print("")
    print("Don`t be shy! Create a new account here. Just don`t forget your username!")
    
def ui_joinexistingaccount():
    print("")
    print("Welcome back! I`ve missed you...")

def ui_accountmanagement():
    print("")
    print("A. Account details")
    print("B. Friends")
    print("C. Logout")
    print("D. Quit")
    print("")

def ui_accountmanagement_editaccountdetails():
    print("________________________________________________________")
    print("")
    print("Don`t worry! You can always change your data:")
    print("")
    print("A. Add a name")
    print("B. Add an age")
    print("C. Add a bio")
    print("D. See your current information")
    print("E. DANGEROUS: Delete all your account information")
    print("F. Go to main menu")
    print("")

def ui_accountmanagement_editfriend():
    print("________________________________________________________")
    print("")
    print("Don`t forget to get in touch with all your friends!")
    print("")
    print("A. View all of your friends")
    print("B. Add a friend")
    print("C. Remove a friend (Please pay attention while typing his name: we don`t want \n to remove anyone else, right?)")
    print("D. Messages")
    print("E. Go to main menu")
    print("")

def ui_messages():
    print("________________________________________________________")
    print("")
    print("Ready to catch up with your friends?")
    print("")
    print("A. View all of your friends")
    print("B. Write a new message")
    print("C. View your received messages")
    print("D. Go to main menu")
    print("")
