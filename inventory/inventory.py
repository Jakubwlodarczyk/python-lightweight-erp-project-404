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

    # you code

    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


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
    aver_dur_dict = {}
    for item in table:
        if item[-3] in aver_dur_dict:
            aver_dur_dict[item[-3]].append(int(item[-1]))
        else:
            aver_dur_dict[item[-3]] = [item[-1]]
    print(aver_dur_dict)
    for manuf in aver_dur_dict:
        if len(aver_dur_dict[manuf]) != 1:

            aver_dur_dict[manuf] = [aver_dur_dict[manuf][i] + aver_dur_dict[manuf][i+1] for i in range(len(aver_dur_dict[manuf])-1)][0]/(len(aver_dur_dict[manuf]))
        else:
            aver_dur_dict[manuf] = aver_dur_dict[manuf][0]
    return aver_dur_dict
