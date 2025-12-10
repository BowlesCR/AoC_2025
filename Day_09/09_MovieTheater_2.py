import fileinput
from itertools import combinations
from shapely.geometry import Polygon, box

print("Input...")
red_tiles: list[tuple[int, int]] = []
for line in fileinput.input():
    tile = tuple(map(int, line.rstrip().split(",")))
    red_tiles.append(tile)
del line, tile

floor = Polygon(red_tiles)


def area(combo: tuple[tuple[int, int], tuple[int, int]]) -> int:
    tile_a, tile_b = combo
    return (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)


print("Combinations...")
for tile_a, tile_b in sorted(combinations(red_tiles, 2), key=area, reverse=True):
    rect = box(*tile_a, *tile_b)
    if floor.contains(rect):
        print(area((tile_a, tile_b)))
        break
