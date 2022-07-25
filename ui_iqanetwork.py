
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
    print("A. Edit account details")
    print("B. Edit friends")
    print("C. Quit")
    print("")

def ui_accountmanagement_editaccountdetails():
    print("________________________________________________________")
    print("")
    print("Don`t worry! You can always change your data:")
    print("")
    print("A. Add age")
    print("B. Add name")
    print("C. Add a bio")
    print("D. See your current information")
    print("E. DANGEROUS: Delete all your account information")
    print("F. One menu back")
    print("")

def ui_accountmanagement_editfriend():
    print("________________________________________________________")
    print("")
    print("Don`t forget to get in touch with all your friends!")
    print("")
    print("A. View all friends")
    print("B. Add friend")
    print("C. Remove friend (Please pay attention while typing his name: we don`t want \n to remove anyone else, right?")
    print("D. Send messages to friend")
    print("E. One menu back")
    print("")

