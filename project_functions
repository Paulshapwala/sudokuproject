def get_data() -> list:
    """
    reads a csv file and returns and creates a dict
    it returns a random item from the dict given a certain range

    :return : a list with two elements, the puzzle and the solution
    """
    import csv
    import random
    random_int = random.randint(0, 10)
    # random_int = 2
    samples = {}
    source_path = 'C:/Users/shapz/Downloads/archive/sudoku.csv'
    with open(source_path) as sudoku:
        lines = csv.reader(sudoku)
        i = 0

        for line in lines:
            samples[i] = line
            i += 1
            if i >= random_int + 1:
                break

    test_sample = samples[random_int]
    return test_sample


def display(dict_param, i=1) -> None:
    """
    takes a dictionary and prints a 9 by 9 sudoku grid using the dict values
    :param dict_param: and dictionary with keys expressed as int values (i, j)
           therefore it accepts a dictionary created by map_dict()
    :param i: start value for the keys
    :return: no return
    """
    while True:
        for j in range(1, 10):
            print(f'{dict_param[i, j]} ', end='')
            if j == 3 or j == 6:
                print('| ', end='')
        print()
        if i == 3 or i == 6:
            print('_' * 21)
        i += 1
        if i == 10:
            break


def map_dict() -> dict:
    """
    creates a dictionary with keys given as (i, j)
    the key values basically allow for representation in
    cartesian coordinate system
    :return: the dictionary created
             all the values are initialized to 0
    """
    mapped_dict = {}
    row_main = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column_main = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in row_main:
        for j in column_main:
            mapped_dict[i, j] = 0
    return mapped_dict


def grid_structure(item: list) -> dict:
    """
    fills up the dictionary created by map_dict()
    with values from the csv file
    :param item: an iterable with 81 items
    :return: the filled up dictionary
    """
    grid = dict(zip((p for p in range(1, 82)), item))
    grid_dict = map_dict()
    index = 1
    for value in grid_dict:
        grid_dict[value] = grid[index]
        index += 1
    return grid_dict


def list_to_int(single_value: list):
    """
    unpacks a list with a single item
    :param single_value:
    :return:
    """
    if len(single_value) == 1:
        number = single_value[0]
        return number
    else:
        return single_value


def section_squares(squares):
    """
    takes a dictionary created by create_squares and
    creates 3 by 3 squares from 3 by 9 columns
    :param squares: dict created by create squares
    :return: a list of 81 items that are ordered into 3 by 3 squares
    note: slicing the list into nine items in order will give key
    values for 3 by 3 square items in a sudoku grid
    """
    squares_list = []
    for key, items in squares.items():
        square_1 = (items[0:9])
        squares_list.append(square_1)
        square_2 = (items[9:18])
        squares_list.append(square_2)
        square_3 = (items[18:])
        squares_list.append(square_3)
    return squares_list


def create_squares(grid_dict):
    """
    creates 3 by 9 column representations of
    a sudoku grid. Basically sections a 9 by 9 grid into 3 columns
    it then calls section_squares to create 3 by 3 squares from each
    of the columns. The values stored in the lists are keys created by grid_dict()
    :param grid_dict: must be a dictionary created by grid_dict()
    :return: a list that is ordered into 3 by 3 squares
    """
    dict_of_squares = {
        'list_1': [],
        'list_2': [],
        'list_3': [],
    }
    for key, value in grid_dict.items():
        row, column = key
        if column in [1, 2, 3]:
            dict_of_squares['list_1'].append(key)
        elif column in [4, 5, 6]:
            dict_of_squares['list_2'].append(key)
        else:
            dict_of_squares['list_3'].append(key)
    return section_squares(dict_of_squares)
