import fileinput
from itertools import combinations

tiles: set[tuple[int, int]] = set()
for line in fileinput.input():
    tiles.add(tuple(map(int, line.rstrip().split(","))))
del line

maxarea = 0

for combo in combinations(tiles, 2):
    a, b = combo
    height = abs(a[0] - b[0]) + 1
    width = abs(a[1] - b[1]) + 1
    area = height * width
    maxarea = max(area, maxarea)

print(maxarea)
