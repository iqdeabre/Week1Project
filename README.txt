IQA Network

--------------------------------------------------------------------------------------------
Context
--------------------------------------------------------------------------------------------

This archive will cover a major explanation regarding the functionality, the thought process and the main issues 
while developing the network. Also, there will be an easy guide on how to use the system. Enjoy!

--------------------------------------------------------------------------------------------
Modules and their usage
--------------------------------------------------------------------------------------------

The whole system is based on three files: iqanetwork.py, ui_iqanetwork.py and data_iqanetwork. 
Basically, ui_iqanetwork and data_iqanetwork are archives responsible for all the action itself. 
Ui_iqanetwork focuses on all the interaction between code and user, printing all the menus 
and information shown in the terminal. Data_iqanetwork defines all the actions that need to occur 
based on the user responses, calling certain functions inside ui_iqanetwork, integrating menus and submenus, 
and also being able to identify what the system should do in each user response. 
Iqanetwork is able to relate all the files making everything work accordingly.

--------------------------------------------------------------------------------------------
UI_IQANETWORK.PY
--------------------------------------------------------------------------------------------

There are 7 menus. The initial one stores all options regarding log in: the user can create a new account 
and join it or quit the network. After creating a new account and typing in the correct username, the 
three main branches are shown via the functions ui_accountmanagement(). Hence, the user can edit their 
account details, manage their friends or just quit the system. Inside each of the first two branches there 
are other UI functions that communicate with the user: ui_accountmanagement_editaccountdetails() and 
ui_accountmanagement_editfriend(). Inside ui_accountmanagement_editfriend() there is also ui_messages(). 

--------------------------------------------------------------------------------------------
UML
--------------------------------------------------------------------------------------------

Objects
(did not really know what to insert here)

Attributes
(did not really know what to insert here)

Function
ui_accountmanagement()
ui_accountmanagement_editaccountdetails()
ui_accountmanagement_editfriend()
ui_createaccount()
ui_joinexistingaccount()
ui_accountmanagement()
ui_messages()

--------------------------------------------------------------------------------------------
IQANETWORL.PY
--------------------------------------------------------------------------------------------

The file starts importing all the code from the other two. Then, the main if statement 
(if __name__ == “__main__”) guarantees that the python interpreter is going to start reading the 
iqanetwork.py file as the main one, inputing information from the other two when needed or requested. 
After the small welcome sign, the first input from the user is converted into a variable that is going 
to be used to access what the program should run depending on each answer. What is curious is that the 
verify_account() function is the one responsible for all the actions, menus and data after the user logs in. 
Because it was too complicated to refer to input variables inside functions which belonged to other files, 
I have decided to make extract inputs as variables inside each class function. As a consequence, 
it was easier to make the code notice when it had to run certain functions depending on each user response.

--------------------------------------------------------------------------------------------
UML
--------------------------------------------------------------------------------------------

Objects
if decision1 == "A":
if decision1 == "B":
if decision1 == "C":
else

Attributes
(did not really know what to insert here)

Functions 
ui_iqanetwork.ui_createaccount()
data_iqanetwork.Network_accounts.create_account()
ui_iqanetwork.ui_joinexistingaccount()      data_iqanetwork.Network_accounts.verify_account()
ui_iqanetwork.ui_initialmenu()

--------------------------------------------------------------------------------------------
DATA_IQANETWORK.PY
--------------------------------------------------------------------------------------------

The file starts by defining different classes and its functions (Account_management, Account_friends, 
Account_messages and Network_accounts). The Account_management class is able to store personal information 
of the user such as name, age and bio inside three lists. Other than storing data, two other functions are able to clear all the user stored information (clear_account_cache()) or just look at what is stored 
(show_info()). 

Account_friends, as the name mentions, contains all the friend-related functions and data. 
Consequently, it relies on three important functions: add_friend(), remove_friend() and show_friends(). 
With straightforward names, these functions modify and/or show the list containing the user's friends, outputting a confirmation that the action was successful.

Account_messages is the class responsible for all the messages sent and received. 
There are three lists which store the recipient name, the sender name and the message itself. 
By using if statements, the code is able to access if the user name (the one inserted in the Account 
Details section) is the same as the recipient name stored into a list called recipient_name. 
In other words, the recipient can only open the message if their name is the same as the one written 
by the sender. Also, the sender is only able to send messages to their friends.

Network_accounts is the main class that makes all the system work. It is basically the skeleton of the network, responsible for identifying which response matches each function. It contains two functions: create_account and verify_account. When an account is created, the username is stored into a list called existing_accounts (there is a predetermined account called “adm” used for testing). After this, the verify_account is able to compare the existing_accounts and the username imputed to see if the user has really created an account. Then, all the submenus and their if statements control whether the code should execute a certain function or not. It may seem really confusing, but since the functions and their lists are all named clearly, the only important thing is to understand what each selected letter means (this is easy by looking at the ui_iqanetwork). There is also a function that is able to return to the beginning of verify_account, which happens to be very useful in order to exit menus (returning_to_main_account_menu).

--------------------------------------------------------------------------------------------
UML
--------------------------------------------------------------------------------------------

Objects
Account_management
Account_friends 
Account_messages
Network_accounts

Attributes
Account_management( age, name, bio, also the lists with the same names)
Account_friends( friends, also the list with the same name)
Account_messages( message, recipent_name, sender_name, also the lists with the same names)
Network_accounts( existing_accounts, also the list with the same name)

Functions 
Account_management(add_age, add_name, add_bio, show_info and clear_account_cache)
Account_friends(add_friend, remove_friend and show_friends)
Account_messages(send_messages and receive_messages)
Network_accounts(create_account, verify_account and returning_to_main_account_menu)

--------------------------------------------------------------------------------------------

Suggestion

--------------------------------------------------------------------------------------------

In order to test the message system, start creating an account and defining a name in Account Details section.
Then, insert a recipient name. Clean your account information and add a new name (one that matches the recipient name inserted previoulsy). Finally, open the received messages section and there should be the message sent!

The system should be very interactive! Try inserting a mistaken name on remove_friend section, for instance! Or maybe seeing your friend list with no friends added... Also, try to send a message to a friend you haven`t added.