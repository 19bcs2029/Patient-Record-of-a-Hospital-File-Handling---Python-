from registration import register
from view_records import view
from billing import addons,add
from billstatement import viewBill

def start():
    while(1):
        #App starts
        print("=================================================================================================================")
        print("                                      WELCOME TO ABCD HOSPITAL PORTAL                                            ")
        print("=================================================================================================================\n")

        print("\n1. Register a new patient.\n2. View a patient details.\n3. Addons to the bill\n4. View Bill Statement\n5. Exit")
        choice = int(input("Select an option to perform: "))

    #To switch between options
        switcher = {1:register,2:view,3:addons,4:viewBill,5:exit}
        switcher.get(choice)()
start()