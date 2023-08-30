# day 2 - calculate the points given the strategies for rock, paper, scissors presented
# rock = 1, paper = 2, scissors = 3 points
# X = need to lose, # Y = Draw, Z = Win
# loss in col 2 = 0, tie = 3, win = 6 points


# opponent: rock = a, paper = b, scissors = c
# you: rock = x, paper = y, scissors = z

f = open('inputs/adventofcode.com_2022_day_2_input.txt')

possibilities = {
    'ax':3, # 1 for rock, x for lose, return scissors 3
    'ay':4, # 2 for rock, y for draw, return rock 4
    'az':8, # 3 for rock, z for win, return paper 8

    'bx':1, # 1 for paper, x for lose, return rock 1
    'by':5, # 2 for paper, y for draw, return paper 5
    'bz':9, # 3 for paper, z for win,  return scissors 9

    'cx':2, # 1 for scissors, x for lose, return paper 2
    'cy':6, # 2 for scissors, y for draw, return scissors 6
    'cz':7, # 3 for scissors, z for win,  return rock 7
}

sum = 0

for line in f:
    
    if line == '\n':
        continue
    else:
        row = line.replace(" ", "").lower().strip('\n')
        sum += possibilities[row] 

print(sum)