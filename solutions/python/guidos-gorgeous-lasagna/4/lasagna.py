"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(baking_time_in_minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    baking_time = EXPECTED_BAKE_TIME-baking_time_in_minutes
    return baking_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time needed for preparation

    :param: int - number of layers for the lasagna
    :return: int - time needed to bake the lasagna based on the number of layers
    """
    preparation_time = number_of_layers * 2
    return preparation_time


def elapsed_time_in_minutes(number_of_layers, baking_time):
    """Calculate total time spent in the preparation

    :param: int - number of layers for the lasagna
    :param: int - elapsed baking time
    :return: int - total time of preparation
    """
    return (number_of_layers * 2)+baking_time


print("Elapsed time: ",elapsed_time_in_minutes(3,bake_time_remaining(25)))