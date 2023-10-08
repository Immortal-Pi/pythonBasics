# import the py file to call the functions from that file
import helloFunctionsInput
import leapYear

if __name__ == '__main__':
    # print the return value from the function
    """
      multiple line comment
    """
    # print(' hello, ' + helloFunctionsInput.func())
    year = input('enter year: ')

    print((leapYear.leapYear(int(year))))
