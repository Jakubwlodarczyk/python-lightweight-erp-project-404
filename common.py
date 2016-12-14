# implement commonly used functions here

import random
import ui

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    generated = ''
    is_unique = False
    id_table = []
    for row in table:
        id_table.append(row[0])

    while not is_unique:
        is_unique = True
        for i in range(2):
            generated += str(special_chars[random.randint(0, len(special_chars)-1)])
            generated += str(digits[random.randint(0, len(digits)-1)])
            generated += str(alphabet[random.randint(0, len(alphabet)-1)])
            generated += str(alphabet[random.randint(0, len(alphabet)-1)].upper())
        if generated in id_table:
            is_unique = False

    return generated


def mean_from_list(num_list):
    num_sum = 0
    for num in num_list: #making sum of number in list
        num_sum += int(num)
    mean = num_sum / len(num_list) #dividing by
    if mean.is_integer():
        mean = int(mean)
    return mean


def is_this_record_exist(table, id_):
    """
    Checking if user input id exist in your table

    Args:
        table: your table
        id_: user input id to check

    Returns:
        True if this record exist, then you can use your function update or remove
        False if record not exitst and print error message

    Example usage:
        if common.is_this_record_exist(table, id_[0]):
            table = update(table, id_[0])
    """
    if id_ not in [record[0] for record in table]:
        ui.print_error_message("Record with this ID not found")
        return False
    return True


def remove_record_from_table(table, id_):
    """
    Remove record from your table by ID.
    Important! Before you use this function check
    if given ID exist in your table by using is_this_record_exist function.

    Args:
        table: your table
        id_: user input id to remove

    Returns:
        Table with removed record
    """
    i = 0
    while i < len(table):
        if id_ == table[i][0]:
            del table[i]
            return table
        i += 1


def add_to_table(table, title_list):
    new_row = ui.get_inputs(title_list, 'What you wanna to add?')
    new_id = generate_random(table)
    new_row.insert(0, new_id)
    table.append(new_row)
    return table


def update_table(table, id_, title_list):
    id_exist = False
    try:
        for record in table:
            if record[0] == id_[0]:
                id_exist = True
                new_row = ui.get_inputs(title_list, 'New Value:')
                count = 1
                for data in new_row:
                    if data == '':
                        count += 1
                    else:
                        record[count] = data
                        count += 1

        if id_exist == False:
            raise ValueError('no record of that id')
    except ValueError as msg:
        ui.print_error_message(msg)

    return table

def modules_functions_to_dict(module_name):
    """function returns dict where are basic functions for all modules assigned to number inputted by user"""
    function_dict = {"1": "show_table(table)",
                     "2": "add(table)" } #function to call only - not needed any input

    input_rem_upd_label_word_dict = {"inventory": "item",
                                           "crm": "customer"} #module-depend word to use in input label

    input_needed_function_dict = {"3": ("remove(table, id_)", ["Enter " + input_rem_upd_label_word_dict[module_name] + " to remove it: "]),
                                  "4": ("update(table, id_)", ["Enter " + input_rem_upd_label_word_dict[module_name] + " to update it: "])}
    #special functions of each names and result labels - stored as list (module-depend)
    specials_functions_dict = {"inventory": {"5": ["get_available_items(table)", "Avaiable items:"],
                                             "6": ["get_average_durability_by_manufacturers(table)", "Average durability for manufacurers"]},
                                     "crm": {"5": ["get_longest_name_id(table)", "The longest name id"],
                                             "6": ["get_subscribed_emails(table)", "Subscribers"]} }
    #merge 3 dicts to one dict to return in two steps:
    function_dict.update(input_needed_function_dict)
    function_dict.update(specials_functions_dict[module_name])
    return function_dict




def modules_menu_title(module_name):
    """function returns string with module menu title"""
    menu_title_dict = {"inventory": "Inventory menu", "crm": "CRM menu"}
    return menu_title_dict[module_name]


def modules_options(module_name):
    """function returns list with module options names (labels)"""
    modules_options_dict = {"inventory": ["Show inventory table", "Add to inventory", "Remove from inventory", "Update inventory",
                                            "Which items have not exceeded their durability yet?",
                                            "What are the average durability times for each manufacturer?"],
                                  "crm": ["Show CRM table", "Add to CRM", "Remove from CRM", "Update CRM",
                                            "What is the id of the customer with the longest name?",
                                            "Which customers has subscribed to the newsletter?"] }
    return modules_options_dict[module_name]


def modules_table_first_row(module_name):
    """function returns list with table titles (first row) connected to specific module"""
    modules_table_first_row_dict = {"inventory": ["Id", "Inventory item", "Manufacturer", "Purchase date", "Durability"],
                                          "crm": ["Id", "Customer name", "e-mail", "Is subscriber"] }
    return modules_table_first_row_dict[module_name]
