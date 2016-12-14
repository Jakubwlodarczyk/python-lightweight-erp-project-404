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
        show_table(table[:])
    elif option == "2":
        add(table)
    elif option == "3":
        id_to_remove = ui.get_inputs(['Enter id to remove: '], '')
        if common.is_this_record_exist(table, id_to_remove[0]):
            remove(table, id_to_remove)
    elif option == "4":
        try:
            id_to_update = ui.get_inputs(['Enter id to update'], '')
            update(table, id_to_update)
        except ValueError as msg:
            ui.print_error_message(msg)
    elif option == "5":
        year = which_year_max(table)
        ui.print_result(year, 'Best profit year')
    elif option == "6":
        try:
            year = ui.get_inputs(['which year?'], '')
            answear = avg_amount(table, year[0])
        except ValueError as msg:
            ui.print_error_message(msg)
        ui.print_result(answear, 'Averge profit')
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
    table = common.add_to_table(table, list_labels)
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
    table = common.remove_record_from_table(table, id_[0])
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
    list_labels = ['Month',
                   'Day',
                   'Year',
                   'Type',
                   'Amount']
    # your code
    common.update_table(table, id_, list_labels)

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    profit_dict = {}
    profit = 0
    year = 0
    for item in table:
        if item[3] not in profit_dict:
            if item[4] == 'in':
                profit_dict[item[3]] = int(item[5])
            else:
                profit_dict[item[3]] = -int(item[5])
        else:
            if item[4] == 'in':
                profit_dict[item[3]] += int(item[5])
            else:
                profit_dict[item[3]] -= int(item[5])
    for k, v in profit_dict.items():
        if v > profit:
            profit = v
            year = k
    return int(year)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    items = 0
    profit = 0
    title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
    # your code
    for item in table:
        if int(item[3]) == int(year):
            items += 1
            if item[4] == 'in':
                profit += int(item[5])
            else:
                profit -= int(item[5])

    avg = profit / items
    return avg
