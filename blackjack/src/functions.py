import random


def deal_card(cards):
    result = random.choice(cards)
    return result


def print_score(player_cards, player_score, dealer_cards):
    print(f"\n    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Dealer's first card: {dealer_cards[0]}")


def print_final_score(player_cards, player_score, dealer_cards, dealer_score):
    print(f"\n    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Dealer's final hand: {dealer_cards}, final score: {dealer_score}\n")
