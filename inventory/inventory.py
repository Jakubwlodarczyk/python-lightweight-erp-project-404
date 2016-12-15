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
    module_data_file = 'inventory/inventory.csv'


    table = data_manager.get_table_from_file(module_data_file)
    #menu_title = modules_menu_title(module_name)
    #options = modules_options(module_name)
    functions_dict = {"1": (show_table, "Show inventory table", "exec_only"),
                      "2": (add, "Add to inventory"),
                      "3": (remove, "Remove from inventory"),
                      "4": (update, "Update inventory"),
                      "5": (get_available_items, "Which items have not exceeded their durability yet?"),
                      "6": (get_average_durability_by_manufacturers, "What are the average durability times for each manufacturer?")}

    options = [""]*len(functions_dict)
    for function in functions_dict:
        options[int(function)-1] = functions_dict[function][1]

    #while True:
    ui.print_menu("Inventory menu", options, 'Back to main')
    function_choice = ui.get_inputs(["Please enter a number: "], "")[0]
    if function_choice in functions_dict:
        if functions_dict[function_choice] == "1":

            print("asdf")
    #         if functions_dict[function_choice][-1] == "input_needed":
    #             id_ = ui.get_inputs(functions_dict[function_choice][1], "")[0]
    #             exec(functions_dict[function_choice][0])
    #         if functions_dict[function_choice][-1] == "special":
    #             special_function_result = eval(functions_dict[function_choice][0])
    #             ui.print_result(special_function_result, functions_dict[function_choice][1])
    #         if functions_dict[function_choice][-1] == "special_with_input":
    #             question = ui.get_inputs(functions_dict[function_choice][1], "")[0]
    #             special_function_result = eval(functions_dict[function_choice][0])
    #             ui.print_result(special_function_result, functions_dict[function_choice][1])
    #
    #
    #     elif function_choice == "0":
    #         data_manager.get_table_from_file(module_data_file)
    #         return None
    #     else:
    #         ui.print_error_message("Choose correct number")
    #


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


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    import datetime
    for i in range(len(table)):
        table[i][-1] = int(table[i][-1])
        table[i][-2] = int(table[i][-2])
    return list(filter(lambda x: (x[-1])+(x[-2]) >= datetime.date.today().year, table))


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
