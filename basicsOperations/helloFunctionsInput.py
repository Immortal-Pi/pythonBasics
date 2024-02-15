# function func which can be called anywhere
def func():
    # define variable
    a = 30
    b = 20
    c = 50
    name = input('whats your name? ')
    print("{} and {} and {}".format(a, b, c))
    # returns value to the main function
    return name
