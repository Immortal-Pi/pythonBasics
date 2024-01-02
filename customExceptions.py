import Exceptions


class negitiveException(Exception):

    def __init__(self,message):
        super().__init__("negitive nubmer not allowed")

class zeroDivideException(Exception):
    def __init__(self):
        super().__init__("non zero number please")
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


