# import the py file to call the functions from that file
import helloFunctionsInput
import leapYear
import typeConversion

if __name__ == '__main__':
    # print the return value from the function
    """
      multiple line comment
    """
    # Functions
    name = helloFunctionsInput.func()

    # sting manipulation methods
    typeConversion.stringManipulation(name)
    # escape sequence example
    # print(' hello,\n ' + name)

    # format print with f
    # print(f"hello, {name}")

    # year = input('enter year: ')
    # Function for Leap Year
    # print((leapYear.leapYear(int(year))))
