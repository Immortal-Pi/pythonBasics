import random


class Hat:
    houses = ["hebbal", "dasarahalli", "bangalore"]
    def __init__(self,name,address):
        self.name=name
        self.address=address
    @classmethod #no need to create objects
    def sort(cls,name):
        print(f"{name} is in {random.choice(cls.houses)}")

    @classmethod #used to get input without objects
    def get(cls):
        name=input("name:")
        address=input("address:")
        return cls(name,address)


def methodsinclass():
    # h=Hat()
    h=Hat.get()
    print(h.name,h.address)
    return