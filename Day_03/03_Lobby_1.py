import fileinput

joltage: int = 0
for line in fileinput.input():
    bank: list[int] = list(map(int, list(line.rstrip())))

    max_value: int = max(bank[: len(bank) - 1])
    max_value = (max_value * 10) + max(bank[bank.index(max_value) + 1 :])
    joltage += max_value

print(joltage)
