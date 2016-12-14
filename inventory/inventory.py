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
    module_name = "inventory"
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    menu_title = common.modules_menu_title(module_name)
    options = common.modules_options(module_name)
    functions_dict = common.modules_functions_to_dict(module_name)

    while True:
        ui.print_menu(menu_title, options, 'Back to main')
        function_choice = ui.get_inputs(["Please enter a number: "], "")[0]
        if function_choice in functions_dict:
            if type(functions_dict[function_choice]) == list:
                if len(functions_dict[function_choice]) == 2:
                    special_function_result = eval(functions_dict[function_choice][0])
                    ui.print_result(special_function_result, functions_dict[function_choice][1])
            elif type(functions_dict[function_choice]) == tuple:
                id_ = ui.get_inputs(functions_dict[function_choice][1], "")[0]
                exec(functions_dict[function_choice][0])
            else:
                exec(functions_dict[function_choice])

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
    title_list = common.modules_table_first_row("inventory")
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    title_list = common.modules_table_first_row("inventory")
    table = common.add_to_table(table, title_list[1:])
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

    common.remove_record_from_table(table, id_)
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
    title_list = common.modules_table_first_row("inventory")
    common.update_table(table, id_, title_list)
    return table

def special_function(table, function_num):

    function_dict = common.modules_special_functions("inventory")
    function_label = common.modules_special_functions_labels("inventory")



# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    import datetime
    #table = list(map(lambda x: int(x[-1]) and int(x[-2]), table))
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
