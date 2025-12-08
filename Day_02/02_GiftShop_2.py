import fileinput
import re

total = 0

for r in list(fileinput.input())[0].rstrip().split(","):
    split = r.split("-")
    start = int(split[0])
    end = int(split[1])
    del split

    rng = range(start, end + 1)

    for i in rng:
        s = str(i)
        if re.match(r"^(\d+)\1+$", s):
            total += i
            print(i)

print(total)
