import datetime

def add(x):
    print("\nAdd an item/service !!!")
    file = open("../data/"+str(x)+".txt",'a+')
    item = input("\nEnter item / service name: ")
    cost = input("Enter the cost of the item / service: Rs.")
    print("\n=================================================================================================================\n")
    date = datetime.datetime.now()
    file.write("\n"+str(date) +" "+ item +" "+ cost)
    file.close()


def addons():
    global pid
    print("\n\n=================================================================================================================")
    print("\t\t\t\t\t\tADD-ONS TO THE BILL\t\t\t\t")
    print("=================================================================================================================\n")
    pid = input("Enter patient's id (PID): ")
    try:
        f = open("../data/"+str(pid)+".txt",'r')
        f.close()
        while(1):
            print("1. Add an item / service\n2. Back")
            n = int(input("Select an option to perform: "))
            switch = {1:add,2:exit}
            switch.get(n)(pid)  
    except:
        print("\nNo patient with entered PID registered!!!")