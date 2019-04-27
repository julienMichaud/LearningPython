print ("Rock")
print ("Paper")
print ("Scissors")

player1 = input ("make your move, player1 ")
player2 = input ("make your move, player2 ")

if player1 == "Rock" and player2 == "Scissors":
    print (" player1 win")

elif player1 == "Rock" and player2 == "Paper"":
    print (" player2 win")

elif player1 == player2:
    print (" draw")

else:
    print (" something went wrong")