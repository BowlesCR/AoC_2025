import fileinput

beams: dict[int, int] = {}

for line in fileinput.input():
    line = line.strip()
    if not beams:
        beams[line.index("S")] = 1
        continue
    beams_copy = beams.copy()
    for beam_i in beams_copy:
        count = beams_copy[beam_i]
        if count == 0:
            continue
        if line[beam_i] == "^":
            beams[beam_i] -= count
            beams[beam_i - 1] = beams.get(beam_i - 1, 0) + count
            beams[beam_i + 1] = beams.get(beam_i + 1, 0) + count
print(sum(beams.values()))
