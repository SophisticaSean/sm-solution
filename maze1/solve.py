import os, time, random
from collections import OrderedDict
def can_move(coords, mazelines):
    position = coords[0]
    index = coords[1]
    temp_arr = []
    try:
        if mazelines[index - 1][position] != "X":
            temp_arr.extend([["N", position, (index - 1)]])
    except:
        pass
    try:
        if mazelines[index + 1][position] != "X":
            temp_arr.extend([["S", position, (index + 1)]])
    except:
        pass
    try:
        if mazelines[index][position - 1] != "X":
            temp_arr.extend([["W", (position - 1), index]])
    except:
        pass
    try:
        if mazelines[index][position + 1] != "X":
            temp_arr.extend([["E", (position + 1), index]])
    except:
        pass
    return temp_arr

def where_to(s_coord, f_coord):
    # x value
    x_diff = (f_coord[0] - s_coord[0])
    # y value
    y_diff = (f_coord[1] - s_coord[1])
    return [x_diff, y_diff]

def closer(old_where, new_where):
    if (new_where[0] >= old_where[0]) or (new_where[1] >= old_where[1]):
        return True
    else:
        return False

def coords_arr(inst_arr):
    return [inst_arr[1], inst_arr[2]]

def choose_direction(current_coords, f_coords, options, step, preferred_direction = None):
    adj_current = coords_arr(current_coords)
    target = where_to(adj_current, f_coords)

    if target[0] > 0:
        preferred_direction = "E"
    if target[0] < 0:
        preferred_direction = "W"
    if target[1] > 0:
        preferred_direction = "S"
    if target[1] < 0:
        preferred_direction = "N"
    if preferred_direction == None:
        return random.choice(options)
    else:
        if len(can_move(adj_current, mazelines)) >= 3:
            for item in options:
                if item[0] == preferred_direction:
                    if step >= 3 and item == some_set[step - 2]:
                        print item
                    else:
                        return item
        else:
            for item in options:
                if item in some_set.values():
                    print item
                else:
                    return item
        return random.choice(options)

def replay(instructions, mazelines):
    for i in range(len(instructions)):
        temp_coords = coords_arr(instructions[i])
        frame(temp_coords, mazelines)

def frame(temp_coords, mazelines):
    print temp_coords
    for num in reversed(range(1, 11)):
        print mazelines[temp_coords[1] - num]

    current_line = list(mazelines[temp_coords[1]])
    current_line[temp_coords[0]] = "@"
    print "".join(current_line)

    for num in range(1, 21):
        print mazelines[temp_coords[1] + num]
    time.sleep(0.05)
    os.system('clear')






maze = open("1a.in", "r")
mazelines = maze.readlines()
line_len = len(mazelines[0])
mazestring = str(mazelines)
inst = ""
for index, line in enumerate(mazelines):
    if "S" in line:
        print line
        s_coord = [line.index("S"), index]
        coolstuff = can_move([line.index("S"), index], mazelines)
    if "F" in line:
        f_coord = [line.index("F"), index]

print coolstuff
solution = {}
temp_coords = coolstuff[0]
step = 0
old_where = where_to(s_coord, f_coord)
some_set = {}
old_value = s_coord
preferred_direction = None

complete_set = []
runs = 1

finished = False
while runs != 0:
    for index, line in enumerate(mazelines):
        if "S" in line:
            s_coord = [line.index("S"), index]
            coolstuff = can_move([line.index("S"), index], mazelines)
        if "F" in line:
            f_coord = [line.index("F"), index]
    solution = {}
    temp_coords = coolstuff[0]
    step = 0
    old_where = where_to(s_coord, f_coord)
    some_set = {}
    old_value = s_coord
    preferred_direction = None
    while finished == False:
        close_arr = []
        for i in coolstuff:
            temp_close = closer(old_value, [i[1], i[2]])
            if temp_close == True:
                close_arr.append(i)
            old_value = [i[1], i[2]]

        temp_coords = choose_direction(temp_coords, f_coord, close_arr, step)

        coolstuff = can_move(coords_arr(temp_coords), mazelines)
        print coolstuff

        some_set[step] = temp_coords
        if f_coord == [temp_coords[1], temp_coords[2]]:
            print len(some_set)
            runs = runs - 1
            complete_set.append(some_set)
            print runs
            finished = True
        if step > 800:
            finished = True
        if f_coord[0] == temp_coords[1]:
            preferred_direction = "S"

        chords = coords_arr(temp_coords)
        #frame([temp_coords[1], temp_coords[2]], mazelines)
        step = step + 1
        print step, where_to([temp_coords[1], temp_coords[2]], f_coord)
    finished = False
best_array = []
for i in complete_set:
    best_array.append(len(i))
best_array.sort()
#print best_array
#print complete_set[0]
replay(complete_set[0], mazelines)
print len(complete_set[0])
print best_array
