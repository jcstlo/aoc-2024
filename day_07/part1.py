def check_if_valid_equation(target: int, nums: list[int]) -> bool:
    def dfs(idx, curr, op):
        new_curr = curr + nums[idx] if op == "+" else curr * nums[idx]

        if idx == len(nums) - 1:
            return new_curr == target

        return dfs(idx + 1, new_curr, "+") or dfs(idx + 1, new_curr, "*")

    return dfs(1, nums[0], "+") or dfs(1, nums[0], "*")


sum = 0

with open("day_07/input.txt", "r") as f:
    for line in f:
        [target, nums] = line.split(": ")
        target = int(target)
        nums = [int(x) for x in nums.strip().split(" ")]
        if check_if_valid_equation(target, nums):
            sum += target
            print(f"CORRECT: {target} -> {nums}")
        else:
            print(f"INCORRECT: {target} -> {nums}")

print(sum)
