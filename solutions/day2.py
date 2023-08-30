# day 2 - calculate outcomes of rock, paper, scissors from input file
# rock = 1, paper = 2, scissors = 3 points
# loss in col 2 = 0, tie = 3, win = 6 points

# opponent: rock = a, paper = b, scissors = c
# you: rock = x, paper = y, scissors = z

f = open('inputs/adventofcode.com_2022_day_2_input.txt')

possibilities = {
    'ax':4, # 1 for rock, 3 for tie
    'ay':8, # 2 for paper, 6 for win
    'az':3, # 3 for scissors, 0 for loss

    'bx':1, # 1 for rock, 0 for loss
    'by':5, # 2 for paper, 3 for tie
    'bz':9, # 3 for scissors, 6 for win

    'cx':7, # 1 for rock, 6 for win
    'cy':2, # 2 for paper, 0 for loss
    'cz':6, # 3 for scissors, 3 for tie
}

sum = 0

for line in f:
    
    if line == '\n':
        continue
    else:
        row = line.replace(" ", "").lower().strip('\n')
        sum += possibilities[row] 

print(sum)