import src.functions as func
from art import tprint
import os


def play_game():

    player_cards = []
    dealer_cards = []
    is_game_over = False

    tprint("blackjack")

    for _ in range(2):
        player_cards.append(func.deal_card())
        dealer_cards.append(func.deal_card())

    while not is_game_over:

        player_score = func.calculate_score(player_cards)
        dealer_score = func.calculate_score(dealer_cards)
        func.print_score(player_cards, dealer_cards)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            get_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            if get_card == "y":
                player_cards.append(func.deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(func.deal_card())
        dealer_score = func.calculate_score(dealer_cards)

    func.print_final_score(player_cards, dealer_cards)
    print(func.compare(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ") == "y":
    os.system('cls||clear')
    play_game()
