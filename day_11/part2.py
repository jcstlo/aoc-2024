from collections import defaultdict


def parse_file() -> list[int]:
    with open("day_11/input.txt", "r") as f:
        for line in f:
            nums = line.split(" ")
            nums = [int(x) for x in nums]
            return nums


def get_init_stones(nums: list[int]) -> dict[int, int]:
    # returns hashmap with {stone_number: count}
    init_stones = defaultdict(int)
    for num in nums:
        init_stones[num] += 1
    return init_stones


def new_stones_from_stone_number(stone_number: int) -> list[int]:
    stone_string = str(stone_number)
    if stone_number == 0:
        return [1]
    elif len(stone_string) % 2 == 0:
        upper_half_idx = len(stone_string) // 2
        left_half_num = int(stone_string[:upper_half_idx])
        right_half_num = int(stone_string[upper_half_idx:])
        return [left_half_num, right_half_num]
    else:
        return [stone_number * 2024]


def blink(curr_stones: dict[int, int]) -> dict[int, int]:
    # returns hashmap with {stone_number: count}
    new_stones = defaultdict(int)

    for stone_number, count in curr_stones.items():
        stones_from_blink = new_stones_from_stone_number(stone_number)
        for stone in stones_from_blink:
            new_stones[stone] += count

    return new_stones


nums = parse_file()
stones = get_init_stones(nums)

for i in range(75):
    print(f"Blinked {i+1} times.")
    stones = blink(stones)

total_stones = 0
for stones in stones.values():
    total_stones += stones

print(total_stones)
