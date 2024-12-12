def parse_nums() -> list[int]:
    nums = []
    with open("day_09/input.txt", "r") as f:
        for line in f:
            nums = list(line.strip())
            nums = [int(x) for x in nums]
    return nums


def separate_block_sizes(nums: list[int]) -> list[(int, int, int)]:
    # returns list[(id, size, start_idx)]
    blocks = []
    start_idx = 0
    id = 0
    for idx, num in enumerate(nums):
        if idx % 2 == 0:
            blocks.append((id, num, start_idx))
            id += 1
        start_idx += num
    return blocks


def separate_free_space(nums: list[int]) -> list[(int, int)]:
    # returns list[(size, start_idx)]
    start_idx = 0
    spaces = []
    for idx, num in enumerate(nums):
        if idx % 2 == 1 and num > 0:
            spaces.append((num, start_idx))
        start_idx += num
    return spaces


def create_expanded_disk(nums: list[int]) -> list[str]:
    expanded = []
    id = 0
    for idx, num in enumerate(nums):
        if idx % 2 == 0:  # block
            id_str = str(id)
            for i in range(num):
                expanded.append(id_str)
            id += 1
        else:  # free space
            for i in range(num):
                expanded.append(".")
    return expanded


def calc_checksum(blocks: list[str]) -> int:
    sum = 0
    for idx, block in enumerate(blocks):
        if block == ".":
            continue
        sum += idx * int(block)
    return sum


def print_blocks(blocks):
    for block in blocks:
        print(f"id = {block[0]}")
        print(f"size = {block[1]}")
        print(f"start_idx = {block[2]}\n")


def print_spaces(spaces):
    for space in spaces:
        print(f"size = {space[0]}")
        print(f"start_idx = {space[1]}\n")


def move_blocks_into_space(blocks, moved_blocks, spaces, space_idx):
    block_idx_to_remove = []
    for block_idx in range(len(blocks) - 1, -1, -1):
        if spaces[space_idx][0] == 0:
            # remove 'moved blocks' from the original list
            for idx in block_idx_to_remove:
                blocks.pop(idx)
            return
        if (
            blocks[block_idx][1] <= spaces[space_idx][0]  # block can fit into space
            and blocks[block_idx][2] > spaces[space_idx][1]  # block will move left
        ):
            # move block
            moved_blocks.append(
                (
                    blocks[block_idx][0],
                    blocks[block_idx][1],
                    spaces[space_idx][1],
                )
            )
            block_idx_to_remove.append(block_idx)

            # update space
            spaces[space_idx] = (
                spaces[space_idx][0] - blocks[block_idx][1],
                spaces[space_idx][1] + blocks[block_idx][1],
            )
    # remove 'moved blocks' from the original list
    for idx in block_idx_to_remove:
        blocks.pop(idx)
    return


def move_blocks(blocks, spaces):
    # returns list[(id, size, start_idx)]
    space_idx = 0
    moved_blocks = []

    while space_idx < len(spaces):
        move_blocks_into_space(blocks, moved_blocks, spaces, space_idx)
        print(f"finished space[{space_idx}]")
        space_idx += 1

    return blocks + moved_blocks


def calc_checksum(blocks):
    sum = 0
    for block in blocks:
        for idx in range(block[2], block[2] + block[1], 1):
            sum += idx * block[0]
    return sum


nums = parse_nums()
blocks = separate_block_sizes(nums)
spaces = separate_free_space(nums)
new_blocks = move_blocks(blocks, spaces)

print(f"sum = {calc_checksum(new_blocks)}")
