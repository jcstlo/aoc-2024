from collections import defaultdict

list1, list2 = [], []
freq_list2 = defaultdict(int)

with open("day_01/input.txt", "r") as f:
    for line in f:
        rawStr = line.split()
        list1.append(int(rawStr[0]))
        list2.append(int(rawStr[1]))

for num in list2:
    freq_list2[num] += 1

similarity = 0
for num in list1:
    if num in freq_list2:
        print(f"{num} {freq_list2[num]}")
        similarity += num * freq_list2[num]

# ANSWER TO PART 2
print(similarity)