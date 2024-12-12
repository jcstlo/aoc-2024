from collections import defaultdict

before_rules = defaultdict(list)
sum = 0


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


def sort_by_rules(nums: list[int]) -> list[int]:
    # Bubble sort, but the order is determined by the before_rules dictionary
    for _ in range(0, len(nums)):
        for i in range(0, len(nums)):
            if i + 1 < len(nums):
                if nums[i + 1] in before_rules[nums[i]]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


# populate rules
with open("day_05/input_rules.txt", "r") as f:
    for line in f:
        extracted_nums = line.split("|")
        extracted_nums = [int(x) for x in extracted_nums]
        key, val = extracted_nums[1], extracted_nums[0]
        before_rules[key].append(val)

with open("day_05/input_updates.txt", "r") as f:
    for line in f:
        extracted_nums = line.split(",")
        extracted_nums = [int(x) for x in extracted_nums]

        if not check_if_update_is_correct(extracted_nums):
            print(f"incorrect, before sorting: {extracted_nums}")
            extracted_nums = sort_by_rules(extracted_nums)
            print(f"after sorting: {extracted_nums}\n")
            mid_idx = (len(extracted_nums) - 1) // 2
            sum += extracted_nums[mid_idx]

print(sum)
