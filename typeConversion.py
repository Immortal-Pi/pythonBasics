def stringManipulation(inputString):

    #Remove whitespace from string
    # inputString = inputString.strip()
    # print ('hello, ' + inputString)

    # Capitalize user's first name
    # inputString = inputString.capitalize()
    # print('hello, ' + inputString)

    # Title Capitalize first letter of all the words
    # inputString = inputString.title()
    # print('hello, ' + inputString)

    # Chain the commands together
    inputString = inputString.strip().title()
    print ('hello, ' + inputString)
    return

def numberStringConversion(inputString):

    # int() converts the string to number
    number=int(inputString)
    print(number,type(number))

def allTypeConversion(input):

    # find the type
    print(type(input))
    if isinstance(input,int):
        # output=str(input) # convert to sting
        # print(output, type(output))
        output = float(input) # convert to float
        print(output, type(output))
    elif isinstance(input,str):
        output = int(input) # convert
        print(output, type(output))

