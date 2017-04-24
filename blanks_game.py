blanks = ["_1_", "_2_", "_3_", "_4_"]
#quiz paragraphs and answers
para1 = """_1_ wrote the opera The Marriage of Figaro. _2_ wrote the Eroica Symphony. 
_3_ is best known for the ballet The Rite of Spring. _4_ composed Appalachian Spring."""
answers1 = ["Mozart", "Beethoven", "Stravinsky", "Copland"]
para2 = """_1_ is the home of the Liberty Bell. _2_ is known for the Space Needle. 
"Do you know what is means to miss _3_?" is a famous song. _4_ is the capital of Illinois."""
answers2 = ["Philadelphia", "Seattle", "New Orleans", "Springfield"]
para3 = """_1_ are red, _2_ are blue. "When _3_ last in the dooryard bloom'd" is a poem written by
Walt Whitman. "The _4_" was written by William Wordsworth."""
answers3 = ["Roses", "violets", "lilacs", "daffodils"]

def fill_blanks(word, blanks): #adapted from Mad Libs code, goes through quiz to find blanks
    for blank in blanks:
        if blank in word:
            return blank
    return None

def check_answers(answer): #checks whether user's answer is correct
    check = False
    while check == False:
        for turn in range(3): # 3 tries per blank
            user_input = raw_input("What is the correct answer? ")
            if user_input == answer:
                print "Correct!"
                return answer
            else:
                print "Incorrect."
            if turn == 2:
                print "The correct answer is " + answer + "."
                return answer


def play_game(paragraph, blanks, answers): #adapted from Mad Libs, takes user input and prints answers
    print paragraph 
    replaced = []
    paragraph = paragraph.split()
    counter = 0
    for word in paragraph:
        replacement = fill_blanks(word, blanks)
        if replacement != None:
            print "Fill in the answer for blank #" + str(counter + 1) + "."
            response = check_answers(answers[counter])
            newword = word.replace(replacement, response)
            replaced.append(newword)
            phrase = " ".join(replaced)
            remainder = " ".join(paragraph)
            print phrase + remainder[remainder.find("_"+str(counter + 1)+"_") + len(word):]
            #prints answers within the quiz as answers are given
            counter += 1
        else:
            replaced.append(word)
            phrase = " ".join(replaced)

def game_start(): #user to choose which subject to be quizzed on
    print "Let's play fill in the blanks! You get three tries per blank."
    choose_difficulty = False
    while choose_difficulty == False:
        user_input = raw_input("Please select a subject- composers, cities, or flowers: ").lower()
        if user_input == "composers":
            print "You chose composers. Answer with last names only."
            choose_difficulty = True
            play_game(para1, blanks, answers1)
        elif user_input == "cities":
            print "You chose cities."
            choose_difficulty = True
            play_game(para2, blanks, answers2)
        elif user_input == "flowers":
            print "You chose flowers."
            choose_difficulty = True
            play_game(para3, blanks, answers3)
        else:
            print "That's not an option. Try again."

game_start()
