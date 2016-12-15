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

    while True:
        ui.print_menu('Store menu', options, 'Back to main menu')

        inputs = ui.get_inputs(['Enter the number'], '')
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_to_remove = ui.get_inputs(['Enter id to remove: '], '')
            if common.is_this_record_exist(table, id_to_remove):
                remove(table, id_to_remove)
        elif option == "4":
            try:
                id_to_update = ui.get_inputs(['Enter id to update'], '')
                update(table, id_to_update)
            except ValueError as msg:
                ui.print_error_message(msg)
        elif option == "5":
            manufacture_dict = get_counts_by_manufacturers(table)
            ui.print_result(manufacture_dict, 'Games by manufacture')
        elif option == "6":
            inputs = ui.get_inputs(['Enter the manufacture'], '')
            manufacturer = inputs[0]
            average = get_average_by_manufacturer(table, manufacturer)
            ui.print_result(str(average), 'Average: ')
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
    title_list = ['Title',
                  'Manufacturer',
                  'Price',
                  'In_stock']

    common.add_to_table(table, title_list)

    return table
    pass


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """
    table = common.remove_record_from_table(table, id_)

    return table
    pass


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

    common.update_table(table, id_, list_labels)
    return table
    pass


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    """
    Counts games by manufacture, assign it to dictionary { [manufacturer] : [count] }

    Args:
        table: list in which we got manufacture of games

    Return:
        dictionary with name of manufacture and count

    """
    manufacture_dict = {}

    for i in table:
        if i[2] not in manufacture_dict:
            manufacture_dict[i[2]] = 1
        elif i[2] in manufacture_dict:
            manufacture_dict[i[2]] += 1

    return manufacture_dict
    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    """
    Function gets average amount of games in stock of given manufacture

    Args:
        table: list in which we have all manufacture and games in stock
        manufacturer = input with name of manufacture 

    Return:
        the average amount of games in stock counted by manufacture
    """

    manufacturer_list = []
    for i in table:
        if i[2] not in manufacturer_list:
            manufacturer_list.append(i[2])
    if manufacturer not in manufacturer_list:
        ui.print_error_message('Manufacture is not in list')
    else:
        list_of_stock_items = [int(record[4]) for record in table if record[2] == manufacturer]
        sum_items = 0
        for i in list_of_stock_items:
            sum_items += i
        average = sum_items / len(list_of_stock_items)
        return average

    pass
