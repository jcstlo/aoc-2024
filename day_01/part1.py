list1, list2 = [], []

with open("day_01/input.txt", "r") as f:
    for line in f:
        rawStr = line.split()
        list1.append(int(rawStr[0]))
        list2.append(int(rawStr[1]))

list1.sort()
list2.sort()

diff = 0
for i in range(len(list1)):
    print(str(list1[i]) + " " + str(list2[i]))
    diff += abs(list1[i] - list2[i])

# ANSWER TO PART 1
print(diff)