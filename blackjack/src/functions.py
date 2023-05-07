import random


def deal_card():
    '''Return 1 card from the card deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw 🔥\n"
    elif dealer_score == 0:
        return "Dealer has blackjack! 😩\n"
    elif player_score == 0:
        return "You've won with a blackjack! 😀\n"
    elif player_score > 21:
        return "Dealer wins, you went over 21 😩\n"
    elif dealer_score > 21:
        return "You've won, dealer went over 21 😀\n"
    elif player_score > dealer_score:
        return "You've won 🥳\n"
    else:
        return "Dealer wins 😠\n"


def print_score(player_cards, dealer_cards):
    print(f"\n    Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"    Dealer's first card: {dealer_cards[0]}")


def print_final_score(player_cards, dealer_cards):
    print(f"\n    Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"    Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n")
