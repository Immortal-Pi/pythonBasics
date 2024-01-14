class Student:
    def __init__(self,name,address=None):
        self.name=name
        self.address=address

class subject(Student):

    def __init__(self,name,address,subject):
        self.subject=subject
        Student.__init__(self,name,address)
        # super().__init__(name,address)


class bus(subject):
    def __init__(self,busno,subject,name):
        self.busno=busno
        Student.__init__(self,name)




def infunction():

    subject1=subject('amruth',"hebbal",'math')
    bus1=bus(12,'math',"amruth")
    print(f"{subject1.name} is at {subject1.address} studying {subject1.subject}")
    print(f"{bus1.name} is at {bus1.address}")
    return