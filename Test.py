from Deck import Deck
from Player import Player

def initializePlayers():
    numPlayers = int(input("How many players? "))  # check constraints, >=1, <=5
    players = []
    for i in range(numPlayers):
        playerName = input("Name of player " + str(i+1) + ": ")
        players.append(Player(playerName))
    return players


def displayPlayerInfo(players):        
    for x in players:
        print(x.getName() + " - $" + str(x.getBalance()))
    return

def collectWagers(players):
    wagers = []
    for x in players:  # check for not-enough-money-to-cover-the-bet, too
        if x.getBalance() > 0 and x.getBalance() <= 5:
            wagers.append(int(input("Bet for " + x.getName() + " (min bet is $" + str(x.getBalance()+"): "))))
        elif x.getBalance() > 5:
            wagers.append(int(input("Bet for " + x.getName() + " (min bet is $5): ")))
    return wagers

def showWagers(players, wagers):
    numPlayers = len(players)
    for i in range(numPlayers):
        print(players[i].getName() + " wagered $" + str(wagers[i]))
    return
    
def getScoreForHand(hand):
    totalHandScore = 0
    sortedHand = sorted(hand, key=lambda x: x.getCardValue(), reverse=False)    # have to sort by  value to make sure aces are properly counted
    for card in sortedHand:
        cardScore = card.getCardValue()
        if cardScore > 10:
            cardScore = 10

        if totalHandScore + 11 > 21 and cardScore == 1:  # sometimes aces are 11s, sometimes 1s
            cardScore = 1
        elif cardScore == 1:
            cardScore = 11
        totalHandScore += cardScore
    return totalHandScore

def showHand(hand):
    print("Total score: " + str(getScoreForHand(hand)))
    for card in hand:
        print(card)
    return

def showAllCards(players, hands):
    for i in range(len(players)):
        print(players[i].getName() + " has cards: ")
        showHand(hands[i])
        print()
    return


# welcome message
print("Hello World and welcome to Jensen Blackjack")

# get the number of players and initialize the player array
players = initializePlayers()
numPlayers = len(players)
print(str(numPlayers))

# make sure we got them all
displayPlayerInfo(players)

# Initialize the deck
curDeck = Deck()

# Get everybody who's still playing's bets
#wagers = collectWagers(players)
#showWagers(players, wagers)


# Initialize the hands variable
hands = [[]]
for i in range(numPlayers):
    hands.append([])
    
# deal first round of cards to every player, then to dealer, then repeat
for i in range(3):
    for hand in hands:
        hand.append(curDeck.draw())
dealersHand = hands[numPlayers]

# show player's, then dealer's hands
showAllCards(players, hands)
print("Dealer has: ")
showHand(dealersHand)

#card = curDeck.draw()
#print(card)
