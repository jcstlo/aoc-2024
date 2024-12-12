def parse_file() -> list[list[int]]:
    map = []
    with open("day_12/input.txt", "r") as f:
        for line in f:
            map.append(list(line.strip()))
    return map


map = parse_file()
visited = set()
ROWS, COLS = len(map), len(map[0])


def dfs(r, c, letter) -> tuple[int, int]:
    # return the area and perimeter respectively
    total_area = 0
    total_perimeter = 0
    if (r >= ROWS or r < 0 or c >= COLS or c < 0) or map[r][c] != letter:
        return (0, 1)
    if (r, c) in visited:
        return (0, 0)

    visited.add((r, c))

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dir in dirs:
        dfs_result = dfs(r + dir[0], c + dir[1], letter)
        total_area += dfs_result[0]
        total_perimeter += dfs_result[1]

    return (total_area + 1, total_perimeter)


total_price = 0

for row in range(ROWS):
    for col in range(COLS):
        if (row, col) not in visited:
            dfs_result = dfs(row, col, map[row][col])
            print(f"Region {map[row][col]} with A={dfs_result[0]}, P={dfs_result[1]}")
            total_price += dfs_result[0] * dfs_result[1]

print(total_price)
