from datetime import datetime
import os
global pid
global p_diseaseCode

#Dictionary for list of diseases with disease name, rest-period, cost of treatment, admission required/not(1/0)
diseases = {
            "1":["Fever",3,200,0],
            "2":["Cough and Cold",7,250,0],
            "3":["Jaundice",30,5000,1],
            "4":["Heart Stroke",15,5000,1]
} 
#Register new patient
def register():
    global admissionRequired
    global admissionDate
    global admissionStatus
    #To maintain last registered patient id in pidcount.txt
    pfile=open("..\pidcount",'r')
    pid = int(pfile.read())
    pfile.close()

    pid = pid+1
    print("\n\n=================================================================================================================")
    print("\t\t\t\tNEW PATIENT REGISTRATION PORTAL\t\t\t\t")
    print("=================================================================================================================\n")
    file = open("../data/"+str(pid)+".txt", 'w')       #Creates/opens a filename as patient id containing patient record
    p_name=input("Enter name: ")              
    p_age=input("Enter age: ")
    p_gender=input("Enter gender: ")
    p_contact=input("Enter contact number: ")
    p_addr=input("Enter address: ")

    f_name=input("\nEnter father's Name: ")
    f_age = input("Enter father's age: ")
    f_contact = input("Enter father's contact number: ")
    f_addr = input("Enter father's address: ")

    m_name=input("\nEnter mother's Name: ")
    m_age = input("Enter mother's age: ")
    m_contact = input("Enter mother's contact number: ")
    m_addr = input("Enter mother's address: ")

    #Prints list of diseases 
    print("\nSelect the disease from below list.")
    for key,value in diseases.items():
        print(key,diseases[key][0])
    p_diseaseCode = input("Enter the disease number from the list: ")           #Input disease code
    if diseases[p_diseaseCode][3] == 1:
        admissionRequired=input("Admission Recommended! Does the patient have consent to get admitted today? (y/n): ")
        if admissionRequired == 'y':
            now = datetime.now()
            admDay = now.strftime("%d")
            admMonth = now.strftime("%m")
            admYear = now.strftime("%Y")
            admDate = datetime.now()
            admissionStatus = '1'
        elif admissionRequired == 'n':
            admissionStatus = '0' 
        else:
            print("Consent cannot be undone!")
            exit()
    else:
        admissionStatus = '0'
    
    #Writes all to the file
    file.write(p_name+"\n")
    file.write(p_age+"\n")
    file.write(p_gender+"\n")
    file.write(p_contact+"\n")
    file.write(p_addr+"\n")
    file.write(f_name+"\n")
    file.write(f_age+"\n")
    file.write(f_contact+"\n")
    file.write(f_addr+"\n")
    file.write(m_name+"\n")
    file.write(m_age+"\n")
    file.write(m_contact+"\n")
    file.write(m_addr+"\n")
    file.write(p_diseaseCode+"\n")
    file.write(admissionStatus+"\n")
    if admissionStatus == '1':
        file.write(admYear+"\n")
        file.write(admMonth+"\n")
        file.write(admDay+"\n")
        file.write(str(admDate)+"\n")
    else:
        file.write("No Admission Date")
        file.close()

    f=open("..\pidcount",'w')              #Updating the pid in pidcount.txt
    f.write(str(pid))
    f.close()

    print("\nPatient successfully registred with Patient ID (PID):",str(pid) + "\nNever lose this PID and use this PID for future refrences")
    