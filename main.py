import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def randomCard():
    card = random.choice(list(cards))
    return card

def calculated_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(player_score, gamemaster_score):
    if gamemaster_score == player_score:
        print("It is a tie!")
    elif gamemaster_score == 0:
        print("You lose, Gamemaster had a blackjack ")
    elif player_score == 0:
        print("You win, You had a blackjack")
    elif player_score > 21:
        print("You lose!, went over the limit")
    elif gamemaster_score > 21:
        print("You win, Gamemaster went over the limit  ")
    elif gamemaster_score > player_score:
        print("You lose! The Game master had more points than the player score!")
    elif gamemaster_score < player_score:
        print("You win!, you had more points than the gamemaster")




def blackjack():
    player = []
    gamemaster = []
    game_over = True
    print("Welcome to the Blackjack!")
    print(art.logo)
    for _ in range(2):
        player.append(randomCard())
        gamemaster.append(randomCard())

    player_score = calculated_scores(player)
    gamemaster_score = calculated_scores(gamemaster)
    while game_over == True:
        if player_score == 0 or gamemaster_score == 0:
            compare(player_score, gamemaster_score)
            game_over = False
        print(f" Your cards are ", player," and your score is ", player_score)
        print(f" One of the cards drawn by the gamemaster is", gamemaster[0])
        if player_score == 0 or gamemaster_score == 0 or player_score > 21:
            game_over = False
            break
        decision_card = input("\n Do you want to draw another card (y/n):")
        if decision_card == "y":
            player.append(randomCard())
        else:
            game_over = False
        player_score = calculated_scores(player)
        if player_score > 21:
            game_over = False
    if player_score <= 21 and player_score != 0:
      while gamemaster_score != 0 and gamemaster_score < 17:
           gamemaster.append(randomCard())
           gamemaster_score = calculated_scores(gamemaster)


    print(f" Your cards are ", player, " and your score is ", player_score)
    print(f" Gamemaster score is ", gamemaster_score ,"and the gamemaster card is",gamemaster)
    compare(player_score, gamemaster_score)


choice = input(" Do you want to play a game of Blackjack?(y/n):")
if choice == "y":
    print(" \n" *100)
    blackjack()

while input("\n Do you want to restart the game (y/n):") == "y":
        print(" \n" *100)
        blackjack()
