def parse_nums() -> list[int]:
    nums = []
    with open("day_09/input.txt", "r") as f:
        for line in f:
            nums = list(line.strip())
            nums = [int(x) for x in nums]
    return nums


def create_expanded_disk(nums: list[int]) -> list[str]:
    expanded = []
    id = 0
    for idx, num in enumerate(nums):
        if idx % 2 == 0:  # block
            id_str = str(id)
            for i in range(num):
                expanded.append(id_str)
            id += 1
        else:  # free space
            for i in range(num):
                expanded.append(".")
    return expanded


def compress(expanded: list[str]) -> list[str]:
    l, r = 0, len(expanded) - 1
    while expanded[l] != ".":
        l += 1
    while expanded[r] == ".":
        r -= 1

    while l < r:
        expanded[l], expanded[r] = expanded[r], expanded[l]
        while l < len(expanded) and expanded[l] != ".":
            l += 1
        while r >= 0 and expanded[r] == ".":
            r -= 1
    return expanded


def calc_checksum(blocks: list[str]) -> int:
    sum = 0
    for idx, block in enumerate(blocks):
        if block == ".":
            return sum
        sum += idx * int(block)
    return sum


nums = parse_nums()
expanded = create_expanded_disk(nums)
compressed = compress(expanded)
checksum = calc_checksum(compressed)
print(checksum)
