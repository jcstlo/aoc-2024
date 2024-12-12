def parse_file() -> list[int]:
    with open("day_11/input.txt", "r") as f:
        for line in f:
            nums = line.split(" ")
            nums = [int(x) for x in nums]
            return nums


def blink(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        num_as_string = str(num)
        if num == 0:
            result.append(1)
        elif len(num_as_string) % 2 == 0:
            upper_half_idx = len(num_as_string) // 2
            left_half_num = int(num_as_string[:upper_half_idx])
            right_half_num = int(num_as_string[upper_half_idx:])
            result.append(left_half_num)
            result.append(right_half_num)
        else:
            result.append(num * 2024)
    return result


stones = parse_file()

for i in range(75):
    stones = blink(stones)
    print(f"After {i+1} blinks:")
    print(f"Number of stones = {len(stones)}\n")
