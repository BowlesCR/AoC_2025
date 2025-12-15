import fileinput

beams: set[int] = set()
splits = 0
for line in fileinput.input():
    line = line.strip()
    if not beams:
        beams.add(line.index("S"))
        continue
    for beam in beams.copy():
        if line[beam] == "^":
            beams.remove(beam)
            beams.add(beam - 1)
            beams.add(beam + 1)
            splits += 1
print(splits)
