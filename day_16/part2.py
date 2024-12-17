import heapq


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data


grid = []
lowest_score_threshold = float("inf")
best_path_cells = set()


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
    global lowest_score_threshold
    ROWS, COLS = len(grid), len(grid[0])

    # cache the lowest score found for each cell at a specific direction
    # this helps prune inefficient paths earlier
    grid_lowest_path = [[[float("inf")] * COLS for _ in range(ROWS)] for _ in range(4)]

    # (total_score, row, col, orientation, node)
    start_node = Node(start_pos)
    minHeap = [(0, start_pos[0], start_pos[1], "E", start_node)]

    def can_add_position_to_heap(r, c, dir, score):
        d = 4
        if dir == "N":
            d = 0
        elif dir == "S":
            d = 1
        elif dir == "E":
            d = 2
        elif dir == "W":
            d = 3

        if (
            (r >= 0 and r < ROWS)
            and (c >= 0 and c < COLS)
            and grid[r][c] != "#"
            and score <= grid_lowest_path[d][r][c]
        ):
            grid_lowest_path[d][r][c] = score
            return True
        else:
            return False

    def try_to_add_position_to_heap(next_score, r, c, next_or, node):
        nr, nc = r, c
        if next_or == "N":
            nr = r - 1
        elif next_or == "S":
            nr = r + 1
        elif next_or == "E":
            nc = c + 1
        elif next_or == "W":
            nc = c - 1

        if can_add_position_to_heap(nr, nc, next_or, next_score):
            new_node = Node((nr, nc))
            new_node.next = node
            heapq.heappush(minHeap, (next_score, nr, nc, next_or, new_node))

    # BFS with priority queue (Djikstra's)
    while minHeap:
        curr = heapq.heappop(minHeap)
        if curr[0] > lowest_score_threshold:
            continue

        if (curr[1], curr[2]) == end_pos and curr[0] <= lowest_score_threshold:
            lowest_score_threshold = curr[0]
            n = curr[4]
            while n:
                best_path_cells.add(n.data)
                n = n.next
            continue

        if curr[3] == "N":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "N", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "E", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "W", curr[4])
        elif curr[3] == "S":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "S", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "E", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "W", curr[4])
        elif curr[3] == "E":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "E", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "N", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "S", curr[4])
        elif curr[3] == "W":
            try_to_add_position_to_heap(curr[0] + 1, curr[1], curr[2], "W", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "N", curr[4])
            try_to_add_position_to_heap(curr[0] + 1001, curr[1], curr[2], "S", curr[4])

    return grid_lowest_path


parse_file()
start_pos, end_pos = find_start_and_end_positions(grid)
grid_lowest = djikstra(start_pos, end_pos, grid)

for cell in best_path_cells:
    grid[cell[0]][cell[1]] = "O"

print("")
for row in grid:
    print("".join(row))

print("")
print(f"lowest_score_threshold = {lowest_score_threshold}")
print(f"len(best_path_cells) = {len(best_path_cells)}")
