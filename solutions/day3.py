# one line per rucksack, always even number of items per side
# find the commonalities between the two halves
# a-z valued 1-26 A-Z valued 27-52

# open input
f = open('inputs/adventofcode.com_2022_day_3_input.txt')

total = 0

for row in f:
    first = row[:len(row) // 2]
    second = row[len(row) // 2:]

    for char in first:
        if char in second:
            if ord(char) < 91:
                total += (ord(char) - 38)
            else:
                total += (ord(char) - 96)
            
            break

print(total)