"""
here we implement the function to return the variance of a list
we will do it for both sample variance and population variance
"""


# population variance:

def population_variance(some_list):
    """
    this population_variance function accepts a list
    and returns the population variance of a list
    """
    number_of_elements = 0
    sum_of_list = 0
    numerator = 0

    for i in some_list:

        # first let's get the number of elements in the list:
        number_of_elements = number_of_elements + 1

        # now we need the sum of the list
        sum_of_list = sum_of_list + i

    for i in some_list:
        # let's work on the numerator
        numerator = numerator + ((i - (sum_of_list/number_of_elements)) ** 2)

    # now we arrive at the answer
    return numerator/number_of_elements


# sample variance:


def sample_variance(some_list):
    """
    this sample_variance function accepts a list
    and returns the sample variance of a list
    """

    number_of_elements = 0
    sum_of_list = 0
    numerator = 0

    for i in some_list:

        # first let's get the number of elements in the list:
        number_of_elements = number_of_elements + 1

        # now we need the sum of the list
        sum_of_list = sum_of_list + i

    for i in some_list:
        # let's work on the numerator
        numerator = numerator + ((i - (sum_of_list/number_of_elements)) ** 2)

    # now we arrive at the answer
    return numerator/(number_of_elements - 1)
