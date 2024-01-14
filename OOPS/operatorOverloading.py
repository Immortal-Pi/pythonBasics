class student:
    def __init__(self,money,assets, name):
        self.money=money
        self.assets=assets
        self.name=name

    def __str__(self):
        return f"{self.name} has {self.money} money and {self.assets} assets in our firm"

    def __add__(self, other):
        return student(self.money+other.money, self.assets+other.assets, self.name+" & "+other.name)

    def __lt__(self, other):
        if self.money<other.money:
            print(f"{self.name} has less assets than {other.name}")
        else:
            print(f"{self.name} has more assets than {other.name}")


def operatorOverloading():
    student1=student(100,25,"amruth")
    student2=student(200,35,"Akshath")
    student3=student(500,23,"sharath")
    student4=student1+student2+student3
    print(student4)
    _=student2>student4
    return