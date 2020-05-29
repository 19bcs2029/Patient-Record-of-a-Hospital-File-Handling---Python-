from registration import diseases
from datetime import datetime
global pid
global p_diseaseCode

#Option 2 to view patient records  
def view():
    print("\n\n=================================================================================================================")
    print("\t\t\t\tVIEW A PATIENT'S RECORD\t\t\t\t")
    print("=================================================================================================================\n")
    ids = input("Enter ID of patient: ")
    try:       
        file = open("../data/"+str(ids) + ".txt", 'r')   
        List = file.readlines()                     #readlines read line by line as list
        
        print("\n******************************************************************************************************************\n")
        print("Patient Id (PID):",ids)
        print("Name: ",List[0].rstrip())
        print("Age: ",List[1].rstrip())
        print("Gender: ",List[2].rstrip())
        print("Contact: ",List[3].rstrip())
        print("Address: ",List[4].rstrip())
        
        print("\nFather's Name: ",List[5].rstrip())
        print("Father's Age: ",List[6].rstrip())
        print("Father's Contact Number: ",List[7].rstrip())
        print("Father's Address: ",List[8].rstrip())

        print("\nMother's Name: ",List[9].rstrip())
        print("Mother's Age: ",List[10].rstrip())
        print("Mother's Contact Number: ",List[11].rstrip())
        print("Mother's Address: ",List[12].rstrip())

        print("\nDisease: ",diseases[List[13].rstrip("\n")][0])
        print("Minimum Resting Period: ",diseases[List[13].rstrip("\n")][1],"days")
        if List[14].rstrip("\n") == "1":
            print("Admission Status: Admitted")
            print("Admission Date & Time: ",List[18])
        else:
            print("Admission Status: Not Admitted")
        file.close()
        bill(ids)
        print("\n******************************************************************************************************************\n")

    except:
        print("No patient with the entered id found!!!") 
        print("\n******************************************************************************************************************\n")   

        
def bill(x):
    file = open("../data/"+str(x) + ".txt", 'r')   
    List = file.readlines()  
    if List[14].rstrip("\n")== '1':
        i = 19
        now = datetime.now()
        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%Y")
        a = datetime(int(year),int(month),int(day),0,0,0)
        b = datetime(int(List[15]),int(List[16]),int(List[17]),0,0,0)
        c = a-b
        bedCharges=int(str(c).split()[0])*300
    else: 
        bedCharges = 0
        i = 16

    sum = 0
    
    while(i<len(List)):
        sum = sum + int(List[i].split(" ")[3].rstrip("\n"))
        i+=1
    sum = sum + diseases[List[13].rstrip("\n")][2] + bedCharges

    print("\n Total Bill: Rs.",sum)
    file.close()
        
  