def isSafe(nums: list[int]) -> bool:
    def dfs(idx, prev, skipped, dir):
        # base case
        if idx >= len(nums):
            return True
        
        # check rules
        curr = nums[idx]
        if ((abs(curr - prev) > 3) or
            (curr == prev) or
            (dir == "INC" and curr < prev) or
            (dir == "DEC" and curr > prev)):
            return False

        newDir = "INC" if curr > prev else "DEC"
        if dfs(idx+1, curr, skipped, newDir):
            return True
        
        return False if skipped else dfs(idx+2, curr, True, newDir)

    return (dfs(1, nums[0], False, "NA") or
            dfs(2, nums[0], True, "NA") or
            dfs(2, nums[1], True, "NA"))

numSafe = 0
with open("day_02/input.txt", "r") as f:
    for line in f:
        # convert each line to list of ints
        reportArray = line.split()
        for idx, s in enumerate(reportArray):
            reportArray[idx] = int(reportArray[idx])

        # backtracking solution
        if isSafe(reportArray):
            print(f"SAFE: {reportArray}")
            numSafe += 1
        else:
            print(f"UNSAFE: {reportArray}")

    # ANSWER TO PART 2
    print(numSafe)