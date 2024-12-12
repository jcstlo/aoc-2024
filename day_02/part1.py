numSafe = 0

def isPairSafe(curr: int, prev: int, increasing: bool):
    if increasing and curr <= prev:
        return False
    if not increasing and curr >= prev:
        return False
    if abs(curr - prev) > 3:
        return False
    return True

with open("day_02/input.txt", "r") as f:
    for line in f:
        # convert each line to list of ints
        reportArray = line.split()
        for idx, s in enumerate(reportArray):
            reportArray[idx] = int(reportArray[idx])
        
        # deal with corner case
        if reportArray[1] == reportArray[0]:
            continue

        # get initial direction
        increasing = True
        if reportArray[1] < reportArray[0]:
            increasing = False
        
        # check if remaining report is safe
        safe = True
        for idx, num in enumerate(reportArray):
            if idx == 0:
                continue
        
            # safe report rules
            safe = isPairSafe(reportArray[idx], reportArray[idx-1], increasing)
            if not safe:
                break

        if safe:
            numSafe += 1
    
    # ANSWER TO PART 1
    print(numSafe)