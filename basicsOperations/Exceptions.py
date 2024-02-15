class Error(Exception):
    pass


def exceptionTestcases():

    try:
        x = int(input())
        y = int(input())
        c=x/y
        if x<0 or y<0:
            raise Error

    except ValueError:
        print("input is not integer")
        # pass
    except ZeroDivisionError:
        print("please provide number greater than 0")
        # pass
    except TypeError:
        print("try to make the datatype similar")
    except Error:
        print("negitive numbers")
    else:
        print(c)
        # print('hello')
    finally:
        print("done")
        return
