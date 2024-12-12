visited = set()
obstacles = set()

row = 0
curr_pos = (0, 0)
direction = "UP"
WIDTH, HEIGHT = 0, 0

# parse input
with open("day_06/input.txt", "r") as f:
    for line in f:
        line_list = list(line.strip())
        WIDTH = len(line_list)
        for col in range(len(line_list)):
            if line_list[col] == "#":
                obstacles.add((row, col))
            if line_list[col] == "^":
                curr_pos = (row, col)
        row += 1
    HEIGHT = row

up, down, left, right = [-1, 0], [1, 0], [0, -1], [0, 1]

while curr_pos[0] in range(HEIGHT) and curr_pos[1] in range(WIDTH):
    visited.add(curr_pos)
    next_pos = (0, 0)

    # calculate next position
    if direction == "UP":
        next_pos = (curr_pos[0] + up[0], curr_pos[1] + up[1])
    elif direction == "RIGHT":
        next_pos = (curr_pos[0] + right[0], curr_pos[1] + right[1])
    elif direction == "DOWN":
        next_pos = (curr_pos[0] + down[0], curr_pos[1] + down[1])
    elif direction == "LEFT":
        next_pos = (curr_pos[0] + left[0], curr_pos[1] + left[1])
    else:
        print("ERROR")

    # change direction if next position is an obstacle
    if next_pos in obstacles:
        if direction == "UP":
            direction = "RIGHT"
        elif direction == "RIGHT":
            direction = "DOWN"
        elif direction == "DOWN":
            direction = "LEFT"
        elif direction == "LEFT":
            direction = "UP"
        else:
            print("ERROR")
    else:
        curr_pos = next_pos

print(len(visited))
