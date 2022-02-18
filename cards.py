# =====================================================================
# CARDS.PY
# A library providing functions for simple card games.
# Remember to import this library at the start of your program.
# =====================================================================

# =====================================================================
# PROVIDED FUNCTIONS
# DO NOT MODIFY THESE FUNCTIONS UNLESS INSTRUCTED TO DO SO!
# =====================================================================
# Creates a deck of cards, consisting of R ranks in S suits.
# If arguments not provided, uses default values of 13 ranks in 4 suits.
# Each card is a tuple of the form (rank, suit), where each rank/suit is an integer.
# Ranks and suits can be assigned base on the needs of your program.
# Jokers can be added. Jokers are ranked (if needed) with a suit of -1.
# Returns the deck of cards as a list, ascending by rank then suit.


def makeDeck(numRanks=13, numSuits=4, numJokers=0):
    deck = []
    for rank in range(1, numRanks + 1):
        for suit in range(1, numSuits + 1):
            deck.append((rank, suit))
    if numJokers > 0:
        for count in range(1, numJokers + 1):
            deck.append((count, -1))
    return deck


# Gets one or more cards from the top of a stock of cards.
# If numCards is specified, returns that many cards.
# If a single card is specified, returns a tuple (the card).
# If more than one card is specified, returns a list of tuples.
# If unable to get enough cards, returns a tuple containing NO CARD.
def dealCards(stock, numCards=1):
    if len(stock) < numCards:
        print("INSUFFICIENT CARDS AVAILABLE TO DEAL.")
        return ("NO", "CARD")
    elif numCards == 1:
        return stock.pop(0)
    else:
        cards = []
        for card in range(numCards):
            cards.append(stock.pop(0))
        return cards


# =====================================================================
# END OF PROVIDED FUNCTIONS
# =====================================================================

# =====================================================================
# MANDATORY FUNCTIONS
# COMPLETE THE FOLLOWING FUNCTIONS, ACCORDING TO THE DESCRIPTIONS.
# =====================================================================
# Obtain the rank of a card, e.g. "Jack"
def getRank(card):
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    rank = card[0]
    return ranks[rank - 1]


# Obtain the suit of a card, e.g. "Spades"
def getSuit(card):
    suits = ["Clubs", "Diamonds", "Hearts", "Spades", "Joker", ""]
    suit = card[1]
    return suits[suit - 1]


# Obtain the full name of a card, e.g. "Jack of Spades"
def getCardName(card):
    if getSuit(card) != "Joker":
        cardName = str(getRank(card)) + " of " + str(getSuit(card))
        return cardName
    else:
        return "Joker"


# Displays a player's hand of cards, in a nicely formatted manner.
def showHand(playerHand):
    hand = []
    jokerOne = None
    jokerTwo = None
    if (1, -1) in playerHand:
        jokerOne = playerHand.pop(playerHand.index((1, -1)))
    if (2, -1) in playerHand:
        jokerTwo = playerHand.pop(playerHand.index((2, -1)))
    playerHand.sort()
    if jokerOne == (1, -1):
        playerHand.append(jokerOne)
    if jokerTwo == (2, -1):
        playerHand.append(jokerTwo)
    for card in playerHand:
        hand.append(f"({playerHand.index(card) + 1}) {getCardName(card)}")
    x = "\n".join(hand)
    return x


# =====================================================================
# END OF MANDATORY FUNCTIONS
# =====================================================================

# =====================================================================
# ADDITIONAL FUNCTIONS
# ADD ANY CARD-SPECIFIC FUNCTIONS HERE.
# =====================================================================
import utilities


# Creates a list of playable cards in the selected hand
def cardsPlayable(hand, discardTop):
    cards = []
    for card in hand:
        if card[1] == -1:
            cards.append(card)
        elif card[0] > discardTop[0] or card[1] == discardTop[1]:
            cards.append(card)
    return cards


# Creates a list of playable groups in the selected hand
def checkGroups(hand, playableCards):
    groups = []
    dupeHand = hand.copy()
    for playableCard in playableCards:
        cards = []
        # print(playableCard)
        # print(dupeHand)
        # print("\n")
        for card in dupeHand:
            # print(card)
            if (card[0] == playableCard[0] and (card[1] != -1 and playableCard[1] != -1)) or \
                    (card[1] == -1 and playableCard[1] == -1):
                cards.append(card)
                dupeHand[dupeHand.index(card)] = (0, 0)
                # print(cards)
                # print("!!")
        if len(cards) > 1:
            groups.append(cards)
        # print(cards)
        # print("\n")
    return groups


# Creates a list of the playable cards in a hand which can start a run
def checkRuns(hand, playableCards):
    runs = []
    for playableCard in playableCards:
        if playableCard[1] != -1:
            cards = [playableCard]
            while True:
                oldLast = cards[-1]
                for card in hand:
                    if card[0] == (cards[-1])[0] + 1:
                        cards.append(card)
                        break
                if cards[-1] == oldLast:
                    break
            if len(cards) > 2:
                runs.append(cards[0])
    return runs


# Checks whether any runs or groups are playable from a selected hand of cards
def checkRunGroups(hand, playableCards):
    if checkGroups(hand, playableCards) == [] and checkRuns(hand, playableCards) == []:
        return False
    elif checkGroups(hand, playableCards) and checkRuns(hand, playableCards):
        return True
    elif checkGroups(hand, playableCards):
        return "groups"
    elif checkRuns(hand, playableCards):
        return "runs"


# Neatly formats a list of playable groups to be printed
def printGroups(groups):
    groups.sort()
    namedList = []
    for group in groups:
        groupList = []
        for card in group:
            groupList.append(getCardName(card))
        namedList.append(f"({groups.index(group) + 1}) {', '.join(groupList)}")
    finalList = "\n".join(namedList)
    return finalList


# Moves group played from hand into discard pile and returns a string of cards played
def printPlayedGroup(hand, groupPlayed, discardPile):
    playedCards = []
    for card in groupPlayed[:-1]:
        hand.pop(hand.index(card))
        discardPile.append(card)
        playedCards.append(getCardName(card))
    discardPile.append(hand.pop(hand.index(groupPlayed[-1])))
    finalList = ", The ".join(playedCards)
    return finalList


# Prompts the player to add a playable card to their run. Returning false plays the run
def buildRun(runCard, hand, run):
    addableCards = []
    for card in hand:
        if card[0] == runCard[0] + 1:
            addableCards.append(card)

    if len(run) > 2:
        if len(addableCards):
            choice = utilities.intput(f"Please choose a card below to continue your run, or 0 to play "
                                      f"your current run: \n{showHand(addableCards)}\n> ",
                                      "Please enter one of the number listed above. ", 0,
                                      len(addableCards), "Please enter one of the number above. ")
            if choice == 0:
                return False
            else:
                runAdd = addableCards[choice - 1]
        else:
            print("Your run has automatically been played as you have no more cards which can continue the run.")
            return False
    else:
        runAdd = addableCards[utilities.intput(f"Please choose a card below to continue your run:"
                                               f"\n{showHand(addableCards)}\n> ",
                                               "Please enter one of the number listed above. ", 1,
                                               len(addableCards), "Please enter one of the number above. ") - 1]
    return runAdd


# Prints the cards in the current run
def printCurrentRun(currentRun):
    runCards = []
    for card in currentRun:
        runCards.append(getCardName(card))
    finalList = ", ".join(runCards)
    return finalList
