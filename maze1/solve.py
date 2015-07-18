import os, time

def can_move(position, index, mazelines):
    temp_arr = []
    if mazelines[index - 1][position] != "X":
        temp_arr.extend([["N", (index - 1), position]])
    if mazelines[index + 1][position] != "X":
        temp_arr.extend([["S", (index + 1), position]])
    if mazelines[index][position - 1] != "X":
        temp_arr.extend([["W", index, (position - 1)]])
    if mazelines[index][position + 1] != "X":
        temp_arr.extend([["E", index, (position + 1)]])
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



maze = open("1.in", "r")
mazelines = maze.readlines()
line_len = len(mazelines[0])
mazestring = str(mazelines)
inst = ""
for index, line in enumerate(mazelines):
    if "S" in line:
        print line
        s_coord = [line.index("S"), index]
        coolstuff = can_move(line.index("S"), index, mazelines)
    if "F" in line:
        f_coord = [line.index("F"), index]

print coolstuff
solution = {}
temp_coords = coolstuff[0]
step = 0
old_where = where_to(s_coord, f_coord)
while "F" in mazestring:
    if closer(old_where, where_to([temp_coords[1], temp_coords[2]], f_coord)):
        temp_coords = can_move(temp_coords[1], temp_coords[2], mazelines)[1]
    else:
        temp_coords = can_move(temp_coords[1], temp_coords[2], mazelines)[0]
    magic = list(mazelines[temp_coords[2]])
    print magic[temp_coords[1]]
    magic[temp_coords[1]] = "X"
    mazelines[temp_coords[2]] = ''.join(magic)
    print mazelines[temp_coords[2]][temp_coords[1]]
    step = step + 1
    print temp_coords, step
    time.sleep(0.01)
    if step == 10:
        print mazelines
        time.sleep(10)
#print "F_coord: " + str(f_coord)
#print "S_coord: " + str(s_coord)
