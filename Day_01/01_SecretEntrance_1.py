import fileinput

pos = 50
password = 0

for line in fileinput.input():
    rot = int(line[1:]) * (-1 if line[0] == "L" else 1)
    pos = (pos + rot) % 100
    if pos == 0:
        password += 1

print(password)
