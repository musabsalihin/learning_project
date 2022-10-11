#blackjack rule
#ace can be considered as 1 or 11
#jack,queen and king is 10
#player get 2 cards at the beginning
#can start_game either to HIT one more card from deck
#sum of card closest to 21 win
#but if over 21 BUST, lose
#and after open if <17 must hit another card
#if same sum of card then DRAW
 
import random
import os

def printAll(mytotal,dealertotal):
    print(f"Your card: {my_card}, total score: {mytotal}")
    print(f"Computer's card: {dealer_card}, total : {dealertotal}\n")

def checkAce(mytotal_card):
    if my_card[mytotal_card-1] == card[0]:
        if mytotal>10:
            my_card[mytotal_card-1] = 1

def dealcard(mytotal):
    my_card.append(card[random.randint(0,12)])
    checkAce(mytotal_card)
    mytotal += my_card[mytotal_card-1]
    return mytotal

def compare_card(mytotal,dealertotal):
    if dealertotal<17:
        dealer_card.append(card[random.randint(0,12)])
        dealertotal += dealer_card[2]

    if dealertotal>21:
        printAll(mytotal,dealertotal)
        print("Dealer is BUSTED. You win")
        return True

    if mytotal<=21 and dealertotal<=21:
        printAll(mytotal,dealertotal)
        if mytotal>dealertotal:
            print("You win")
        elif mytotal == dealertotal:
            print("Draw")
        else:
            print("You lose")
        return True

card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
start_game = input("Do you want to play blackjack?'y' or 'n'.")
if start_game == 'y':
    play = True
elif start_game == 'n':
    play = False

while play is True:
    my_card = []
    dealer_card  = []

    mytotal = 0
    dealertotal = 0
    mytotal_card = 2

    my_card.append(random.choice(card))
    my_card.append(random.choice(card))

    dealer_card.append(random.choice(card))
    dealer_card.append(random.choice(card))

    for n in my_card:
        mytotal += n
        
    for n in dealer_card:
        dealertotal += n

    game_over = False
    while game_over is False:
        print(f"Your card: {my_card}, current score: {mytotal}")
        print(f"Computer's first card: {dealer_card[0]}")
        hit_card = input("\nType 'y' to get another card, type 'n' to pass: ")

        if hit_card == 'y':
            checkAce(mytotal_card)
            mytotal_card+=1
            mytotal = dealcard(mytotal)        
            if mytotal>21:
                printAll(mytotal,dealertotal)
                print("BUSTED. You lose")
                break
            os.system('cls')

        else:
            os.system('cls')
            game_over = compare_card(mytotal,dealertotal)
    
    start_game = input("Do you want to play blackjack?'y' or 'n'.")
    if start_game == 'y':
        os.system('cls')
        play = True
    elif start_game == 'n':
        play = False