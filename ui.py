def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    table.insert(0, title_list)
    columns_max_lenght = [0 for x in range(len(table[0]))]
    for row_index, row in enumerate(table):
        for col_index, col in enumerate(row):
            if columns_max_lenght[col_index] < len(col):
                columns_max_lenght[col_index] = len(col)
    s = [[str(e) for e in row] for row in table]
    to_format = '  '.join('{{:{}}}'.format(x) for x in columns_max_lenght)
    table = [to_format.format(*row) for row in s]
    sum_of_col = sum(columns_max_lenght)
    for item in table:
        print("-"*(sum_of_col+len(columns_max_lenght)*2))
        print(item)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    if type(result) == string:
        print("{}: {}".format(label, result))
    if type(result) == list:
        print(label + ":")
        for res in result:

            print(str(res) + "\n")
    if type(result) == dict:
        print(label + ":")
        for item, value in result:
            print("{}: {}".format(item, value))


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(title + ':')
    for i in range(len(list_options) - 1):
        print('  ({}) {}'.format(i + 1, list_options[i]))
    print('  (0) ' + exit_message)

    pass


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code
    print(title)
    for item in list_labels:
        user_input = input(item + ' ')
        inputs.append(user_input)

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print("Error: ", message)
