import fileinput
import math

worksheet: list[list[int]] = []
operators: list[str] = []
for line in fileinput.input():
    if "+" in line or "*" in line:
        operators = line.split()
    else:
        worksheet.append(list(map(int, line.split())))

total = 0
for col in range(len(operators)):
    terms = [worksheet[r][col] for r in range(len(worksheet))]
    if operators[col] == "+":
        total += sum(terms)
    elif operators[col] == "*":
        total += math.prod(terms)

print(total)
