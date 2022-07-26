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