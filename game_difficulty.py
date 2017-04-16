#user decides on difficulty level here
choose_difficulty = False
while choose_difficulty == False:
	user_input = raw_input("Please select a game difficulty- easy, medium, or hard: ")
	if user_input == "easy":
		print "You chose easy."
		choose_difficulty = True
	elif user_input == "medium":
		print "You chose medium."
		choose_difficulty = True
	elif user_input == "hard":
		print "You chose hard."
		choose_difficulty = True
	else:
		print "That's not an option. Try again."


