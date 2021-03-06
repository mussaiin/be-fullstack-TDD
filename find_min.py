def get_min(a, b):
    """
        return min number among a and b
    """
    return b if a > b else a


def get_min_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('there is no arguments in your function')


def get_min_with_one_argument(x):
    """
        return that value
    """
    return x

def get_min_with_many_arguments(*args):
    """
        return smallest number among args
    """
    minValue = args[0]

    for i in args:
        if i < minValue:
            minValue = i

    return minValue


def get_min_with_one_or_more_arguments(first, *args):
    """
        return smallest number among first + args
    """
    minValue = first

    for i in args:
        if i < minValue:
            minValue = i

    return minValue

def get_min_bounded(*args, low, high):
    """
        return smallest number among args bounded by low & high
    """
    minValue = high

    for i in args:
        if i > low and i < high and i < minValue:
                    minValue = i

    return minValue

def make_min(*, low, high):
    """
        return inner function object which takes at least one argument
        and return smallest number amount it's arguments, but if the
        smallest number is lower than the 'low' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        minValue = float('inf')
        for i in (first,) + args:
            if i < minValue and low < i < high:
                minValue = i
        return minValue

    return inner
