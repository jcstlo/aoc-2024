from collections import defaultdict

antennas = defaultdict(list)
antinodes = set()

row = 0
MAXROW, MAXCOL = 0, 0

# add all antenna locations to a dictionary
with open("day_08/input.txt", "r") as f:
    for line in f:
        for col, char in enumerate(line.strip()):
            if char != ".":
                antennas[char].append((row, col))
            MAXCOL = max(MAXCOL, col + 1)
        row += 1
MAXROW = row

# find all possible antinodes
for antenna_list in antennas.values():
    for first in range(len(antenna_list)):
        for second in range(len(antenna_list)):
            if first == second:
                # add the node itself to antinodes
                antinodes.add(antenna_list[first])
                continue

            difference = (
                antenna_list[second][0] - antenna_list[first][0],
                antenna_list[second][1] - antenna_list[first][1],
            )

            antinode = (
                antenna_list[second][0] + difference[0],
                antenna_list[second][1] + difference[1],
            )

            while antinode[0] in range(MAXROW) and antinode[1] in range(MAXCOL):
                if antinode not in antinodes:
                    antinodes.add(antinode)
                    print(f"antinode at {antinode}")

                antinode = (antinode[0] + difference[0], antinode[1] + difference[1])

print(len(antinodes))
