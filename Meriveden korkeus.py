"""
# COMP.CS.100 Project 2: Changes in seawater levels
# Made by: Linda Riikonen
"""


def deviation_value(seawater_levels, mean):
    """
    Calculate variance using mean, then calculate deviation using variance
    :param seawater_levels: the list of seawater levels the user gave
    :param mean: the calculated mean
    :return: calculated deviation
    """
    value = 0

    for index in range(0, len(seawater_levels)):
        value += (float(seawater_levels[index]) - mean) ** 2

    variance = 1 / (len(seawater_levels) - 1) * value
    deviation = variance ** (1/2)

    return deviation


def mean_value(seawater_levels):
    """
    Calculate the mean from the given list of seawater levels
    :param seawater_levels: the list of seawater levels the user gave
    :return: the calculated mean
    """
    all_levels = 0

    for index in range(0, len(seawater_levels)):
        all_levels += float(seawater_levels[index])

    mean = all_levels / len(seawater_levels)

    return mean


def median_value(seawater_levels):
    """
    Turn the list into ascending order and find the median
    :param seawater_levels: the list of seawater levels the user gave
    n: the number of values in the list
    :return: the calculated median
    """
    sorted_levels = sorted(seawater_levels)
    n = len(sorted_levels)

    # The median is the middle value if there is an odd number of values
    if n % 2 != 0:
        index = int(n/2)
        median = float(sorted_levels[index])

    # The median is the mean of two central-most values if there is an even
    # number of values
    else:
        index_1 = int((n/2) - 1)
        index_2 = int(n/2)
        median = (float(sorted_levels[index_1]) +
                  float(sorted_levels[index_2])) / 2

    return median


def min_max_values(seawater_levels):
    """
    Find the smallest and greatest value in the list
    :param seawater_levels: the list of seawater levels the user gave
    :return: the smallest and the greatest values
    """
    minimum = maximum = None

    if len(seawater_levels) > 1:
        minimum = min(seawater_levels)
        maximum = max(seawater_levels)

    return minimum, maximum


def main():
    """
    Add the values given by the user into an empty list and check that there
    are more than two values. Call for functions to find the desired values.
    """
    # Create an empty list for the values
    seawater_levels = []

    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    while True:
        level = input()

        # Stop the loop if the input is empty
        if level == "":
            break
        # Insert the given values to the list
        else:
            seawater_levels.append(level)

    # Check the number of values in the list and print an error message if it's
    # less than two
    if len(seawater_levels) < 2:
        print("Error: At least two measurements must be entered!")

    else:
        # Find the desired values using dedicated functions and
        # print them with two decimals
        min_value, max_value = min_max_values(seawater_levels)
        print(f"Minimum: {float(min_value):.2f} cm")
        print(f"Maximum: {float(max_value):.2f} cm")

        median = median_value(seawater_levels)
        print(f"Median: {float(median):.2f} cm")

        mean = mean_value(seawater_levels)
        print(f"Mean: {float(mean):.2f} cm")

        deviation = deviation_value(seawater_levels, mean)
        print(f"Deviation: {float(deviation):.2f} cm")


if __name__ == "__main__":
    main()
