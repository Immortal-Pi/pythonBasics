import csv
def fileiooperations():

    names =[]
    # syntax 1 write
    # for _ in range(3):
    #     names.append(input("name : "))
    # syntax one
    # file = open("names.txt", "a")


    #syntax 2 write
    # with open("names.txt","a") as file:
    #     for name in sorted(names, reverse=True):
    #     # print(f"Hello,{name} ")
    #         file.write(f'{name}\n') #write operation
    # file.close() needed for syntax one

    # syntax 1 read
    #read all the lines at once
    # with open("names.txt","r") as file:
    #     lines=file.readlines()
    # for line in sorted(lines):
    #     print(line.rstrip())



    # syntax 2 read
    # with open("names.txt","r") as file:
    #     for line in file:
    #         print(line.rstrip())


    #CSV files
    students={}
    # with open("names2.csv","r") as file:
    #     for line in file:

            # syntax 1
            # row=line.rstrip().split(',')
            # print(f"name: {row[0]}, address: {row[1]}")

            # syntax 2
            # name, address = line.rstrip().split(',')
            # print(f"{name}: {address}")
            # students[name]=address #dictionary

    # for k,v in student.items():
    #     print(k,v)

    # with open("names2.csv","w") as file:

    #list of dictionaries
    students=[]
    # with open("names2.csv","r") as file:
    #     for line in file:
    #         name, address=line.rstrip().split(',')
    #         student={"name":name,"address":address}
    #         # student["name"]=name
    #         # student["address"]=address
    #         students.append(student)
    # # print(students)
    # for student1 in sorted(students, key=lambda x:x["name"]):
    #     print(f"{student1['name']} is from {student1['address']}")



    #CSV file with delimeter
    # library in python we can read csv files using reader


    # students=[]
    # with open("names2.csv","r") as file:
    #     reader=csv.reader(file) #only flaw is that if the excel header is there it is not going to identify
    #     for name,address in reader:
    #         students.append({"name":name,"address":address})
    # print(students)

    # using DictReader for using headers in Excel/CSV files
    # students = []
    # with open("names3.csv", "r") as file:
    #     reader = csv.DictReader(file)  # only flaw is that if the excel header is there it is not going to identify
    #     for row in reader:
    #         students.append({"name": row["name"], "address": row["address"]})
    # for student in students:
    #     print(f"{student['name']} is from {student['address']}")


    #write to a csv file
    students=[]

    # with open("names3.csv","a") as file:
    #     for _ in range(3):
    #         name = input("whats your name:")
    #         address = input("whats your address:")
    #         writer=csv.writer(file) #CSV.writer writes one row at a time
    #         writer.writerow([name, address])


    # write to a csv file using fieldnames
    students = []

    # with open("names3.csv","a") as file:
    #     for _ in range(3):
    #         name = input("whats your name:")
    #         address = input("whats your address:")
    #
    #         writer=csv.DictWriter(file,fieldnames=["name","address"]) #CSV.writer writes one row at a time
    #         writer.writerow({"address":address.rstrip(), "name":name.rstrip()})



















    return
