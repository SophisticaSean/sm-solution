import os

def can_move(index, position, mazelines):
    if mazelines[index - 1][position] != "X":
        print "N"
    if mazelines[index + 1][position] != "X":
        print "S"
    if mazelines[index][position - 1] != "X":
        print "W"
    if mazelines[index][position + 1] != "X":
        print "E"



maze = open("1.in", "r")
mazelines = maze.readlines()
line_len = len(mazelines[0])
mazestring = str(mazelines)
for index, line in enumerate(mazelines):
    if "S" in line:
        s_coord = [line.index("S"), index]
        can_move(index, line.index("S"), mazelines)
    if "F" in line:
        f_coord = [line.index("F"), index]
print "F_coord: " + str(f_coord)
print "S_coord: " + str(s_coord)
