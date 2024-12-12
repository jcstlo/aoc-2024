obstacles = set()

row = 0
start_pos = (0, 0, "UP")
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
                start_pos = (row, col, "UP")
        row += 1
    HEIGHT = row

up, down, left, right = [-1, 0], [1, 0], [0, -1], [0, 1]


def check_if_guard_in_loop() -> bool:
    # returns True if guard gets stuck in loop
    # returns False if guard is not stuck in a loop
    visited = set()
    curr_pos = start_pos
    curr_dir = direction
    while curr_pos[0] in range(HEIGHT) and curr_pos[1] in range(WIDTH):
        if curr_pos in visited:
            return True

        visited.add(curr_pos)
        next_pos = (0, 0)

        # calculate next position
        if curr_dir == "UP":
            next_pos = (curr_pos[0] + up[0], curr_pos[1] + up[1])
        elif curr_dir == "RIGHT":
            next_pos = (curr_pos[0] + right[0], curr_pos[1] + right[1])
        elif curr_dir == "DOWN":
            next_pos = (curr_pos[0] + down[0], curr_pos[1] + down[1])
        elif curr_dir == "LEFT":
            next_pos = (curr_pos[0] + left[0], curr_pos[1] + left[1])
        else:
            print("ERROR")

        # change direction if next position is an obstacle
        if next_pos in obstacles:
            if curr_dir == "UP":
                curr_dir = "RIGHT"
            elif curr_dir == "RIGHT":
                curr_dir = "DOWN"
            elif curr_dir == "DOWN":
                curr_dir = "LEFT"
            elif curr_dir == "LEFT":
                curr_dir = "UP"
            else:
                print("ERROR")
            curr_pos = (curr_pos[0], curr_pos[1], curr_dir)
        else:
            curr_pos = (next_pos[0], next_pos[1], curr_dir)

    return False


possible_obstructions = 0
# add obstructions through brute force and check each one
for i in range(HEIGHT):
    for j in range(WIDTH):
        # skip places we aren't allowed to add an obstruction
        if (i, j) in obstacles or (i, j, "UP") == start_pos:
            continue

        # add an obstruction
        obstacles.add((i, j))
        print(f"Trying obstacle at ({i}, {j})")

        if check_if_guard_in_loop():
            possible_obstructions += 1
            print(
                f"Obstruction found! Total valid obstructions = {possible_obstructions}"
            )
        else:
            print("Invalid obstruction.")

        # remove obstruction for next iteration
        obstacles.remove((i, j))

print(possible_obstructions)
