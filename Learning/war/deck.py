import random

def initDeck():
    """
        this returns a new deck of 52 cards
    """
    deck = set()

    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    faces = ["Jack", "Queen", "King", "Ace"]
    numbered = [2,3,4,5,6,7,8,9,10]

    for suit in suits:
        for card in faces + numbered:
            deck.add(f"{card} of {suit}")

    return deck


def draw(deck):
    """
        given a deck of cards, this removes a card from the deck and returns that card to the caller
    """
    if len(deck) == 0:
        return
    card = random.choice(list(deck))
    deck.remove(card)
    return card

def deal(deck, number_of_players):
    """
        given a deck and a number of players, deal cards to the players
        until all the cards are in the players hands

        may want to modify this to specify the number of cards dealt to each player
    """
    player_hands = [set(), set()]

    while len(deck) > 0:
        for p in range(number_of_players):
            card = draw(deck)
            player_hands[p].add(card)

    return player_hands

    
def game_over(hands):
    """
    game is over when only one hand has cards
    """
    players_with_cards = 0

    for hand in hands:
        if len(hand) > 0:
            players_with_cards += 1

    return players_with_cards > 1


def play_round(hands):
    #todo: consider switching to dictionaries to assist with keeping track of hands and drawn by player
    drawn = []
    for hand in hands:
        #draw two cards from each hand
        faceup_card  = draw(hand)
        facedown_card  = draw(hand)

        drawn.append((faceup_card, facedown_card))

    high_card_val = 0
    high_indexes = []

    #compare first card of cards drawn from each player 
    for _ in len(drawn):
        played_card_val = get_val(drawn[_].faceup_card)

        if played_card_val > high_card_val:
            high_card_val = played_card_val
            high_indexes = [_]
        elif played_card_val == high_card_val:
            high_indexes.append(_)
    
    #if cards are the same value do war rounds until no more cards or player has higher card value
    #while len(high_indexes) > 1:
        


    #add all cards to player that has the higher value
    for card in drawn:
        hands[high_indexes[0]].add(card)

    return

def play_war(hands):
    #todo: do war
    return

def get_val(card):
    face_dict = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    card_val = card.split()[0]
    int_val = 0

    try:
        int_val = int(card_val)
    except:
        int_val = face_dict[card_val]

    return int_val