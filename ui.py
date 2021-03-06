import common


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
    BOLD = '\033[1m'
    END = '\033[0m'
    print("\n" * 100)
    work_table = table[:]
    for row_index, row in enumerate(work_table):
        for col_index, col in enumerate(row):
            if type(col) == int:
                work_table[row_index][col_index] = str(col)
    work_table.insert(0, title_list)
    widths = [max(map(len, col)) for col in zip(*work_table)]
    sum_of_widths = common.sum_numbers(widths) + len(work_table[0]) * 2 + len(work_table[0]) - 1
    for index, row in enumerate(work_table):
        print("-" * sum_of_widths)
        if index == 0:
            print(BOLD, end="")
            print("|" + "  ".join((val.rjust(width) + "|" for val, width in zip(row, widths))))
            print(END, end="")
        else:
            print("|" + "  ".join((val.rjust(width) + "|" for val, width in zip(row, widths))))
    print("-" * sum_of_widths)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    if type(result) in [str, int]:  # result can be int too (needed to pass test), so this part works for 1-word result not depend on type
        print("{}: {}".format(label, result))
    if type(result) == list:
        print(label + ":")
        for res in result:
            print(str(res) + "\n")
    if type(result) == dict:
        print('\n\033[1m' + label + '\033[0m')
        for key, value in result.items():
            print('-' * 41)
            value = str(value)
            print('{} {}'.format(key.ljust(0), value.rjust(40 - len(key))))
        print('-' * 41, '\n')


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
    for i in range(len(list_options)):
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

    print(title)
    for item in list_labels:
        user_input = input(item + ' ').strip()
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
    print("Error:", message)
