# day 3
import numpy as np

# part 1
with open("day3-input.txt") as f:
    report = [item.strip() for item in f.readlines()]

# gamma = most common bit in each position
# epsilon = least common bit in each position: complement of gamma
# answer = gamma * epsilon (in decimal)
# input length is 1000, each line is 12 digits long
Ndigits = len(report[0])
gamma_array = np.zeros(Ndigits, dtype=int)

for entry in report:
    for i, digit in enumerate(entry):
        gamma_array[i] += int(digit)

gamma_array //= 500
epsilon_array = 1 - gamma_array

gamma = ''.join([str(i) for i in gamma_array])
epsilon = ''.join([str(i) for i in epsilon_array])
print(gamma, epsilon)
print(int(gamma, 2), int(epsilon, 2), int(gamma, 2) * int(epsilon, 2))

# part 2


def MSB_LSB(list, digit):
    bit = 0
    N = len(list)
    for entry in list:
        bit += int(entry[digit])

    bit //= (N / 2)
    complement = 1 - bit
    return (int(bit), int(complement))


O2 = []
CO2 = []
list = report
for n in range(Ndigits):
    MSB, _ = MSB_LSB(list, n)
    O2.append(str(MSB))
    list2 = []
    for item in list:
        if item[n] == str(MSB):
            list2.append(item)
    list = list2
    if len(list) == 1:
        break

print(list)
O2report = list[0]

list = report
for n in range(Ndigits):
    _, LSB = MSB_LSB(list, n)
    CO2.append(str(LSB))
    list2 = []
    for item in list:
        if item[n] == str(LSB):
            list2.append(item)
    list = list2
    if len(list) == 1:
        break

print(list)
CO2report = list[0]

print(int(O2report, 2), int(CO2report, 2), int(O2report, 2) * int(CO2report, 2))
