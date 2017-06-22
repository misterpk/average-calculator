def get_numbers():
    """Gets numbers to be used in calculations from user"""
    list_values = input("Enter numbers separated by a space: ").split()
    float_values = []
    for i in list_values:
        float_values.append(float(i))
    return float_values


def average(list_for_averages):
    """Returns the average of a list of numbers entered by the user in
    get_numbers()"""
    total = 0
    counter = 0

    for i in list_for_averages:
        total += i
        counter += 1

    return total/counter


def median(list_for_median):
    """Returns the median value of a list of numbers entered by the user in
    get_numbers()"""
    list_for_median.sort()
    middle_index = int(len(list_for_median) / 2)

    if len(list_for_median) % 2 == 1:
        # return the middle element of an odd length list
        return list_for_median[middle_index]
    else:
        # return the average of the middle 2 elements in an even length list
        return (list_for_median[middle_index] +
                list_for_median[middle_index - 1]) / 2


def mode(list_for_mode):
    """Returns the mode of a list of numbers entered by the user in
    get_numbers()"""
    count_of_values = {}
    modes = []
    largest_value = 0

    # count how many times a value appears
    for i in list_for_mode:
        if i not in count_of_values:
            count_of_values[i] = 1
        else:
            count_of_values[i] = int(count_of_values.get(i)) + 1

    # determine the largest number of times a value repeats
    for k, v in count_of_values.items():
        if count_of_values.get(k) > largest_value:
            largest_value = v

    # add the mode(s) to a new list
    for k, v in count_of_values.items():
        if v == largest_value:
            modes.append(k)

    if largest_value == 1:
        return []

    return modes


if __name__ == "__main__":
    values = get_numbers()
    the_mode = mode(values)

    print("The average of the values entered is {:.3f}".format(average(values)))
    print("The median of the values entered is {:.3f}".format(median(values)))

    # handle the case where no mode is present
    if not the_mode:
        print("There is no mode since there are no repeating values.")
    else:
        print("The mode of the values entered is/are {}".format(the_mode))
