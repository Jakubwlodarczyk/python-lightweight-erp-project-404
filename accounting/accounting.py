# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def choose(table):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        try:
            id_to_remove = ui.get_inputs(['Enter id to remove: '], '')
            table = remove(table, id_to_remove)
        except ValueError as msg:
            ui.print_error_message(msg)
    elif option == "4":
        update(table)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        avg_amount(table)
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # you code
    table = data_manager.get_table_from_file('accounting/items_test.csv')
    options = ['Show table',
               'Add',
               'Remove',
               'Update',
               'Which year max',
               'Avg amount']

    menu = None
    while menu == None:
        ui.print_menu('Accounting menu', options, 'Back to main')
        try:
            menu = choose(table)
        except KeyError as err:
            ui.print_error_message(err)
    print(table)
    data_manager.write_table_to_file('accounting/items_test.csv', table)
    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
    ui.print_table(table, title_list)
    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code
    list_labels = ['Month',
                   'Day',
                   'Year',
                   'Type',
                   'Amount']
    new_row = ui.get_inputs(list_labels, 'What you wanna to add?')

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
    count = 0
    for i in range(len(table)):
        if str(id_[0]) == str(table[i][0]):
            table.remove(table[i])
            count = 1
    if count == 0:
        raise ValueError('No record of that id')

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
