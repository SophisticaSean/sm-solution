import os, time, random

def can_move(position, index, mazelines):
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
    print old_where, new_where
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
some_set = {}
old_value = s_coord
while "F" in mazestring:
    close_arr = []
    for i in coolstuff:
        temp_close = closer(old_value, [i[1], i[2]])
        if temp_close == True:
            close_arr.append(i)
        old_value = [i[1], i[2]]
    temp_coords = random.choice(close_arr)
        #while temp_coords in some_set.values():
            #temp_coords = random.choice(close_arr)
    coolstuff = can_move(temp_coords[1], temp_coords[2], mazelines)
    print coolstuff

    #if :
        #temp_coords = can_move(temp_coords[1], temp_coords[2], mazelines)[1]
    #else:
    #temp_coords = random.choice(can_move(temp_coords[1], temp_coords[2], mazelines))
    #magic = list(mazelines[temp_coords[2]])
    #magic[temp_coords[1]] = "X"
    #mazelines[temp_coords[2]] = ''.join(magic)
    if temp_coords not in some_set.values():
        some_set[step] = temp_coords
    if f_coord == [temp_coords[1], temp_coords[2]]:
        print str(some_set)
        time.sleep(100)
    if f_coord[0] == temp_coords[1]:
        time.sleep(10)
    #print f_coord, [temp_coords[1], temp_coords[2]]
    step = step + 1
    print step, where_to([temp_coords[1], temp_coords[2]], f_coord)
    time.sleep(0.001)
#print "F_coord: " + str(f_coord)
#print "S_coord: " + str(s_coord)
