'''
 Write a code that prints out individual scores of two players in a game of cricket where score is given as runs per ball
 in an array. In a game of cricket a person changes strike if he scores an odd number, and keeps strike with him
 if he scores an even number. No need to consider changing strike after every 6 balls or an over.
    Sample Input1: [1,2]
    Output1: p1: 1, p2: 2
    Sample Input2: [1,2,3,2,1]
    Output2: p1: 4, p2: 5
'''

print("Hi!! Welcome to score calculator")

# s_inp = []

s_inp = [int(ele) for ele in input("Please enter the scores with space as gap: ").split()]

# s_inp = [1,1,1,1,1,1,2]  # score board

d = {'p1': [], 'p2': []}  # individual score placeholder

strike = 'p1'
over = False

for i in range(len(s_inp)):

# check strike and append accordingly
    if strike == 'p1':
        d['p1'].append(s_inp[i])
        if s_inp[i]%2 == 0:
            strike = 'p1'
        else:
            strike = 'p2'
    elif strike == 'p2':
        d['p2'].append(s_inp[i])
        if s_inp[i]%2 == 0:
            strike = 'p2'
        else:
            strike = 'p1'


# Check over
    k = i + 1
    if k%6 == 0:
        over = True
    else:
        over = False

# check over and change strike accordingly
    if over == True and s_inp[i]%2 == 0:
        if strike == 'p1':
            strike = 'p2'
            # print(f"Strike changing at score {s_inp[i]}")
        elif strike == 'p2':
            strike = 'p1'
            # print(f"Strike changing at score {s_inp[i]}")







d['p2'] = sum(d['p2'])
d['p1'] = sum(d['p1'])
print(f"Score board : {d}")
print(f" Player 1 score: {d['p1']}")
print(f" Player 2 score: {d['p2']}")


