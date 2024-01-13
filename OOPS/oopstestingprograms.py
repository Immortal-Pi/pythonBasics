
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("missing name")
        # if house not in ["hebbal","dasarahalli","kempapura"]:
        #     raise ValueError("invalid house")

        else:
            self.name=name
            self.house=house


    # represent an object as string
    def __str__(self):
        return f"{self.name} is from {self.house}"

    @property
    def house(self):
        return self._house

    #setter sets some value
    @house.setter
    def house(self,house):
        if house not in ["hebbal","dasarahalli","kempapura"]:
            raise ValueError("invalid house")
        self._house=house
def testing():

    # name, address=get_student() #tuple
    student=get_student() #tuple
    # student[0]='akshath' #tuple is immutable value cannot be assigned since its immutable
    # print(f"{student[0]} is from {student[1]}") # tuple can be indexed but not assigned
    # student.house='hebbala'
    # print(f'{student["name"]} is from {student["house"]}')
    print(student) #represting an object in string because of using __str__
    # print(student.charm())
    return

def get_student():

    # return dictionary
    name = input("name:")
    house = input("house:")

    # return {"name":name,"house":house}


    # student=Student() #creating objects eg. student
    # student.name=input("name:")
    # student.house=input("house:")


    #constructor call
    # student=Student(name,house)
    return Student(name,house)

    # return student


    # return