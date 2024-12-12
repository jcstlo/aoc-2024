board = []  # list[list[str]]

with open("day_04/input.txt", "r") as f:
    for line in f:
        board.append(list(line.strip()))

dirs = [
    [(0, -1), (0, -2), (0, -3)],  # left
    [(0, 1), (0, 2), (0, 3)],  # right
    [(-1, 0), (-2, 0), (-3, 0)],  # up
    [(1, 0), (2, 0), (3, 0)],  # down
    [(1, 1), (2, 2), (3, 3)],  # down-right
    [(1, -1), (2, -2), (3, -3)],  # down-left
    [(-1, 1), (-2, 2), (-3, 3)],  # up-right
    [(-1, -1), (-2, -2), (-3, -3)],  # up-left
]

letters = ["M", "A", "S"]

num_valid = 0

for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != "X":
            continue

        for dir in dirs:
            valid = True
            for i in range(3):
                letter_pos = [row + dir[i][0], col + dir[i][1]]
                if (letter_pos[0] not in range(len(board))) or (
                    letter_pos[1] not in range(len(board[0]))
                ):
                    valid = False
                    break

                letter = letters[i]

                if board[letter_pos[0]][letter_pos[1]] != letter:
                    valid = False
                    break

            if valid:
                num_valid += 1

print(num_valid)
