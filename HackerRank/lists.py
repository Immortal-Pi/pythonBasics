def listOperations():
    #https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
    listfinal = []
    N = int(input())
    for i in range(0, N):
        list1 = []
        command = str(input())
        list1 = command.split(" ")

        if list1[0]=="insert":
            listfinal.insert(int(list1[1]),int(list1[2]))
        elif list1[0]=="append":
            listfinal.append(int(list1[1]))
        elif list1[0]=="print":
            print(listfinal)
        elif list1[0]=="remove":
            listfinal.remove(int(list1[1]))
        elif list1[0]=="sort":
            listfinal.sort()
        elif list1[0]=="reverse":
            listfinal.reverse()
        elif list1[0]=="pop":
            listfinal.pop()
    #print(listfinal)


    return

def listComprehensions():
    # https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list1=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i+j+k)!=n):
                    list1.append([i,j,k])
    print(list1)
    return