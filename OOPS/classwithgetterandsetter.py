class student:

    def __init__(self,name,address):
        self.name=name
        self.address=address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")

        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if address not in ["hebbal", "dasarahalli", "bangalore"]:
            raise ValueError("missing house")

        self._address = address

    def __str__(self):
        return f"{self.name} is from {self.address}"


def classworks():
    student1=student("amruth",'hebbal')
    # student1.address='das'
    # student1._address='das' #exception of using _
    print(student1)