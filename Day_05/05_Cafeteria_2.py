import fileinput

fresh: list[range] = []

for line in fileinput.input():
    line = line.rstrip()
    if line == "":
        continue
    elif "-" in line:
        start, end = map(int, line.split("-"))
        fresh.append(range(start, end + 1))  # Make range inclusive
    else:
        continue

fresh.sort(key=lambda r: r.start)
new_fresh: list[range] = []
for r in fresh:
    if new_fresh and r.start <= new_fresh[-1].stop:
        new_fresh[-1] = range(new_fresh[-1].start, max(new_fresh[-1].stop, r.stop))
    else:
        new_fresh.append(r)

print(sum(len(r) for r in new_fresh))
