walls, boxes = set(), set()  # box LEFT SIDE coordinates are tracked
movements = []
ROWS, COLS = 0, 0
robot_pos = (0, 0)


def parse_map() -> tuple[int, int]:
    global ROWS, COLS, robot_pos
    grid = []

    with open("day_15/input_map.txt", "r") as f:
        for line in f:
            wide_line = (
                line.strip()
                .replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            grid.append(list(wide_line))

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                walls.add((row, col))
            if grid[row][col] == "[":
                boxes.add((row, col))
            if grid[row][col] == "@":
                robot_pos = (row, col)

    ROWS, COLS = len(grid), len(grid[0])
    return


def parse_movement():
    with open("day_15/input_movement.txt", "r") as f:
        for line in f:
            for char in line.strip():
                movements.append(char)


def print_map():
    grid = [["."] * COLS for _ in range(ROWS)]
    for wall in walls:
        grid[wall[0]][wall[1]] = "#"
    for box in boxes:
        grid[box[0]][box[1]] = "["
        grid[box[0]][box[1] + 1] = "]"
    grid[robot_pos[0]][robot_pos[1]] = "@"

    for row in grid:
        print("".join(row))


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


def box_find_next_boxes(box_position, movement):
    if movement == "^":
        return [
            (box_position[0] - 1, box_position[1]),
            (box_position[0] - 1, box_position[1] - 1),
            (box_position[0] - 1, box_position[1] + 1),
        ]
    if movement == "v":
        return [
            (box_position[0] + 1, box_position[1]),
            (box_position[0] + 1, box_position[1] - 1),
            (box_position[0] + 1, box_position[1] + 1),
        ]
    if movement == ">":
        return [(box_position[0], box_position[1] + 2)]
    if movement == "<":
        return [(box_position[0], box_position[1] - 2)]
    return "ERROR"


def robot_find_next_boxes(robot_position, movement):
    if movement == "^":
        return [
            (robot_position[0] - 1, robot_position[1]),
            (robot_position[0] - 1, robot_position[1] - 1),
        ]
    if movement == "v":
        return [
            (robot_position[0] + 1, robot_position[1]),
            (robot_position[0] + 1, robot_position[1] - 1),
        ]
    if movement == ">":
        return [(robot_position[0], robot_position[1] + 1)]
    if movement == "<":
        return [(robot_position[0], robot_position[1] - 2)]
    return "ERROR"


def box_find_next_walls(box_position, movement):
    if movement == "^":
        return [
            (box_position[0] - 1, box_position[1]),
            (box_position[0] - 1, box_position[1] + 1),
        ]
    if movement == "v":
        return [
            (box_position[0] + 1, box_position[1]),
            (box_position[0] + 1, box_position[1] + 1),
        ]
    if movement == ">":
        return [(box_position[0], box_position[1] + 2)]
    if movement == "<":
        return [(box_position[0], box_position[1] - 1)]
    return "ERROR"


def robot_find_next_wall(robot_position, movement):
    if movement == "^":
        return (robot_position[0] - 1, robot_position[1])
    if movement == "v":
        return (robot_position[0] + 1, robot_position[1])
    if movement == ">":
        return (robot_position[0], robot_position[1] + 1)
    if movement == "<":
        return (robot_position[0], robot_position[1] - 1)
    return "ERROR"


def is_movement_possible(robot_position, movement):
    def dfs(box_position, movement):
        # return True if this box can be moved
        possible_walls = box_find_next_walls(box_position, movement)
        for wall in possible_walls:
            if wall in walls:
                # base case: there is a wall in front of this box
                return False

        result = True
        possible_boxes = box_find_next_boxes(box_position, movement)
        for box in possible_boxes:
            if box in boxes:
                # recursively check if other boxes can be moved
                result = result and dfs(box, movement)

        return result

    if robot_find_next_wall(robot_position, movement) in walls:
        return False

    result = True
    possible_robot_boxes = robot_find_next_boxes(robot_position, movement)
    for box in possible_robot_boxes:
        if box in boxes:
            result = result and dfs(box, movement)

    return result


def perform_movement(robot_position, movement):
    # NOTE: only call this method when is_movement_possible() returns True
    global robot_pos

    def move_box(box_position, movement):
        possible_boxes = box_find_next_boxes(box_position, movement)
        for box in possible_boxes:
            if box in boxes:
                move_box(box, movement)

        boxes.remove(box_position)
        boxes.add(calculate_next_pos(box_position, movement))

    possible_boxes = robot_find_next_boxes(robot_position, movement)
    for box in possible_boxes:
        if box in boxes:
            move_box(box, movement)

    robot_pos = calculate_next_pos(robot_pos, movement)


def calculate_sum_of_gps_coords():
    sum = 0
    for box in boxes:
        sum += 100 * box[0] + box[1]
    return sum


parse_map()
parse_movement()

for movement in movements:
    if is_movement_possible(robot_pos, movement):
        perform_movement(robot_pos, movement)

print(f"Sum = {calculate_sum_of_gps_coords()}")
