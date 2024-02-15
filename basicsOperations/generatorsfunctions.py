def genfunctions(number):
    for i in sheep(number):
        print(f"{i} \n")
    return

def sheep(number):
    yield "*"*number

