import fileinput

grid: set[tuple[int, int]] = set()

max_row = 0
max_col = 0
for row, line in enumerate(fileinput.input()):
    for col, char in enumerate(line.rstrip()):
        if char == "@":
            grid.add((row, col))
    max_row = row
    max_col = len(line)


def check_roll(roll: tuple[int, int]) -> bool:
    row, col = roll
    full = 0
    for r in range(row - 1, row + 2):
        if not 0 <= r <= max_row:
            continue
        for c in range(col - 1, col + 2):
            if not 0 <= c <= max_col:
                continue
            check = (r, c)
            if check == roll:
                continue
            if check in grid:
                full += 1
    return full < 4


accessible_rolls = 0
for roll in grid:
    if check_roll(roll):
        accessible_rolls += 1

print(accessible_rolls)
