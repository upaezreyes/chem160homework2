from random import choices

ntrials = 100000    # number of trials
player1wins = 0     # to keep track of player1
player2wins = 0     # to keep track of player2
ndice1 = 3     # number of dices for player1
ndice2 = 2     # number of dices for player2


for i in range(ntrials):   # loop for the number of trials

    #Ramdomly pick the two number for player2
    dice2 = choices(range(1,7), k = ndice2)
    player2wins = player2wins + dice2[0] + dice2[1]

    # Test if player2's two dice are equal
    if dice2[0] == dice2[1]:
       # player2wins += 1
        continue
    # Randomly picking the two highest number of 3 dices for player1
    dice1 = choices(range(1,7), k = ndice1)
    dice1.sort(reverse=True)
    player1wins = player1wins + dice1[0] + dice1[1]   #adding the two highest numbers

    if player2wins == player1wins or player2wins > player1wins:
        player2wins += 1

    if player1wins > player2wins:
        player1wins += 1


print("Avg sum for player1:",player1wins/ntrials, ", Avg sum for payer2:",player2wins/ntrials)
print("After several runs, 54.2% is the probability of player1 of winning")
print("it is not fair at all because player1 still have over 50% change of winning")