def get_max(a, b):
    """
        return max number among a and b
    """
    return a if a > b else b


def get_max_without_arguments():
    """
        raise TypeError exception with message
    """
    raise TypeError('there is no arguments in your function')


def get_max_with_one_argument(a):
    """
        return that value
    """
    return a


def get_max_with_many_arguments(*args):
    """
        return biggest number among args
    """
    maxValue = args[0]

    for i in args:
        if i > maxValue:
            maxValue = i

    return maxValue


def get_max_with_one_or_more_arguments(first, *args):
    """
        return biggest number among first + args
    """
    maxValue = first
    for i in args:
        if i > maxValue:
            maxValue = i

    return maxValue

def get_max_bounded(*args, low, high):
    """
        return biggest number among args bounded by low & high
    """
    maxValue = low

    for i in args:
        if i > low and i < high and i > maxValue:
            maxValue = i

    return maxValue


def make_max(*, low, high):
    """
        return inner function object which takes at least one argument
        and return biggest number amount it's arguments, but if the
        biggest number is bigger than the 'high' which given as required
        argument the inner function has to return it.
    """
    def inner(first, *args):

        maxValue = low
        for i in (first,) + args:
            if i > maxValue and low < i < high:
                maxValue = i
        return maxValue

    return inner
