import fileinput

total_joltage: int = 0
for line in fileinput.input():
    bank: list[int] = list(map(int, list(line.rstrip())))

    digits: list[int] = []

    BATTERIES = 12

    start = 0
    for i in range(1, BATTERIES + 1):
        slice = bank[start : len(bank) - (BATTERIES - i)]
        digit = max(slice)
        digits.append(digit)
        start = bank.index(digit, start) + 1

    joltage = int("".join(map(str, digits)))
    # print(joltage)

    total_joltage += joltage

print(total_joltage)
