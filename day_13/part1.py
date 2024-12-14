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
                new_machine["PX"] = int(px)
                new_machine["PY"] = int(py)
                machines.append(new_machine)
            lineno += 1
    return machines


def find_fewest_tokens(machine):
    fewest_tokens = float("inf")
    for num_a in range(101):
        for num_b in range(101):
            if (num_a * machine["AX"] + num_b * machine["BX"] == machine["PX"]) and (
                num_a * machine["AY"] + num_b * machine["BY"] == machine["PY"]
            ):
                fewest_tokens = min(fewest_tokens, num_a * 3 + num_b)
    return fewest_tokens if fewest_tokens != float("inf") else 0


machines = parse_file()
total_fewest_tokens = 0

for machine in machines:
    total_fewest_tokens += find_fewest_tokens(machine)

print(f"Total fewest tokens: {total_fewest_tokens}")
