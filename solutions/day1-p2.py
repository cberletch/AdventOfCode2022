# part 2

# find the top 3 and sum the calories for each

f = open('inputs/adventofcode.com_2022_day_1_input.txt')

elf_dict = dict()
cur = 0
counter = 0

# sum and add to dict
for line in f:
    if line == '\n':
        elf_dict[counter] = cur
        cur = 0
        counter += 1
    else:
        cur += int(line)

# find and sum top 3

arr = sorted(elf_dict.values(), reverse=True)

top_3 = sum(arr[:3])

print(top_3)
