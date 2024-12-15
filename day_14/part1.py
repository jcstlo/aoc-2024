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


def calculate_safety_factor(robots):
    quadrants = [0] * 4
    HORIZONTAL_BORDER = int(ROOM_HEIGHT // 2)
    VERTICAL_BORDER = int(ROOM_WIDTH // 2)
    # [0] = top right, [1] = bottom right, [2] = bottom left, [3] = top left
    for robot in robots:
        if robot["px"] == VERTICAL_BORDER or robot["py"] == HORIZONTAL_BORDER:
            continue

        # determine which quadrant each robot is in
        if robot["px"] > VERTICAL_BORDER:
            if robot["py"] > HORIZONTAL_BORDER:
                quadrants[1] += 1
            else:
                quadrants[0] += 1
        else:
            if robot["py"] > HORIZONTAL_BORDER:
                quadrants[2] += 1
            else:
                quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


parse_file()
move_robots(robots, 100)
print(calculate_safety_factor(robots))
