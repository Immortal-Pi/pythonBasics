def fileiooperations():

    names =[]

    # for _ in range(3):
    #     names.append(input("name : "))
    # syntax one
    # file = open("names.txt", "a")


    #syntax two
    # with open("names.txt","a") as file:
    #     for name in sorted(names):
    #     # print(f"Hello,{name} ")
    #         file.write(f'{name}\n') #write operation
    # file.close() needed for syntax one


    with open("names.txt","r") as file:
        lines=file.readlines()
    for line in lines:
        print(line)

    return