def parse_file() -> list[list[int]]:
    map = []
    with open("day_12/input.txt", "r") as f:
        for line in f:
            map.append(list(line.strip()))
    return map


map = parse_file()
visited = set()
ROWS, COLS = len(map), len(map[0])


def tile_equals_letter(r, c, letter):
    # returns True if tile equals letter
    # returns False if tile is out of range or does not equal letter
    return (r >= 0 and r < ROWS and c >= 0 and c < COLS) and (map[r][c] == letter)


def dfs(r, c, letter) -> tuple[int, int]:
    # hint: # sides = # corners
    # return the area and corners respectively
    total_area = 0
    total_corners = 0
    if (
        (r >= ROWS or r < 0 or c >= COLS or c < 0)
        or map[r][c] != letter
        or (r, c) in visited
    ):
        return (0, 0)

    visited.add((r, c))

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # down, up, right, left
    for dir in dirs:
        dfs_result = dfs(r + dir[0], c + dir[1], letter)
        total_area += dfs_result[0]
        total_corners += dfs_result[1]

    corners = [
        [dirs[0], dirs[2], [1, 1]],  # down right
        [dirs[0], dirs[3], [1, -1]],  # down left
        [dirs[1], dirs[2], [-1, 1]],  # up right
        [dirs[1], dirs[3], [-1, -1]],  # up left
    ]
    for corner in corners:
        nr1, nc1 = r + corner[0][0], c + corner[0][1]
        nr2, nc2 = r + corner[1][0], c + corner[1][1]
        nr3, nc3 = r + corner[2][0], c + corner[2][1]
        if (
            tile_equals_letter(nr1, nc1, letter)
            and tile_equals_letter(nr2, nc2, letter)
            and not tile_equals_letter(nr3, nc3, letter)
        ):
            # concave corner
            total_corners += 1
        if not tile_equals_letter(nr1, nc1, letter) and not tile_equals_letter(
            nr2, nc2, letter
        ):
            # convex corner
            total_corners += 1

    return (total_area + 1, total_corners)


total_price = 0

for row in range(ROWS):
    for col in range(COLS):
        if (row, col) not in visited:
            dfs_result = dfs(row, col, map[row][col])
            print(f"Region {map[row][col]} with A={dfs_result[0]}, C={dfs_result[1]}")
            total_price += dfs_result[0] * dfs_result[1]

print(total_price)
