##HANGMAN##
import random
#list of words for the game
word = "avoid halting page airplane middle " \
       "house sprout plough duck vulgar tough large " \
       "ripe copper collect eatable elbow wacky bath " \
       "thin battle flat sincere bashful owe roof grandfather " \
       "boorish playground trousers watery abnormal lie vivacious " \
       "nice tow iron ratty spoil crack provide ring stiff dreary " \
       "tooth skin oatmeal experience entertain yummy"

#sort word list in array
word_list = word.split()

#random picking word for game
random_word = word_list[random.randint(0, 49)]
NumOfLetter = len(random_word)
#print(random_word)
life = 5
blank = ""
guess_word = ""

for n in range(NumOfLetter):
    blank += "_ "
print(blank)
guess_word = blank.split()

while NumOfLetter > 0 and life > 0:
    ##print(NumOfLetter)
    ##print(life)
    print(guess_word)
    count = 0
    sen_count = 0
    letter_guess =input("Please guess a letter for the word: ").lower()

    for n in range(len(random_word)):
        #right letter guessed
        if letter_guess == random_word[n]:
            guess_word[n] = letter_guess
            NumOfLetter -= 1
            sen_count += 1
        #wrong letter guessed
        else:
            if guess_word[n] != "_":
                continue
            else:
                guess_word[n] = "_"
    #################life UI########################
    if sen_count == 0:
        life -= 1
        if life == 4:
            print(".......  -----............\n"
                  ".......  0   |............\n"
                  ".......      |............\n"
                  ".......      |............\n"
                  ".......      |............\n"
                  ".......    +++++..........\n\n")

        elif life == 3:
            print(".......  -----............\n"
                  ".......  0   |............\n"
                  "....... /|\  |............\n"
                  ".......      |............\n"
                  ".......      |............\n"
                  ".......    +++++..........\n\n")
        elif life == 2:
            print(".......  -----............\n"
                  ".......  0   |............\n"
                  "....... /|\  |............\n"
                  ".......  |   |............\n"
                  ".......      |............\n"
                  ".......    +++++..........\n\n")
        elif life == 1:
            print(".......  -----............\n"
                  ".......  0   |............\n"
                  "....... /|\  |............\n"
                  ".......  |   |............\n"
                  "....... /    |............\n"
                  ".......    +++++..........\n\n")
        else:
            print(".......  -----............\n"
                  ".......  0   |............\n"
                  "....... /|\  |............\n"
                  ".......  |   |............\n"
                  "....... / \  |............\n"
                  ".......    +++++..........\n\n")
            ##################################
if life <= 0:
    #when player lose
    print("\n\nYou Lost")
    print(f"The answer is {random_word}")

answer = ""
for n in range(0, len(random_word)):
    answer += guess_word[n]
#when player win
if NumOfLetter == 0:
    print(f"\n\nYou did a great job. Your answer is correct. {answer}.")
