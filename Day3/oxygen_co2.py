# Not going to refactor this as I ran out of time

import copy

with open('input.txt') as f:
    readings = f.read().split()

oxygen_readings, co2_readings = copy.deepcopy(readings), copy.deepcopy(readings)
binary_number_size, freqs = 12, [0,0,0,0,0,0,0,0,0,0,0,0]
# binary_number_size, freqs = 5, [0,0,0,0,0]

# oxygen calculation
for position in range(0, binary_number_size):
    for num in oxygen_readings:
        freqs[position] += 1 if num[position] == '1' else -1
    
    for index, num in enumerate(oxygen_readings):
        # '1's are more common, remove '0'
        if (freqs[position] >= 0 and not int(num[position])):
            oxygen_readings[index] = '-'
        # '0's are more common, remove '1'
        elif (freqs[position] < 0 and int(num[position])):
            oxygen_readings[index] = '-'

    oxygen_readings = list(filter(lambda item: item != "-", oxygen_readings))
    if len(oxygen_readings) == 1:
        break

oxygen = int(oxygen_readings[0], 2)

freqs = [0,0,0,0,0,0,0,0,0,0,0,0]
for position in range(0, binary_number_size):
    for num in co2_readings:
        freqs[position] += 1 if num[position] == '1' else -1
    
    for index, num in enumerate(co2_readings):
        # '1's are more common, remove '1'
        if (freqs[position] >= 0 and int(num[position])):
            co2_readings[index] = '-'
        # '0's are more common, remove '0'
        elif (freqs[position] < 0 and not int(num[position])):
            co2_readings[index] = '-'

    co2_readings = list(filter(lambda item: item != "-", co2_readings))

    if len(co2_readings) == 1:
        break

co2 = int(co2_readings[0], 2)

print(oxygen)
print(co2)
print(oxygen * co2)