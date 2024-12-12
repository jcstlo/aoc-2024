def parse_map():
    map = []
    with open("day_10/input.txt", "r") as f:
        for line in f:
            row = list(line.strip())

            for i in range(len(row)):
                if row[i] == ".":
                    row[i] = 999  # unreachable

            row = [int(x) for x in row]
            map.append(row)
    return map


def debug_print_map(map):
    for row in map:
        print(row)


def calculate_trailhead_score_sum(map) -> int:
    ROWS, COLS = len(map), len(map[0])
    sum = 0

    def dfs(r, c, expected, start):
        nonlocal sum
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return
        if map[r][c] != expected:
            return
        if expected == 9:
            sum += 1
            return

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dir in dirs:
            dfs(r + dir[0], c + dir[1], expected + 1, start)
        return

    for row in range(len(map)):
        for col in range(len(map[0])):
            dfs(row, col, 0, (row, col))

    return sum


map = parse_map()
score_sum = calculate_trailhead_score_sum(map)
print(score_sum)
