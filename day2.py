# day 2

# part 1
with open("day2-input.txt") as f:
    instructions = f.readlines()

x = 0
y = 0

for step in instructions:
    direction, amount = step.split()
    if direction == "forward":
        x += int(amount)
    elif direction == "up":
        y -= int(amount)
    elif direction == "down":
        y += int(amount)

print(x, y, x * y)

# part 2
# aim, now a thing. this is similar to the ship steering one from 2020
x = 0
y = 0
aim = 0

for step in instructions:
    direction, amount = step.split()
    if direction == "forward":
        x += int(amount)
        y += int(amount) * aim
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)

print(x, y, x * y)
