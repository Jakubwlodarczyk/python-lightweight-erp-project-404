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
    module_data_file = 'crm/customers.csv'

    table = data_manager.get_table_from_file(module_data_file)
    options = ["Show customer table",
               "Add to customer list",
               "Remove from customer list",
               "Update customer list",
               "What is the id of the customer with the longest name?" ,
               "Which customers has subscribed to the newsletter?"]



    while True:
        ui.print_menu("Inventory menu", options, 'Back to main')
        option = ui.get_inputs(['Enter the number'], '')[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            id_ = ui.get_inputs(["ID: "], "Please provide ID of record to remove")
            if common.is_this_record_exist(table, id_):
                table = remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please provide ID of record to update")
            if common.is_this_record_exist(table, id_):
                table = update(table, id_)
        elif option == "5":
            ui.print_result(get_longest_name_id(table), "Longest customer name ID")
        elif option == "6":
            ui.print_result(get_subscribed_emails(table), "Subscribers")
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

    title_list = ["ID", "Name", "e-mail", "Newsletter subsciber?"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    label_list = ["Name", "e-mail", "Newsletter subsciber? (0 for 'yes', 1 for 'no')"]

    type_list = ['str',
                 'e-mail',
                 'bool']
    table = common.add_to_table(table, label_list, type_list)
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
