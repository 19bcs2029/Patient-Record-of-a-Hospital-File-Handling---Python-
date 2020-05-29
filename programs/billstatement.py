from datetime import datetime
from registration import (register,diseases)

def viewBill():
    global sum
    ids = input("\nEnter PID of the patient to view Bill-Breakup: ")
    try:
        file = open("../data/"+str(ids)+".txt",'r')
        List = file.readlines() 
        print("****************************************************************************************************************\n")
        print("\n\t\t\t\tBILL-BREAKUP FOR THE PATIENT WITH PID -",ids,"\n")
        if List[14].rstrip("\n")== '1':
            print("The patient is admitted in the hospital since",List[18])
            i=19
            now = datetime.now()
            day = now.strftime("%d")
            month = now.strftime("%m")
            year = now.strftime("%Y")
            a = datetime(int(year),int(month),int(day),0,0,0)
            b = datetime(int(List[15]),int(List[16]),int(List[17]),0,0,0)
            c = a-b
            bedCharges=int(str(c).split()[0])*300
        else:
            print("The patient is not admitted in the hospital")
            bedCharges = 0
            i=16

        print("\nConsultation / Treatment Charges: Rs.",diseases[List[13].rstrip("\n")][2])
        print("\nBed Charges for the patient: Rs.",bedCharges)
        print("\n\tDate and Time\t\t\tItem/Service name\t\tCost (Rs.)\n")
        sum = 0
        
        while(i<len(List)):
            print(List[i].split(" ")[0],List[i].split(" ")[1],"\t\t",List[i].split(" ")[2],"\t\t\t",List[i].split(" ")[3].rstrip())
            sum = sum + int(List[i].split(" ")[3].rstrip("\n"))
            i+=1
        sum = sum + diseases[List[13].rstrip("\n")][2] + bedCharges
        print("\n\n Total Amount: Rs.",sum)
        print("\n****************************************************************************************************************\n")
        file.close()
    except:
        print("\nNo patient with entered PID registered!!!")