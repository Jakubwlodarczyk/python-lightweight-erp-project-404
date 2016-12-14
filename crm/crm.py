# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

    module_name = "crm"
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    menu_title = common.modules_menu_title(module_name)
    options = common.modules_options(module_name)
    functions_dict = common.modules_functions_to_dict(module_name)

    while True:
        ui.print_menu(menu_title, options, 'Back to main')
        function_choice = ui.get_inputs(["Please enter a number: "], "")[0]
        if function_choice in functions_dict:
            if type(functions_dict[function_choice]) != tuple: #functions without input
                exec(functions_dict[function_choice])
            elif len(functions_dict[function_choice]) > 1: #functions with input
                id_ = ui.get_inputs(functions_dict[function_choice][1], "")[0]
                exec(functions_dict[function_choice][0])
        elif function_choice == "0":
            data_manager.write_table_to_file('inventory/inventory.csv', table)
            return None
        else:
            ui.print_error_message("Choose correct number")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = common.modules_table_first_row("crm")
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

    return table


def input_prep(table, function):
    function_dict = {"remove": "remove(table, inputted)", "update": "update(table, inputted)"}
    text_dict = {"remove": "Enter id to remove:", "update": "Enter id to remove:"  }
    inputted =  ui.get_inputs([text_dict[function]], '')[0]
    table = eval(function_dict[function])

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

    # your code

    return table


# special functions:
# ------------------
def special_function(table, function_num):

    function_dict = common.modules_special_functions("crm")
    function_label = common.modules_special_functions_labels("crm")
    special_function_result = eval(function_dict[function_num])
    ui.print_result(special_function_result, function_label[function_num])

# special functions:

# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):
    result_list = []
    for customer in table:
        result_list.append([len(customer[1]),customer[0],customer[1]])

    max_length = (max(result_list))[0]

    result = list(filter(lambda x: x[0] == max_length, result_list))
    result = min(result, key = lambda x: x[2])

    return result[1]

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    subscribers_list = []
    for customer in table:
        if int(customer[-1]) == 1:
            subscribers_list.append(customer[-2] + ";" + customer[1])
    return subscribers_list
