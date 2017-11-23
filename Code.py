from random import *

dealval = 0
playval = 0
newcard = 0
dealcard = 0
chips = 500
losses = 0
wins = 0

def ace():
    global playval
    global newcard
    if playval + 11 < 22:
        playval =+11
    else:
        playval =+ 1
    options()

def bust():
    global losses
    global currentbet
    global chips
    print("Bust!")
    print("New round.")
    print(" ")
    chips = -currentbet
    losses = +1
    gamestart()

def stand():
    dealerturn()

def hit():
    global playval
    global newcard

    print("Your new card is a")
    newcard = print(randint(2, 10) or "ace" or "Jack" or "queen" or "king")
    cardtotal()
    if playval > 21:
        bust()
    else:
        print("Your total", playval)
        options()

def cardtotal():
    global newcard
    global playval
    int(playval)

    if newcard == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
        playval = playval + newcard
    if newcard == "queen":
        playval = playval + 10
    if newcard == "king":
        playval = playval + 10
    if newcard == 'Jack':
        playval = playval + 10
    if newcard == "ace":
        ace()

def options():
    option = input("Would you like to hit, stand, or double down?")
    if option == "stand":
        stand()
    if option == "hit":
        hit()
    if option == "double down":
        double()
    else:
        print("Please select a valid option")
        print("")
        options()

def gamestart():
    global chips
    global wins
    global losses

    print("")
    print("You have", chips, "chips")
    print("")
    print("You have", wins, "wins and", losses, "losses")
    bets()

def bets():
    global chips
    global currentbet
    print("")
    currentbet = int(input("How much would you like to bet?"))
    if currentbet > chips or currentbet < 1:
        print("You can't do that.")
        bets()
    else:
        print("")
        draw()

def draw():
    global playval
    global dealval
    global newcard
    global chips
    global currentbet
    print("You have two cards. They are a")
    newcard = print(randint(2,10) or "ace" or "Jack" or "queen" or "king")
    cardtotal()
    print("and a")
    newcard = print(randint(2,10) or "ace" or "Jack" or "queen" or "king")
    cardtotal()
    if playval == 21:
        print("BlackJack!")
        chips = +currentbet*1.5
        print(" ")
        print("New round")
        gamestart()
    else:
        print("")
        print("Your card total is", playval)
        print("")

        options()

def start():
    print("Welcome to text-based BlackJack!")
    print(" ")
    if input("Do you want to start?") == "yes":
        gamestart()
    else:
        print("Goodbye")

start()