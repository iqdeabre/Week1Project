import ui_iqanetwork

def teste():
    print("Testando1")

if __name__ == "__main__":
    
    print("________________________________________________________")
    print("")
    print("            Welcome to the IQA's social media!")
    print("")
    
    decision1 = ui_iqanetwork.ui_initialmenu()

    while True:
    
        if decision1 == "a.":
            print("Working")
            teste()

        elif decision1 == "b.":
            print("Working 2")
        
        elif decision1 == "c.":
            break

        else:
            print("Please insert a valid input!")

        decision1 = ui_iqanetwork.ui_initialmenu()