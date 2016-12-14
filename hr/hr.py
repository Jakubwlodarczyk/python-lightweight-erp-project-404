# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file('hr/persons.csv')
    options = [
        'Show Table',
        'Add to Table',
        'Remove from Table',
        'Update Table',
        'Get oldest person',
        'Get persons closest to average']

    while True:
        ui.print_menu('HR menu', options, 'Back to main menu')

        inputs = ui.get_inputs(['Enter the number'], '')
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            id_ = ui.get_inputs(["ID: "], "Please provide ID of record to remove")
            if common.is_this_record_exist(table, id_[0]):
                table = remove(table, id_[0])
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please provide ID of record to update")
            if common.is_this_record_exist(table, id_[0]):
                table = update(table, id_[0])
        elif option == "5":
            ui.print_result(get_oldest_person(table), "Oldest persons")
        elif option == "6":
            ui.print_result(get_persons_closest_to_average(table), "Closest persons to average year")
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['Id', 'Name', 'Year']
    ui.print_table(table[:], title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ui.get_inputs(["Name and surname: ", "Birth date: "], "Please provide person data")
    new_key = common.generate_random(table)
    table.append([new_key, inputs[0], inputs[1]])
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """
    i = 0
    while i < len(table):
        if id_ == table[i][0]:
            del table[i]
            return table
        i += 1


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """
    inputs = ui.get_inputs(["Name and surname: ", "Birth date: "], "Please provide person data to update")
    i = 0
    while i < len(table):
        if id_ == table[i][0]:
            table[i][1], table[i][2] = inputs[0], inputs[1]
            return table
        i += 1


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    """ Searching for oldest persons in table, return string of names """
    oldest_year = min([int(year[2]) for year in table])  # search for oldest year
    oldest_person = []
    i = 0
    while i < len(table):
        if int(table[i][2]) == oldest_year:
            oldest_person.append(table[i][1])
        i += 1
    return oldest_person

# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)


def get_persons_closest_to_average(table):
    """ Searching for closest persons to average year in table, return string of names """
    average = 0
    for year in table:
        average += int(year[2])  # sum of years
    average = round(average/len(table))  # average year

    list_of_abs = [abs(int(person[2])-average) for person in table]  # make list of substract years with same index
    min_from_abs = min(list_of_abs)
    closest_person = []

    i = 0
    while i < len(table):
        if list_of_abs[i] == min_from_abs:
            closest_person.append(table[i][1])
        i += 1
    return closest_person
