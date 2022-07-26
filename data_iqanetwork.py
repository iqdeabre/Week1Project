from inspect import _empty
from re import A
import ui_iqanetwork
import iqanetwork


class Account_management:
    
    age = []
    name = []
    bio = []
    def __init__(self, name, age, biography):
        self.name = name
        self.age = age
        self.biography = biography
        
    def add_age():
        user_age = input("How old are you? ")
        Account_management.age.append(user_age)

    def add_name():
        user_name = input("What is your real name? ")
        Account_management.name.append(user_name)

    def add_bio():
        user_bio = input("What do you want to say about you? ")
        Account_management.bio.append(user_bio)

    def show_info():
        if len(Account_management.age) or len(Account_management.bio) or len(Account_management.name) !=  0:
            print("________________________________________________________")
            print("")
            print("Your name is", Account_management.name,)
            print("Your age is", Account_management.age, "year(s) old")
            print("You want to tell the world that:", Account_management.bio)
        else:
            print("________________________________________________________")
            print("")
            print("You don`t have any information storaged!")

    def clear_account_cache():
        if len(Account_management.age) or len(Account_management.bio) or len(Account_management.name) !=  0:
            Account_management.age.clear()
            Account_management.name.clear()
            Account_management.bio.clear()
            print("________________________________________________________")
            print("")
            print("All your data is now empty!")

        else:
            print("________________________________________________________")
            print("")
            print("You don`t have any information storaged!")

class Account_friends:
    
    friends = []
    def __init__(self, friends):
        self.friends = friends

    def add_friend():
        friend_name = input("What is yout friend`s name? ")
        Account_friends.friends.append(friend_name)

    def remove_friend():
        friend_name_remove = input("Who is that you want to get rid of? ")
        if friend_name_remove in Account_friends.friends:
            Account_friends.friends.remove(friend_name_remove)
            print("________________________________________________________")
            print("")
            print(friend_name_remove, "has been successfully removed!")
        else:
            print("________________________________________________________")
            print("")
            print("Imagine getting rid of the wrong friend! Please check your spelling: you do not have a friend named", friend_name_remove)

    def show_friends():
        if len(Account_friends.friends) == 0:
            print("________________________________________________________")
            print("")
            print("You don`t have any friends. That`s really sad... :(") 
        else:
            print("________________________________________________________")
            print("")
            print("This is a list of all your current friends:", Account_friends.friends)

class Account_messages:
    message = []
    recipient_name = []
    sender_name = []

    def __init__(self, message, recipient_name, sender_name):
        self.message = message
        self.recipient_name = recipient_name
        self.sender_name = sender_name

    def send_messages():
        sender = input("How do you like to be referred to in the message? ")
        recipient_name_sending = input("Who will receive this message? ")
        message_sending = input("Type in the message you would like to send: ")

        if recipient_name_sending not in Account_friends.friends:
            print("________________________________________________________")
            print("")
            print("It`s seems like you don`t have", recipient_name_sending, "as your friend!. Try adding them...")
        else:
            Account_messages.recipient_name.append(recipient_name_sending)
            Account_messages.message.append(message_sending)
            Account_messages.sender_name.append(sender)
            print("________________________________________________________")
            print("")
            print("Your message to", recipient_name_sending, "has been successfully sent!")
    
    def receive_messages():
        if Account_management.name == Account_messages.recipient_name:
            print("________________________________________________________")
            print("")
            print("You receveived the following message from", Account_messages.sender_name)
            print(Account_messages.message)
            print("________________________________________________________")
            print("")
            delete_received_message = input("Would you like to delete this message (Y/N): ")
            if delete_received_message == "Y":
                Account_messages.message.clear()
                Account_messages.recipient_name.clear()
                Account_messages.sender_name.clear()
                print("________________________________________________________")
                print("")
                print("Your messages were successfully deleted!")
            else:
                pass

        else:
            print("________________________________________________________")
            print("")
            print("You don`t have any new messages!")
        

class Network_accounts:
    
    existing_accounts = ["adm"]
    def __init__(self, existing_accounts):
        self.existing_accounts = existing_accounts
       
    def create_account():    
        createacc = input("Type in your username: ")
        Network_accounts.existing_accounts.append(createacc)

    def verify_account():
        joinacc = input("Type in your username: ")
        
        if joinacc in Network_accounts.existing_accounts:
            while True:
                
                def returning_to_main_account_menu():

                    print("________________________________________________________")
                    print("")
                    print("Hello", joinacc, "long time no see!")
                
                    ui_iqanetwork.ui_accountmanagement()
                    decision_main_accountmanagement = input("What can I do for you? ")

                    if decision_main_accountmanagement == "A":
                
                        while True:
                            ui_iqanetwork.ui_accountmanagement_editaccountdetails()
                            decision_account_details = input("What do you want to do? ")
                
                            if decision_account_details == "B":
                                Account_management.add_age()
                                print("________________________________________________________")
                                print("")
                                print("Age successfully added!")
                
                            elif decision_account_details == "A":
                                Account_management.add_name()
                                print("________________________________________________________")
                                print("")
                                print("Name successfully added!")
                
                            elif decision_account_details == "C":
                                Account_management.add_bio()
                                print("________________________________________________________")
                                print("")
                                print("Bio successfully added")                
                        
                            elif decision_account_details == "D":
                                Account_management.show_info()

                            elif decision_account_details == "E":
                                Account_management.clear_account_cache()

                            elif decision_account_details == "F":
                                print("________________________________________________________")
                                print("")
                                print("Going back to the previous menu!")
                                returning_to_main_account_menu()
                    
                            else:
                                print("________________________________________________________")
                                print("")
                                return("Please reconsider your choice! It is invalid...")
                    
                    elif decision_main_accountmanagement == "B":
                        
                        while True:
                            ui_iqanetwork.ui_accountmanagement_editfriend()
                            decision_friendsmanagement = input("What do you want to do? ")
                        
                            if decision_friendsmanagement == "A":
                                Account_friends.show_friends()
                        
                            elif decision_friendsmanagement == "B":
                                Account_friends.add_friend()
                                print("________________________________________________________")
                                print("")
                                print("Friend added successfully!")
                        
                            elif decision_friendsmanagement == "C":
                                Account_friends.remove_friend()
                        
                            elif decision_friendsmanagement == "D":    
                                while True:
                                    print("________________________________________________________")
                                    print("")
                                    ui_iqanetwork.ui_messages()
                                    decision_messages_mainpage = input("What should I do? ")
                                    if decision_messages_mainpage == "A":
                                        Account_friends.show_friends()

                                    elif decision_messages_mainpage == "B":
                                        Account_messages.send_messages()

                                    elif decision_messages_mainpage == "C":
                                        Account_messages.receive_messages()

                                    elif decision_messages_mainpage == "D":
                                        print("________________________________________________________")
                                        print("")
                                        print("Going back to the previous menu!")
                                        returning_to_main_account_menu()

                                    else:
                                        print("________________________________________________________")
                                        print("")
                                        return("Please reconsider your choice! It is invalid...")

                            elif decision_friendsmanagement == "E":
                                print("________________________________________________________")
                                print("")
                                print("Going back to the previous menu!")
                                returning_to_main_account_menu()
                
                            else:
                                return("Please reconsider your choice! It is invalid...")
                            
                    elif decision_main_accountmanagement == "C":
                        print("________________________________________________________")
                        print("")
                        print("See you later", joinacc)
                        print("")
                        print("________________________________________________________")
                        exit()

                    
                returning_to_main_account_menu()
        
        else:
            return ("Invalid username. Please insert a valid input!")
