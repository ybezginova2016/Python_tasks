def scale(data, factor):
    """
    Multiply all entries of numeric data list by the given factor.
data an instance of any mutable sequence type (such as a list)
containing numeric elements
factor a number that serves as the multiplicative factor for scaling
    :param data:
    :param factor:
    :return:
    """
    for j in range(len(data)):
        data[j] *= factor
    return data, factor

print(scale([1, 4, 5, 6], 2))

"""
Guidelines for authoring useful docstrings are available
at: http://www.python.org/dev/peps/pep-0257/
"""