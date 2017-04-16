paragraph_1 = """A 1 is created with the def keyword. You specify the inputs a 1 takes by
adding 2 separated by commas between the parentheses. 1s by default return 
3 if you don't specify the value to return. 2 can be standard data types 
such as string, number, dictionary, tuple, and 4 or 
can be more complicated such as objects and lambda functions."""

para1_dict = {1 : "function", 2 : "variables", 3 : "none", 4 : "lists"} #answers to the number blanks in the paragraph

def replace_words(nlist, word, new_word):
	nlist = " ".join(nlist)
	string = nlist.replace(word, new_word)
	string = string.split()
	return string


print paragraph_1
print
for key, value in para1_dict.iteritems(): #goes through each item in the dictionary
	for turn in range(3):
		paralist = paragraph_1.split()
		print "You have 3 tries for each blank. This is try #" + str(turn + 1) + "."
		user_answer = raw_input ("What word should be substituted for " + str(key) + "? ").lower()
		print
		if user_answer == para1_dict[key]:
			print "That's correct!"
			print
			print " ".join(replace_words(paralist, str(key), para1_dict[key])) #converts list back into string
			print
			break
		else:
			print "That's incorrect."
			print
		if turn == 2:
			print "The correct answer is " + para1_dict[key] + "."
			print
			print " ".join(replace_words(paralist, str(key), para1_dict[key]))
			print
