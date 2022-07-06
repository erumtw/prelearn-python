import random


def play(player):
    # s = ['r', 'p', 's'] #form 1
    d = {'r': "Rock", 'p': "Paper", 's': "Scissor"} #form 2

    # computer = s[random.randrange(len(s))] #form 1
    computer = random.choice(list(d.keys())) #form 2

    if player == computer:
        result = "Tie"
    elif player == 'p' and computer == 'r':
        result = "You win"
    elif player == 'r' and computer == 's':
        result = "You win"
    elif player == 's' and computer == 'p':
        result = "You win"
    else:
        result = "You lose"

    print("You -> {}, Computer -> {}, Result -> {}!".format(d[player], d[computer], result))

while True:
    prompt = input("[r]ock [p]aper [s]cissor e[x]it -> ")

    if(prompt != 'x'):
        play(prompt)
    else:
        break;
