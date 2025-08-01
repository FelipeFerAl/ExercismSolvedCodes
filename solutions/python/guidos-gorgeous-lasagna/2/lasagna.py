"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(preparation_time_in_minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-preparation_time_in_minutes


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time needed for preparation

    :param: int - number of layers for the lasagna
    :return: int - time needed to bake the lasagna based on the number of layers
    """
    return number_of_layers * 2
    
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def elapsed_time_in_minutes(number_of_layers, baking_time_remaining):
    """Calculate total time spent in the preparation

    :param: int - number of layers for the lasagna
    :param: int - elapsed baking time
    :return: int - total time of preparation
    """
    return (number_of_layers * 2)+baking_time_remaining

baking_time_remaining = bake_time_remaining(25)
preparation_time = preparation_time_in_minutes(3)
print("Elapsed time: ",elapsed_time_in_minutes(3,baking_time_remaining))