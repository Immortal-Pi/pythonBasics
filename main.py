# import the py file to call the functions from that file
# import OOPS

import Exceptions
import GifcreationusingPIL
import OOPS.classwithgetterandsetter
import Packages
# import Packages
import commandLineArguments
import customExceptions
import fileInputOutputOperations
import formatStringNumber
import helloFunctionsInput
import leapYear
import libraries
import loops2
import patterns
import regularExpression
import typeConversion
import sys

import test_leapYear
from OOPS import oopstestingprograms

# class fewArgumentException(Exception):
#     def __init__(self,message):
#         super().__init__('too few arguments'+ message)

if __name__ == '__main__':
    # print the return value from the function
    """
      multiple line comment
    """
    # Functions
    # name = helloFunctionsInput.func()

    # sting manipulation methods
    # typeConversion.stringManipulation(name)
    # escape sequence example
    # print(' hello,\n ' + name)

    # format print with f
    # print(f"hello, {name}")

    # year = input('enter year: ')
    # Function for Leap Year
    # print((leapYear.leapYear(int(year))))

    # Type Conversion
    # typeConversion.numberStringConversion('2345')

    # all Type Conversion
    # var1 = int(input('value of variable 1'))
    # var1 = str(input('value of variable 1'))
    # var1 = int(input('value of variable 1'))
    # typeConversion.allTypeConversion(var1)


    # Change number formats
    # formatStringNumber.changeNumberFormat()
    # patterns.patternPyramid(3)
    # patterns.stringPatter("ABCDEFGHIJKLMNOPQRSTUVWXYZ",3)
    # patterns.matPattern(11,33)
    # patterns.aphabeticRangoli(3)
    # loops2.loops2()
    # print('hello')
    # Exceptions.exceptionTestcases()
    # customExceptions.exception234()
    # libraries.randomFunctions()


    # command line arguments usage
    # try:
    #     if len(sys.argv)<=2:
    #         raise fewArgumentException('')
    #
    #     else:
    #         commandLineArguments.commandLine(sys.argv[2])
    # except fewArgumentException as e:
    #     print(e)

    # list1=[]
    # for arg in sys.argv:
    #     list1.append(arg)
    # print(list1[::-1])


    #Packages
    # using packages and API's
    # Packages.packagesExperiment(sys.argv)


    # unit testing
    # test_leapYear.unitTestcase()


    # file i/o
    # fileInputOutputOperations.fileiooperations()



    #gif creation
    # GifcreationusingPIL.gifcreation(sys.argv)


    #Regular expression
    # regularExpression.regularExpressionex()
    # regularExpression.reformatdata()
    # regularExpression.extractinformation()


    #oops
    # oopstestingprograms.testing()
    OOPS.classwithgetterandsetter.classworks()
