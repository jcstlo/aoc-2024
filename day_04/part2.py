board = []  # list[list[str]]

with open("day_04/input.txt", "r") as f:
    for line in f:
        board.append(list(line.strip()))


def mas_exists(char_1, char_2) -> bool:
    # pre-condition: the center is an "A"
    if (char_1 == "M" and char_2 == "S") or (char_1 == "S" and char_2 == "M"):
        return True
    else:
        return False


num_valid = 0

# iterate over all valid starting positions where "A" would be
for row in range(1, len(board) - 1, 1):
    for col in range(1, len(board[0]) - 1, 1):
        if board[row][col] != "A":
            continue

        # get characters in positive diagonal
        pos_char1 = board[row + 1][col - 1]
        pos_char2 = board[row - 1][col + 1]

        # get characters in negative diagonal
        neg_char1 = board[row - 1][col - 1]
        neg_char2 = board[row + 1][col + 1]

        # add to count if both diagonals have MAS
        if mas_exists(pos_char1, pos_char2) and mas_exists(neg_char1, neg_char2):
            num_valid += 1

print(num_valid)
