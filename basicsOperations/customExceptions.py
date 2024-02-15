import Exceptions


class negitiveException(Exception):

    def __init__(self,message):
        super().__init__(message)

class zeroDivideException(Exception):
    def __init__(self):
        super().__init__("non zero number please")

class above50exception(Exception):
    def __init__(self):
        super().__init__('above 50')
def exceptions123():
    try:
        x=int(input())
        y=int(input())
        if x<0 or y<0:
            raise negitiveException('negitive number')
        elif y==0:
            raise zeroDivideException()
        else:
            print(x/y)
    except zeroDivideException as e:
        print('divide by zero exception',e)
    except negitiveException as e:
        print("custom exception caught:",e)
    except Exceptions as e:
        print("some other exception:",e)


def exception234():
    try:
        x=int (input())
        y=int (input())
        if x+y>50:
            raise above50exception()
        else:
            print(x+y)
            name='amruth'
            name1=name[::-1]
            print(name1)
    except above50exception as e:
        print('above 50, please enter values below 50')
    finally:
        print('anyways')


