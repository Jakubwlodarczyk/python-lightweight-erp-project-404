# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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

    table = data_manager.get_table_from_file('sales/sales_test.csv')
    options = ["Show Sales",
               "Add item",
               "Remove item",
               "Update item",
               "Show item id sold with lowest price",
               "Items which are sold between two given dates"]

    while True:
        ui.print_menu('Sales menu', options, 'Back to main menu')
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_ = get_id(table)
            remove(table, id_)
        elif option == "4":
            id_ = get_id(table)
            update(table, id_)
        elif option == "5":
            get_lowest_price_item_id(table)
        elif option == "6":
            inputs = get_dates()
            year_from = inputs[0]
            month_from = inputs[1]
            day_from = inputs[2]
            year_to = inputs[3]
            month_to = inputs[4]
            day_to = inputs[5]
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    user_input = ["Title", "Price", "Month", "Day", "Year"]
    title = "Please input required data"
    is_correct_input = False
    while not is_correct_input:
        inputs = ui.get_inputs(user_input, title)
        try:
            test = int(inputs[1]) + int(inputs[2]) + int(inputs[3]) + int(inputs[4])
        except ValueError:
            ui.print_error_message("Incorect input. Please try again.")
            continue
        if int(inputs[2]) > 12 or int(inputs[3]) > 31 or int(inputs[4]) > 2100:
            ui.print_error_message("Incorect date. Please try again.")
            continue
        is_correct_input = True
    id_ = common.generate_random(table)
    inputs.insert(0, id_)
    table.append(inputs)
    return table


def get_id(table):
    id_table = []
    for row in table:
        id_table.append(row[0])
    user_input = ["Id"]
    title = "Please input ID"
    is_correct_input = False
    while not is_correct_input:
        inputs = ui.get_inputs(user_input, title)
        if not inputs[0] in id_table:
            ui.print_error_message("Incorect input. Please try again.")
            continue
        is_correct_input = True
    return inputs[0]


def find_index_table(table, id_):
    for index, row in enumerate(table):
        if row[0] == id_:
            return index


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    index = find_index_table(table, id_)
    del table[index]
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
    index = find_index_table(table, id_)
    user_input = ["Title", "Price", "Month", "Day", "Year"]
    title = "Please input required data"
    is_correct_input = False
    while not is_correct_input:
        inputs = ui.get_inputs(user_input, title)
        try:
            test = int(inputs[1]) + int(inputs[2]) + int(inputs[3]) + int(inputs[4])
        except ValueError:
            ui.print_error_message("Incorect input. Please try again.")
            continue
        if int(inputs[2]) > 12 or int(inputs[3]) > 31 or int(inputs[4]) > 2100:
            ui.print_error_message("Incorect date. Please try again.")
            continue
        is_correct_input = True
    inputs.insert(0, id_)
    del table[index]
    table.insert(index, inputs)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    price_table = []
    for row in table:
        price_table.append(row[2])
    min_price = min(price_table)
    for index, row in enumerate(table):
        if row[2] == min_price:
            return table[index][0]


def get_dates():
    user_input = ["Year from", "Month from", "Day from", "Year to", "Month to", "Day to"]
    title = "Please input required data"
    is_correct_input = False
    while not is_correct_input:
        inputs = ui.get_inputs(user_input, title)
        try:
            test = int(inputs[0]) + int(inputs[1]) + int(inputs[2]) + int(inputs[3]), + int(inputs[4]) + int(inputs[5])
        except ValueError:
            ui.print_error_message("Incorect input. Please try again.")
            continue
        if int(inputs[0]) > 2100 or int(inputs[3]) > 2100 or int(inputs[2]) > 31 or int(inputs[5]) > 31 or int(inputs[1]) > 12 or int(inputs[4]) > 12:
            ui.print_error_message("Incorect date. Please try again.")
            continue
        is_correct_input = True
    return inputs

# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    table_output = []
    sum_of_input_from = int(year_from) * 365 + int(month_from) * 12 + int(day_from)
    sum_of_input_to = int(year_to) * 365 + int(month_to) * 12 + int(day_to)
    for row in table:
        sum_of_table = int(row[5]) * 365 + int(row[3]) * 12 + int(row[4])
        if sum_of_table > sum_of_input_from:
            if sum_of_table < sum_of_input_to:
                table_output.append(row)
    title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
    #ui.print_table(table_output, title_list)
    for row in table_output:
        row[2], row[5], row[3], row[4] = int(row[2]), int(row[5]), int(row[3]), int(row[4])
    return table_output
