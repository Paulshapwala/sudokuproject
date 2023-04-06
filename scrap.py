import project_functions as pf
import pandas as pd
map_dict = pf.map_dict()
test_samples = pf.random_value()
puzzle_list = []
puzzle, solution = test_samples['quizzes'], test_samples['solutions']
print(puzzle)
for i in puzzle:
    puzzle = i

for i, in puzzle:
    puzzle_list.append(int(i))

puzzle_dict = dict(zip((p for p in range(1, 82)), puzzle_list))
print(puzzle_dict)

index = 1
for value in map_dict:
    map_dict[value] = puzzle_dict[index]
    index += 1
pf.display(map_dict)




