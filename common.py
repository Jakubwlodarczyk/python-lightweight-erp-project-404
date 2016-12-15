# implement commonly used functions here

import random
import ui
import data_manager


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
            generated += str(special_chars[random.randint(0, len(special_chars) - 1)])
            generated += str(digits[random.randint(0, len(digits) - 1)])
            generated += str(alphabet[random.randint(0, len(alphabet) - 1)])
            generated += str(alphabet[random.randint(0, len(alphabet) - 1)].upper())
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
    for num in num_list:  # making sum of number in list
        num_sum += int(num)
    mean = num_sum / len(num_list)  # dividing by
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


        if common.is_this_record_exist(table, id_):
            table = update(table, id_)
    """
    if id_[0] not in [record[0] for record in table]:

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

        if id_[0] == table[i][0]:

            del table[i]
            return table
        i += 1


def validate(row, title_list, type_list):
    '''
        validate user input
        Sample call:
            validate(row_to_validate, title_list, type_list)
        Sample display:
            Wrong input
            Year (user input)
            Wrong input
            Type (user input)

        Args:
            row : row to validate
            title_list: List of names of varibals
            type_list : list of types of varibals:
                str = string
                int = integer
                in = in or out
                day = from 1 to 31
                month = fron 1 to 12

        Returns:
            Validated row
    '''

    for i in range(len(row)):
        switch = True
        if type_list[i] == 'str':
            pass
        elif type_list[i] == 'int':
            while switch:
                if row[i].isdigit():
                    switch = False
                else:
                    new_answear = ui.get_inputs([title_list[i]], 'Wrong input')
                    row[i] = new_answear[0]
        elif type_list[i] == 'in':
            while switch:
                if row[i] == 'in' or row[i] == 'out':
                    switch = False
                else:
                    new_answear = ui.get_inputs([title_list[i]], 'Wrong input')
                    row[i] = new_answear[0]
        elif type_list[i] == 'day':
            while switch:
                if row[i].isdigit():
                    if 0 < int(row[i]) < 32:
                        switch = False
                else:
                    new_answear = ui.get_inputs([title_list[i]], 'Wrong input')
                    row[i] = new_answear[0]
        elif type_list[i] == 'month':
            while switch:
                if row[i].isdigit():
                    if 0 < int(row[i]) < 13:
                        switch = False
                else:
                    new_answear = ui.get_inputs([title_list[i]], 'Wrong input')
                    row[i] = new_answear[0]

    return row


def add_to_table(table, title_list, type_list):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to
        title_list: list of varibal names to add 
        type_list: list of varibal types to add

    Returns:
        Table with a new record
    """
    new_row = ui.get_inputs(title_list, 'What you wanna to add?')
    new_row = validate(new_row, title_list, type_list)
    new_id = generate_random(table)
    new_row.insert(0, new_id)
    table.append(new_row)
    return table


def update_table(table, id_, title_list, type_list):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        title_list: list of varibal names to add 
        type_list: list of varibal types to add

    Returns:
        table with updated record
    """
    record = 0
    for record in range(len(table)):
        if table[record][0] == id_[0]:
            new_row = ui.get_inputs(title_list, 'New Value:')
            i = 0
            while i < len(new_row):
                if new_row[i] == '':
                    new_row[i] = table[record][i + 1]
                i += 1
            new_row = validate(new_row, title_list, type_list)
            new_row.insert(0, table[record][0])
            table[record] = new_row
            print(table[record])
    return table
