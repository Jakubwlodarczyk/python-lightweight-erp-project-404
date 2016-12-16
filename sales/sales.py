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

    table = data_manager.get_table_from_file('sales/sales.csv')
    options = ["Show Sales",
               "Add item",
               "Remove item",
               "Update item",
               "Show item id sold with lowest price",
               "Items which are sold between two given dates"]

    while True:
        ui.print_menu('Sales menu', options, 'Back to main menu')
        option = ui.get_inputs(["Please enter a number: "], "")[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_ = ui.get_inputs(["ID: "], "Please provide ID of record to remove")
            if common.is_this_record_exist(table, id_):
                table = remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["ID: "], "Please provide ID of record to update")
            if common.is_this_record_exist(table, id_):
                table = update(table, id_)
        elif option == "5":
            ui.print_result(get_lowest_price_item_id(table), 'Item ID with lowest price')
        elif option == "6":
            title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
            inputs = get_input_for_sold_between()
            item_list = get_items_sold_between(table, inputs[1], inputs[2], inputs[0],
                                               inputs[4], inputs[5], inputs[3])
            if item_list:
                ui.print_table(item_list, title_list)
        elif option == "0":
            data_manager.write_table_to_file('sales/sales.csv', table)
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
    title_list = ["Title", "Price", "Month", "Day", "Year"]
    type_list = ["str", "int", "month", "day", "int"]
    table = common.add_to_table(table, title_list, type_list)
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
    table = common.remove_record_from_table(table, id_)
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
    title_list = ["Title", "Price", "Month", "Day", "Year"]
    type_list = ["str", "int", "month", "day", "int"]
    table = common.update_table(table, id_, title_list, type_list)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    """
    Search for lowest price item ID

    Args:
        table: list in which function will search for lowest price item ID

    Returns:
        Lowest price item ID
    """
    price_table = []
    for row in table:
        price_table.append(row[2])
    min_price = min(price_table)
    for index, row in enumerate(table):
        if row[2] == min_price:
            return table[index][0]


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Displays rows with items sold between two given dates

    Args:
        table: list of lists in which function will search for items
        year_from: year from start range
        month_from: month from start range
        day_from: day from start range
        year_to: year from end range
        month_to: month from end range
        day_to: day from end range

    Returns:
        Filtered list of lists with sold items between given dates
    """
    table_output = []
    sum_of_input_from = int(year_from) * 365 + int(month_from) * 12 + int(day_from)
    sum_of_input_to = int(year_to) * 365 + int(month_to) * 12 + int(day_to)
    for row in table:
        sum_of_table = int(row[5]) * 365 + int(row[3]) * 12 + int(row[4])
        if sum_of_table > sum_of_input_from:
            if sum_of_table < sum_of_input_to:
                table_output.append(row)
    if not table_output:
        ui.print_error_message("No items was sold between these dates.")
        return None
    #title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
    #ui.print_table(table_output, title_list)
    for row in table_output:  # switch data type, test requires it
        row[2], row[5], row[3], row[4] = int(row[2]), int(row[5]), int(row[3]), int(row[4])
    return table_output


def get_input_for_sold_between():
    """
    Provides input data for get_items_sold_between function

    Args:
        None

    Returns:
        list which contains dates for get_items_sold_between function purpose
    """
    title_list = ["Year from", "Month from", "Day from", "Year to", "Month to", "Day to"]
    title = "Please input desired time range"
    type_list = ["int", "month", "day", "int", "month", "day"]
    inputs = ui.get_inputs(title_list, title)
    inputs = common.validate(inputs, title_list, type_list)
    return inputs
