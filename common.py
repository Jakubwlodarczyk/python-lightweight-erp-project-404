# implement commonly used functions here

import random


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
        print(generated)
    return generated


def mean_from_list(num_list):
    num_sum = 0
    for num in num_list: #making sum of number in list
        num_sum += int(num)
    mean = num_sum / len(num_list) #dividing by
    if mean.is_integer():
        mean = int(mean)
    return mean


def modules_functions_to_dict(module_name):
    """function returns dict where are basic functions for all modules assigned to number inputted by user"""
    standard_function_dict = {"1": "show_table(table[:])", "2": "add(table)", "3": "input_prep(table, 'remove')", "4": "input_prep(table, 'update')", "5": "special_function(table, '1')", "6": "special_function(table, '2')" }
    final_function_dict = standard_function_dict
    #if in any module will be different order or for example more special function, standard dict can be modified in according to module_name
    return final_function_dict


def modules_special_functions(module_name):
    """function returns dict with special functions name, which are connected with specific module (switch by module_name)"""
    specials_in_modules_dict = {"inventory": {"1": "get_available_items(table)", "2": "get_average_durability_by_manufacturers(table)"},
                                "crm": {"1": "get_longest_name_id(table)", "2": "get_subscribed_emails(table)"} }
    return specials_in_modules_dict[module_name]

def modules_special_functions_labels(module_name):
    """function returns dict with special functions name, which are connected with specific module (switch by module_name)"""
    specials_in_modules_dict = {"inventory": {"1": "Avaiable items:", "2": "Average durabity for manufacurers"},
                                "crm": {"1": "The longest name id", "2": "Subscribers"} }
    return specials_in_modules_dict[module_name]


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
