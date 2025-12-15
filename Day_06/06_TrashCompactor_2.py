import fileinput
import math

lines: list[str] = []
operators: list[str] = []
splits: list[int] = []

for line in fileinput.input():
    line = line.rstrip()
    if "+" in line or "*" in line:
        operators = line.split()
        splits = [i for i in range(len(line)) if line[i] in ["+", "*"]]
    else:
        lines.append(line)

# Fix ragged-edge lines
maxline = max([len(line) for line in lines])
for i, line in enumerate(lines):
    if len(line) != maxline:
        lines[i] = line.ljust(maxline, " ")

total = 0

for i, split in enumerate(splits):
    if i == len(splits) - 1:
        end = maxline - 1
    else:
        end = splits[i + 1] - 2
    terms: list[int] = []
    for c in range(end, split - 1, -1):
        term = ""
        for r in range(len(lines)):
            term += lines[r][c]
        terms.append(int(term))

    if operators[i] == "+":
        total += sum(terms)
    elif operators[i] == "*":
        total += math.prod(terms)

print(total)
