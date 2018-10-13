def get_max(a, b):
    return a if a > b else b


def get_max_without_arguments():
    raise TypeError('there is no arguments in your function')


def get_max_with_one_argument(a):
    return a


def get_max_with_many_arguments(*args):
    maxValue = args[0]

    for i in args:
        if i > maxValue:
            maxValue = i

    return maxValue


def get_max_with_one_or_more_arguments(first, *args):
    maxValue = first
    for i in args:
        if i > maxValue:
            maxValue = i

    return maxValue

def get_max_bounded(*args, low, high):
    maxValue = low

    for i in args:
        if i > low and i < high and i > maxValue:
            maxValue = i

    return maxValue


def make_max(*, low, high):
    def inner(first, *args):

        maxValue = low
        for i in (first,) + args:
            if i > maxValue and low < i < high:
                maxValue = i
        return maxValue

    return inner
