import src.functions as func
from art import tprint
import os, sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0
player_is_playing = True
dealer_is_playing = True


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")
os.system('cls||clear')


if play_game == "y":
    tprint("blackjack")
    for i in range(2):
        player_cards.append(func.deal_card(cards))
        dealer_cards.append(func.deal_card(cards))
        player_score = sum(player_cards)
        dealer_score = sum(dealer_cards)
    func.print_score(player_cards, player_score, dealer_cards)
else:
    sys.exit()


while player_is_playing:

    if player_score == 21:
        print("\nYou've won")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        player_is_playing = False
        dealer_is_playing = False
    elif dealer_score == 21:
        print("\nDealer wins")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        player_is_playing = False
        dealer_is_playing = False
    elif player_score > 21:
        print("\nDealer wins")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        player_is_playing = False
        dealer_is_playing = False
    elif 11 in player_cards:
        player_score = ((player_score - 11) + 1)
        if player_score > 21:
            print("\nDealer wins")
            func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
            player_is_playing = False
            dealer_is_playing = False
        else:
            get_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            if get_card == "y":
                player_cards.append(func.deal_card(cards))
                player_score = sum(player_cards)
                func.print_score(player_cards, player_score, dealer_cards)
            else:
                player_is_playing = False
    else:
        get_card = input("\nType 'y' to get another card, type 'n' to pass: ")
        if get_card == "y":
            player_cards.append(func.deal_card(cards))
            player_score = sum(player_cards)
            func.print_score(player_cards, player_score, dealer_cards)
        else:
            player_is_playing = False


while dealer_is_playing:

    while dealer_score < 17:
        dealer_cards.append(func.deal_card(cards))
        dealer_score = sum(player_cards)
    
    if dealer_score > 21:
        print("\nYou've won")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        dealer_is_playing = False
    elif player_score == dealer_score:
        print("\nDraw")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        dealer_is_playing = False
    elif player_score < dealer_score:
        print("\nDealer wins")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        dealer_is_playing = False
    elif player_score > dealer_score:
        print("\nYou've won")
        func.print_final_score(player_cards, player_score, dealer_cards, dealer_score)
        dealer_is_playing = False
    else:
        print("Error")
