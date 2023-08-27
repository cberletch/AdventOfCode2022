# Day 1

# Find the person with the greatest amount of calories in the input file, newline separated

# read input file
f = open('inputs/adventofcode.com_2022_day_1_input.txt')

# establish pointers
high = 0
cur = 0 

# loop through
for line in f:
    if line == '\n':
        if cur > high:
            high = cur
            cur = 0
        else:
            cur = 0
    else:
        cur += int(line)

# print highest
print(high)    


f.close()