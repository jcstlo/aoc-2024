from collections import defaultdict


def check_if_update_is_correct(nums: list[int]) -> bool:
    visited, not_found_before = set(), set()
    for num in nums:
        if num in not_found_before:
            return False

        for page in before_rules[num]:
            if page not in visited:
                not_found_before.add(page)

        visited.add(num)
    return True


before_rules = defaultdict(list)
sum = 0

# populate rules
with open("day_05/input_rules.txt", "r") as f:
    for line in f:
        extracted_nums = line.split("|")
        extracted_nums = [int(x) for x in extracted_nums]
        key, val = extracted_nums[1], extracted_nums[0]
        before_rules[key].append(val)

# check correctness of each update
with open("day_05/input_updates.txt", "r") as f:
    for line in f:
        extracted_nums = line.split(",")
        extracted_nums = [int(x) for x in extracted_nums]
        if check_if_update_is_correct(extracted_nums):
            print(f"CORRECT: {extracted_nums}")
            mid_idx = (len(extracted_nums) - 1) // 2
            sum += extracted_nums[mid_idx]
        else:
            print(f"INCORRECT: {extracted_nums}")

print(sum)
