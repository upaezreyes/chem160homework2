from random import choices
ntrials = 10000   # number of trials
player1wins = 0   # to keep track\
player2wins = 0
ndice1 = 3
ndice2 = 2

for i in range(ntrials):

    dice2 = choices(range(1,7), k = ndice2)
    player2wins = player2wins + dice2[0] + dice2[1]

    if dice2[0] == dice2[1]:
        continue

    dice1 = choices(range(1,7), k = ndice1)
    dice1.sort(reverse=True)
    dice1.count(2)
    player1wins = player1wins + dice1[0] + dice1[1]

    if player2wins == player1wins or player2wins > player1wins:
        player2wins += 1

    if player1wins > player2wins:
        player1wins += 1


print("Avg sum for player1:", player1wins/ntrials,", Avg sum for player2:", player2wins/ntrials)
print("After several runs, 50% is the probability of player1 of winning")
print("Now it is a fairgame, becuase both players have a 50% change of winning")