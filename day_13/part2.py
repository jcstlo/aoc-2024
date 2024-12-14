import re


def parse_file():
    button_A_regex = r"Button A: X\+([0-9]+), Y\+([0-9]+)"
    button_B_regex = r"Button B: X\+([0-9]+), Y\+([0-9]+)"
    prize_regex = r"Prize: X=([0-9]+), Y=([0-9]+)"

    machines = []  # list of {AX: int, AY: int, BX: int, BY: int, PX: int, PY: int}
    ax, ay, bx, by, px, py = 0, 0, 0, 0, 0, 0

    lineno = 0
    with open("day_13/input.txt", "r") as f:
        for line in f:
            if lineno % 4 == 0:
                # Button A
                match = re.match(button_A_regex, line)
                ax, ay = match[1], match[2]
            if lineno % 4 == 1:
                # Button B
                match = re.match(button_B_regex, line)
                bx, by = match[1], match[2]
            if lineno % 4 == 2:
                # Prize
                match = re.match(prize_regex, line)
                px, py = match[1], match[2]

                # store the numbers in a new dictionary
                new_machine = {}
                new_machine["AX"] = int(ax)
                new_machine["AY"] = int(ay)
                new_machine["BX"] = int(bx)
                new_machine["BY"] = int(by)
                new_machine["PX"] = int(px) + 10000000000000
                new_machine["PY"] = int(py) + 10000000000000
                machines.append(new_machine)
            lineno += 1
    return machines


def is_close_enough_integer(f: float):
    if f.is_integer():
        return True
    nearest_int = round(f)
    if abs(f - nearest_int) < 0.0001:
        return True
    else:
        return False


def find_fewest_tokens(machine):
    AX, AY, BX, BY, PX, PY = (
        machine["AX"],
        machine["AY"],
        machine["BX"],
        machine["BY"],
        machine["PX"],
        machine["PY"],
    )
    # linear algebra, where
    # | AX BX | | A | = | PX |
    # | AY BY | | B | = | PY |

    # then solve for
    # | A |
    # | B |

    C = 1 / (AX * BY - AY * BX)  # 1/det
    A = C * (BY * PX - BX * PY)
    B = C * (-AY * PX + AX * PY)
    if is_close_enough_integer(A) and is_close_enough_integer(B):
        return round(A) * 3 + round(B)
    else:
        return 0


machines = parse_file()
total_fewest_tokens = 0

for machine in machines:
    total_fewest_tokens += find_fewest_tokens(machine)

print(f"Total fewest tokens: {total_fewest_tokens}")
