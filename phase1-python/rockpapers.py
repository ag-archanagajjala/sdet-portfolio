import random, sys

print("ROCK, PAPER, SCISSORS")
#initialization display of the score
wins = 0
losses = 0
ties = 0
print("WINS-", wins, "; LOSSES-", losses, "; TIES-", ties)


user_move=""
while True:
    
    #Get user's move
    user_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit > ")
    if user_move == 'r':
        user_move = 'ROCK'
    elif user_move == 'p':
        user_move = 'PAPER'
    elif user_move == 's':
        user_move = 'SCISSORS'
    elif user_move =='q':
        sys.exit()

    #Get computer's move
    computer_move = random.randint(1,3)
    if computer_move == 1:
        computer_move = 'ROCK'
    elif computer_move == 2:
        computer_move = 'PAPER'
    else:
        computer_move = 'SCISSORS' 

    print(user_move, "versus...")
    print(computer_move, "** Computer's move***")

    #compare user_move and computer_move
    if user_move == computer_move:
        print("It is a tie!")
        ties = ties + 1        
    elif (user_move == 'ROCK' and computer_move == 'SCISSORS') or (user_move == 'SCISSORS' and computer_move == 'PAPER') or (user_move == 'PAPER' and computer_move == 'ROCK'):
        print("You win!")
        wins = wins + 1
    else:
        print("You lost!")
        losses = losses + 1
    
    print("WINS-", wins, "; LOSSES-", losses, "; TIES-", ties)    





