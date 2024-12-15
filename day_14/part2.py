import re

ROOM_WIDTH = 101
ROOM_HEIGHT = 103
number_pattern = r"-?\d+"
robots = []


def parse_file():
    with open("day_14/input.txt", "r") as f:
        for line in f:
            numbers = re.findall(number_pattern, line)
            new_robot = {
                "py": int(numbers[1]),
                "px": int(numbers[0]),
                "vy": int(numbers[3]),
                "vx": int(numbers[2]),
            }
            robots.append(new_robot)


def move_robots(robots, seconds):
    for robot in robots:
        new_x = (robot["px"] + robot["vx"] * seconds) % ROOM_WIDTH
        new_y = (robot["py"] + robot["vy"] * seconds) % ROOM_HEIGHT
        robot["px"] = new_x
        robot["py"] = new_y


def make_grid(robots):
    grid = [["."] * ROOM_WIDTH for _ in range(ROOM_HEIGHT)]
    for robot in robots:
        grid[robot["py"]][robot["px"]] = "1"
    return grid


def has_long_consecutive_line(grid, long_threshold):
    largest_consecutive = 0
    for row in grid:
        consecutive = 0
        for i in range(len(row)):
            consecutive = consecutive + 1 if row[i] == "1" else 0
            largest_consecutive = max(largest_consecutive, consecutive)
    return largest_consecutive >= long_threshold


def display_robots(grid):
    for row in grid:
        print(row)


parse_file()

time = 1
while True:
    move_robots(robots, 1)
    grid = make_grid(robots)
    if has_long_consecutive_line(grid, 15):
        display_robots(grid)
        print(f"TIME = {time}")
        break
    time += 1

    if time % 1000 == 0:
        print(f"Time elapsed: {time}")
