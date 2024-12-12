import re

# mul(123,123)
mul_pattern = "mul\([0-9]+,[0-9]+\)"
num_groups_pattern = r"mul\(([0-9]+),([0-9]+)\)"

sum = 0

with open("day_03/input.txt", "r") as f:
    for line in f:
        extracted_list = re.findall(mul_pattern, line)
        for statement in extracted_list:
            m = re.match(num_groups_pattern, statement)
            print(m.group(1, 2))
            sum += int(m.group(1)) * int(m.group(2))
            print(sum)

print(sum)
