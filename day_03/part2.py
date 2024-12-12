import re

# mul(123,123)
mul_pattern = "(mul\([0-9]+,[0-9]+\)|(do\(\))|(don't\(\)))"
num_groups_pattern = r"mul\(([0-9]+),([0-9]+)\)"

sum = 0
enabled = True

with open("day_03/input.txt", "r") as f:
    for line in f:
        extracted_list = re.findall(mul_pattern, line)
        for statement in extracted_list:
            if statement[1] != "":
                enabled = True
                print("ENABLED")
            elif statement[2] != "":
                enabled = False
                print("DISABLED")
            else:
                if enabled:
                    m = re.match(num_groups_pattern, statement[0])
                    print(m.group(1, 2))
                    sum += int(m.group(1)) * int(m.group(2))
                    print(sum)

print(sum)
