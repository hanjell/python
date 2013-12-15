# Angel Gonzalez
# hello_world.py
# Oct 25, 2013

while True:
	player1 = raw_input("Player1? ")
	if player1 == "rock" or player1 == "scissors" or player1 == "paper":
		break;
	else:
		print "This is not a valid object selection"

while True:
	player2 = raw_input("Player2? ")
	if player2 == "rock" or player2 == "scissors" or player2 == "paper":
		break;
	else:
		print "This is not a valid object selection"

if player1 == player2:
	print "Tie"
elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
	print "Player1 wins."
elif (player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
	print "Player2 wins."
else:
	print "Not possible"