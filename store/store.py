# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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

    table = data_manager.get_table_from_file('store/games_test.csv')
    options = [
        'Show Table',
        'Add to Table',
        'Remove from Table',
        'Update Table',
        'Get count by manufactures',
        'Get average by manufacturer']

    manufacturer = []
    for i in table:
        if i[2] not in manufacturer:
            manufacturer.append(i[2])

    while True:
        ui.print_menu('Store menu', options, 'Back to main menu')

        inputs = ui.get_inputs(['Enter the number'], '')
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            get_counts_by_manufacturers(table)
        elif option == "6":
            get_average_by_manufacturer(table, manufacturer)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['Id', 'Title', 'Manufacturer', 'Price', 'In_stock']
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
    list_labels = ['Title',
                   'Manufacturer',
                   'Price',
                   'In_stock']
    new_row = ui.get_inputs(list_labels, 'What you wanna to add?')
    new_id = common.generate_random(table)
    new_row.insert(0, new_id)
    table.append(new_row)

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

    list_labels = ['Title',
                   'Manufacturer',
                   'Price',
                   'In_stock']

    i = 0
    count = 0
    while i < len(table):
        if str(id_[0]) == str(table[i][0]):
            new_row = ui.get_inputs(list_labels, 'New Value:')
            new_row.insert(0, table[i][0])
            for item in range(len(table[i]) - 1):
                if list_labels[count] != '':
                    table[i][count] = new_row[count]
                count += 1
        i += 1
    print(table)
    return table

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    manufacture_dict = {}

    for i in table:
        if i[2] not in manufacture_dict:
            manufacture_dict[i[2]] = 1
        elif i[2] in manufacture_dict:
            manufacture_dict[i[2]] += 1

    ui.print_result(manufacture_dict, 'Games by manufacture')
    return manufacture_dict
    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    inputs = ui.get_inputs(['Enter the manufacture'], '')
    choosen_manufacture = inputs[0]
    if choosen_manufacture not in manufacturer:
        ui.print_error_message('Manufacture is not in list')
    else:
        list_of_stock_items = [int(record[4]) for record in table if record[2] == choosen_manufacture]
        sum_items = 0
        for i in list_of_stock_items:
            sum_items += i
        average = sum_items / len(list_of_stock_items)
        return average

    pass
