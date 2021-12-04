# day 1

# part 1
with open("day1-input.txt") as f:
    sonar = [int(a) for a in f.readlines()]

increasing = 0
for n in range(1, len(sonar)):
    if sonar[n] > sonar[n - 1]:
        increasing += 1

print(increasing)

# part 2
increasing = 0
for n in range(0, len(sonar) - 3):
    a = sonar[n] + sonar[n+1] + sonar[n+2]
    b = sonar[n+1] + sonar[n+2] + sonar[n+3]
    if b > a:
        increasing += 1

print(increasing)
