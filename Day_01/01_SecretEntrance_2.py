import fileinput

pos = 50
password = 0

for line in fileinput.input():
    rot = int(line[1:]) * (-1 if line[0] == "L" else 1)
    oldpos = pos
    pos += rot

    password += abs(pos) // 100

    if oldpos != 0 and pos < 0:
        password += 1

    if pos == 0:
        password += 1

    pos = pos % 100


print(password)
