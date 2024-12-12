def calculate_equation(target: int, eqn: list[int | str]) -> bool:
    # Parse the equation from left to right
    curr = eqn[0]
    op = ""

    for idx, elem in enumerate(eqn):
        if idx == 0:
            continue
        if idx % 2 == 1:  # operator
            op = elem
            continue

        if op == "+":
            curr = curr + elem
        elif op == "*":
            curr = curr * elem
        else:  # "||"
            concat = str(curr) + str(elem)
            curr = int(concat)

    if curr == target:
        print(f"CORRECT: {target} = {eqn}")
        return True
    return False


def check_if_valid_equation(target: int, nums: list[int]) -> bool:
    # Create equations with DFS, calculate when all numbers have been used
    curr = [nums[0]]

    def dfs(idx, op) -> bool:
        result = False
        curr.append(op)
        curr.append(nums[idx])

        if idx == len(nums) - 1:
            result = calculate_equation(target, curr)
            curr.pop()
            curr.pop()
            return result

        result = dfs(idx + 1, "+") or dfs(idx + 1, "*") or dfs(idx + 1, "||")
        curr.pop()
        curr.pop()
        return result

    return dfs(1, "+") or dfs(1, "*") or dfs(1, "||")


sum = 0
with open("day_07/input.txt", "r") as f:
    for line in f:
        [target, nums] = line.split(": ")
        target = int(target)
        nums = [int(x) for x in nums.strip().split(" ")]
        if check_if_valid_equation(target, nums):
            sum += target

print(sum)
