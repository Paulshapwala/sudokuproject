import project_functions as pf

counter = 0
map_dict = pf.map_dict()

print('*' * 80)
print('SUDOKU PUZZLE')
print('*' * 80)

puzzle_list = []
puzzle, solution = pf.get_data()
for i in puzzle:
    puzzle_list.append(int(i))

puzzle_dict = dict(zip((p for p in range(1, 82)), puzzle_list))

index = 1
for value in map_dict:
    map_dict[value] = puzzle_dict[index]
    index += 1
pf.display(map_dict)

solution_dict = pf.grid_structure(solution)

print('*' * 80)
print('SOLUTION')
print('*' * 80)
pf.display(solution_dict)
squares = pf.create_squares(map_dict)
number = 1
numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
status = 0
loops = 0
while True:
    # checking for unknown variables:
    for key, value in map_dict.items():
        if value == 0:
            map_dict[key] = 10

    # square method algorithm:
    for key, value in map_dict.items():
        if value == number:
            row, column = key
            for j in range(1, 10):
                if map_dict[row, j] == 10:
                    map_dict[row, j] = 0
                if map_dict[j, column] == 10:
                    map_dict[j, column] = 0
            map_dict[row, column] = number
    # checking if a variable has been solved:
    for i in range(9):
        count = 0
        number_in = False
        for key in squares[i]:
            if map_dict[key] == 10:
                count += 1
            if map_dict[key] == number:
                number_in = True
                break
        if count == 1 and number_in is False:
            # go through the square and find the solved variable:
            for key in squares[i]:
                if map_dict[key] == 10:
                    map_dict[key] = number
        else:
            # reset everything to zero:
            for key in squares[i]:
                if map_dict[key] == 10:
                    map_dict[key] = 0
    #
    # # this code is for checking for squares with only one unknown
    # for i in range(9):
    #     box_count = 0
    #     for key in squares[i]:
    #         if map_dict[key] != 0:
    #             numbers_to_check.remove(map_dict[key])
    #         else:
    #             box_count += 1
    #         if box_count > 1:
    #             break
    #     if box_count == 1:
    #         for key in squares[i]:
    #             if map_dict[key] == 0:
    #                 rem = numbers_to_check[0]
    #                 map_dict[key] = rem
    #     numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # code to exit the loop
    if number < 9:
        number += 1
    else:
        for key, value in map_dict.items():
            if value == 0:
                number = 1
                loops += 1
                break
            else:
                status = 1
    if status == 1 or loops == 10000000000:
        break


print('*' * 80)
print('ALGORITHM RESULT')
print('*' * 80)
pf.display(map_dict)
