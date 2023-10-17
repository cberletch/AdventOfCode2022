# every 3 elves has a shared letter that is unique to their group and is their badge
# find the badges between the groups of elves and sum
# a-z valued 1-26 A-Z valued 27-52

# open input
f = open('inputs/adventofcode.com_2022_day_3_input.txt')
print((len(f.readlines())+1))
total = 0

for group in range(int(len(f.readlines())+1)/3):
    print(group)

