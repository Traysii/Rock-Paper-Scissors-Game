from random import randint


player = input("Select Rock, Paper or Scissors?: ")
select = ['Rock', 'rock', 'Paper', 'paper', 'Scissors', 'scissors']
while player not in select :
	print("Wrong type!")
	player = input("Select Rock, Paper or Scissors?: ")

computer = randint(0,2)
print("Your select: " + player)
if computer == 0:
	computer = "Rock"
if computer == 1:
	computer = "Paper"
if computer == 2:
	computer = "Scissors"
print("Computer selects : " + computer)
print("---")

if player == computer:
	print("Draw")
else:
	if player == "Rock" or player == "rock":
		if computer == "Paper":
			print("You Lose")
		else:
			print("You Win")
	elif player == "Paper" or player == "paper":
		if computer == "Rock":
			print("You Win")
		else:
			print("You Lose")
	else:
		if computer == "Rock":
			print("You Lose")
		else:
			print("You Win")