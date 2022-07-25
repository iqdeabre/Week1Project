#V1
import ui_iqanetwork
import data_iqanetwork

if __name__ == "__main__":
    
    print("________________________________________________________")
    print("")
    print("            Welcome to the IQA's social media!")
    print("")
    print("________________________________________________________")
    
    decision1 = ui_iqanetwork.ui_initialmenu()
    
    while True:
        if decision1 == "A":
            ui_iqanetwork.ui_createaccount()
            data_iqanetwork.Network_accounts.create_account()

        elif decision1 == "B":
                ui_iqanetwork.ui_joinexistingaccount()
                data_iqanetwork.Network_accounts.verify_account()

                
        elif decision1 == "C":
            print("________________________________________________________")
            print("")
            print("You leaving too soon... Consider visiting again! ;)")
            print("")
            print("________________________________________________________")
            break

        else:
            print("________________________________________________________")
            print("")
            print("Please insert a valid input!")

        decision1 = ui_iqanetwork.ui_initialmenu()