
def total(notes=0,coins=0,online=0):
    print(f"notes:{notes} and coins:{coins}")
    return coins+notes+online
def unpacking123():
    # coins=[2,4,5]
    """
    *coins to send list as an argument, sends the elements of list to the variables
    **coins will send the dictionary along with keys and keys have to be the parameters, no need to be in an order
    unpacking a list
    """
    coins={"coins":10,"notes":20,"online":300}
    # print(total(*coins))
    print(total(**coins))
    return



def func(*args,**kwargs):
    """
            used for variable number of arguments as parameter (0-..)
            * args      arguments
            ** kwargs   kwyword arguments
            if not used may run into type error

            below is to manipulate values of dictionary
    """
    # print("positional:",args)
    # print("named:",kwargs)
    # list2=list(map(lambda x:x["name"].upper(),args))
    # list3=list(filter(lambda x:x["salary"]==200,args))
    # print(list2)
    # for person in sorted(list3,key=lambda x:x["address"]):
    #     print(f"{person['name']} is at {person['address']} earning {person['salary']}")
    # upper=[]
    #
    # upper.append(list(map(lambda x:x.upper(),kwargs.keys())))
    # print(upper)

    """
     creating dictionary on the fly
     
    """

    # student=["amruth","akshath","sharath"]
    #
    # studentAshokaHouse = [{"name": name, "house": "ashoka"} for name in student]
    # print(studentAshokaHouse)


    """
        indexing or giving numbers to values in a list
        using enumerate
        
        secnario 1: where we need indexing
    """

    name=["amruth","akshath","sharath"]

    for i in range(len(name)):
        print(i+1,name[i])

    """
        indexing with enumerate
        enumerate(value,start=0) - it gives back value and index 
    """
    print(enumerate(name))

    for i,student in enumerate(name):
        print(i+1,student)
