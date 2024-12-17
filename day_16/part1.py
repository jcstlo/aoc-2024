import heapq

grid = []


def parse_file():
    with open("day_16/input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))


def find_start_and_end_positions(grid):
    start_pos, end_pos = (0, 0), (0, 0)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start_pos = (r, c)
            if grid[r][c] == "E":
                end_pos = (r, c)

    return [start_pos, end_pos]


def djikstra(start_pos, end_pos, grid):
    ROWS, COLS = len(grid), len(grid[0])

    # (total_score, row, col, orientation)
    minHeap = [(0, start_pos[0], start_pos[1], "E")]

    visited = set()  # (row, col)
    visited.add(start_pos)

    def can_add_position_to_heap(r, c):
        return (
            (r >= 0 and r < ROWS)
            and (c >= 0 and c < COLS)
            and (r, c) not in visited
            and grid[r][c] != "#"
        )

    def try_to_add_position_to_heap(next_score, r, c, next_or):
        nr, nc = r, c
        if next_or == "N":
            nr = r - 1
        elif next_or == "S":
            nr = r + 1
        elif next_or == "E":
            nc = c + 1
        elif next_or == "W":
            nc = c - 1

        if can_add_position_to_heap(nr, nc):
            print(
                f"adding ({nr}, {nc}):{next_or} with score = {next_score}, heaplen = {len(minHeap)}"
            )
            heapq.heappush(minHeap, (next_score, nr, nc, next_or))
            visited.add((nr, nc))

    # BFS with priority queue (Djikstra's)
    while minHeap:
        curr = heapq.heappop(minHeap)
        if (curr[1], curr[2]) == end_pos:
            return curr[0]

        if curr[3] == "N":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "N")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "E")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "W")
        elif curr[3] == "S":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "S")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "E")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "W")
        elif curr[3] == "E":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "E")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "N")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "S")
        elif curr[3] == "W":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "W")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "N")
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "S")

    return "ERROR"


parse_file()
start_pos, end_pos = find_start_and_end_positions(grid)
lowest_score = djikstra(start_pos, end_pos, grid)

print(f"lowest score = {lowest_score}")
