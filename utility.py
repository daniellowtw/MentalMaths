__author__ = 'Daniel'

def get_integer_input(query="", default=None):
    """
    Takes a query and gets an input from the user
    :param query:
    :param default:
    :return:
    """
    res = ""
    while not str.isnumeric(res):
        res = input(query)
        if res == "" and default is not None:
            return default
    return int(res)
