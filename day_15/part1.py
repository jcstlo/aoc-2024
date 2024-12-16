walls, boxes = set(), set()
movements = []
ROWS, COLS = 0, 0
robot_pos = (0, 0)


def parse_map() -> tuple[int, int]:
    global ROWS, COLS, robot_pos
    grid = []

    with open("day_15/input_map.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                walls.add((row, col))
            if grid[row][col] == "O":
                boxes.add((row, col))
            if grid[row][col] == "@":
                robot_pos = (row, col)

    ROWS, COLS = len(grid), len(grid[0])
    return


def print_map():
    global robot_pos
    grid = [["."] * COLS for _ in range(ROWS)]
    for wall in walls:
        grid[wall[0]][wall[1]] = "#"
    for box in boxes:
        grid[box[0]][box[1]] = "O"
    grid[robot_pos[0]][robot_pos[1]] = "@"

    for row in grid:
        print("".join(row))


def parse_movement():
    with open("day_15/input_movement.txt", "r") as f:
        for line in f:
            for char in line.strip():
                movements.append(char)


def calculate_next_pos(position, movement):
    if movement == "^":
        return (position[0] - 1, position[1])
    if movement == "v":
        return (position[0] + 1, position[1])
    if movement == ">":
        return (position[0], position[1] + 1)
    if movement == "<":
        return (position[0], position[1] - 1)
    return "ERROR"


def perform_movement(robot_position, movement):
    def try_to_move_box(box_position, movement):
        next_pos = calculate_next_pos(box_position, movement)

        if next_pos in walls:
            return

        if next_pos in boxes:
            try_to_move_box(next_pos, movement)

        if next_pos not in boxes:
            boxes.remove(box_position)
            boxes.add(next_pos)
        return

    next_pos = calculate_next_pos(robot_position, movement)

    if next_pos in walls:
        return robot_position

    if next_pos in boxes:
        try_to_move_box(next_pos, movement)

    if next_pos not in boxes:
        return next_pos
    return robot_position


def calculate_sum_of_gps_coords():
    sum = 0
    for box in boxes:
        sum += 100 * box[0] + box[1]
    return sum


parse_map()
parse_movement()

for movement in movements:
    robot_pos = perform_movement(robot_pos, movement)

print(f"Sum = {calculate_sum_of_gps_coords()}")
