#Submision 12: Rock-Paper-Scissors

player1 = input()
player2 = input()

rock = "rock"
paper = "paper"
scissors = "scissors"

# conditions for a draw
if player1 == player2:
    print("Tie")
#conditions for player1 to win:
    #player1 = rock and player2 = scisors
    #player1 = paper and player2 = rock
    #player1 = scisors and player2 = paper
#else player2 
 
elif player1 == rock and player2 == scissors:
    print("Player 1 wins")
elif player1 == paper and player2 == rock:
    print("Player 1 wins")
elif player1 == scissors and player2 == paper:
    print("Player 1 wins")
else:
    print("Player 2 wins")