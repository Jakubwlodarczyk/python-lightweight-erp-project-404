# implement commonly used functions here

import random
import ui


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    generated = ''
    is_unique = False
    id_table = []
    for row in table:
        id_table.append(row[0])

    while not is_unique:
        is_unique = True
        for i in range(2):
            generated += str(special_chars[random.randint(0, len(special_chars)-1)])
            generated += str(digits[random.randint(0, len(digits)-1)])
            generated += str(alphabet[random.randint(0, len(alphabet)-1)])
            generated += str(alphabet[random.randint(0, len(alphabet)-1)].upper())
        if generated in id_table:
            is_unique = False
    return generated


def sum_numbers(numbers_list):
    output = 0
    for number in numbers_list:
        output += number
    return output


def mean_from_list(num_list):
    num_sum = 0
    for num in num_list: #making sum of number in list
        num_sum += int(num)
    mean = num_sum / len(num_list) #dividing by
    if mean.is_integer():
        mean = int(mean)
    return mean


def is_this_record_exist(table, id_):
    """
    Checking if user input id exist in your table

    Args:
        table: your table
        id_: user input id to check

    Returns:
        True if this record exist, then you can use your function update or remove
        False if record not exitst and print error message

    Example usage:
        if common.is_this_record_exist(table, id_[0]):
            table = update(table, id_[0])
    """
    if id_ not in [record[0] for record in table]:
        ui.print_error_message("Record with this ID not found")
        return False
    return True


def remove_record_from_table(table, id_):
    """
    Remove record from your table by ID.
    Important! Before you use this function check
    if given ID exist in your table by using is_this_record_exist function.

    Args:
        table: your table
        id_: user input id to remove

    Returns:
        Table with removed record
    """
    i = 0
    while i < len(table):
        if id_ == table[i][0]:
            del table[i]
            return table
        i += 1
