import string
import cowsay
import argparse
# import sys - this is used to get command line arguments into a function
class nameException(Exception):
    def __init__(self,message):
        super().__init__('name format incorrect')
def commandLine(inputString):
    try:
        if inputString.isdigit():
            raise nameException('name')
        else:
            # cowsay.cow('my name is '+ inputString)
            cowsay.trex('say what '+ inputString)

    except nameException as e:
        print(e)



