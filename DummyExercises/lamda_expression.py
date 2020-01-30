def add(a, b):
    return a+b  # normal expression


def add2(a, b): return a+b  # lamda expression

#mulitply = lambda a,b : a*b


def mulitply(a, b): return a*b


print(mulitply(2, 3))


def is_even(arg):
    if arg % 2 == 0:  # return arg %2 == 0
        return True
    else:
        return False


print(is_even(4))

# in lambda expression


def isEven(arg): return arg % 2 == 0  # isEven = lambda arg : arg%2 == 0


# example 2
def last_char(s): return s[-1]


print(last_char('arafat'))


# lambda if else

def func(s):
    if len(s) > 5:
        return True
    return False


# func2 = lambda s : TRue if len(s) > 5 else False
def func2(s): return True if len(s) > 5 else False


print(func2('afnvfhfa'))
