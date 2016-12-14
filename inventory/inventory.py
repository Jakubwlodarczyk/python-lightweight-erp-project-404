# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    #options = ['Show table', 'Add', 'Remove', 'Update', 'Question1', 'Question2']
    menu_title = common.modules_menu_title("inventory")
    options = common.modules_options("inventory")
    #inv_functions_dict = {"1": "show_table(table[:])", "2": "add(table)", "3": "input_prep(table, 'remove')", "4": "input_prep(table, 'update')", "5": "special_function(table, '1')", "6": "special_function(table, '2')" }
    inv_functions_dict = common.modules_functions_to_dict("inventory")
    menu = True
    while menu == True:
        ui.print_menu(menu_title, options, 'Back to main')
        function_choice = ui.get_inputs(["Please enter a number: "], "")[0]
        if function_choice in inv_functions_dict:
            exec(inv_functions_dict[function_choice])
            menu = False
        elif function_choice == "0":
            data_manager.write_table_to_file('accounting/items_test.csv', table)
            return None
        else:
            ui.print_error_message("Choose correct number")

    start_module()




def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    #title_list = ['id', 'month', 'day', 'year', 'type']
    title_list = common.modules_table_first_row("inventory") #common function
    ui.print_table(table, title_list)
    print("asdf")




def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    print("add add add")
    # your code

    return table

def input_prep(table, function):
    function_dict = {"remove": "remove(table, inputted)", "update": "update(table, inputted)"}
    text_dict = {"remove": "Enter id to remove:", "update": "Enter id to remove:"  }
    inputted =  ui.get_inputs([text_dict[function]], '')[0]
    exec(function_dict[function])

def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

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
    print("update" + id_)
    # your code

    return table

def special_function(table, function_num):

    function_dict = common.modules_special_functions("inventory")
    function_label = common.modules_special_function_label("inventory")
    special_function_result = eval(function_dict[function_num])
    ui.print_result(special_function_result, function_label[function_num])


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    import datetime
    return list(filter(lambda x: int(x[-1])+int(x[-2]) >= datetime.date.today().year, table))


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists

def get_average_durability_by_manufacturers(table):
    aver_durability_dict = {}
    for item in table:
        if item[-3] in aver_durability_dict:
            aver_durability_dict[item[-3]].append(int(item[-1]))
        else:
            aver_durability_dict[item[-3]] = [item[-1]]
    for manufacturer in aver_durability_dict:
        aver_durability_dict[manufacturer] = common.mean_from_list(aver_durability_dict[manufacturer])

    return aver_durability_dict
