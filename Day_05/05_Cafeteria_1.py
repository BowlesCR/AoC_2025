import fileinput

fresh: set[range] = set()

count = 0
for line in fileinput.input():
    line = line.rstrip()
    if line == "":
        continue
    elif "-" in line:
        parts = tuple(map(int, line.split("-")))
        fresh.add(range(parts[0], parts[1] + 1))
    else:
        ing = int(line)
        if any(ing in r for r in fresh):
            count += 1
print(count)
