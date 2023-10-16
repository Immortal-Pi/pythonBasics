class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

def sortedOp():

    list1=[5,4,3,2,1]
    print(sorted(list1,reverse=True))

    # sorts as per the first index of the tuple
    list2=[(3,2),(4,5),(1,1)]
    print(sorted(list2,key=lambda x:x[1]))

    grades=[('amruth',66),('aksath',77,),('sharath',44)]
    print(grades)
    print(sorted(grades,key=lambda x:x[0]))


    # Sorted function for class objects
    students = [Student("Alice", 20), Student("Bob", 22), Student("Charlie", 19)]
    students1=sorted(students,key=lambda x:x.age)

    for i in students1:
        print(i.name,i.age)
    return