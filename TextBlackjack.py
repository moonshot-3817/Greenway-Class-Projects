from random import *
import tkinter as tk

dealval = 0
playval = 0
newcard = 0
dealcard = 0
chips = 500
losses = 0
wins = 0

def double():
    global currentbet
    global chips
    global playval
    global newcard
    global newvar

    currentbet = currentbet*2
    print(" ")
    print("Your new bet is",currentbet)
    newvar = choice([2,3,4,5,6,7,8,9,10,"ace","Jack","queen","king"])
    if newvar == 2:
        newcard = 2
    if newvar == 3:
        newcard = 3
    if newvar == 4:
        newcard = 4
    if newvar == 5:
        newcard = 5
    if newvar == 6:
        newcard = 6
    if newvar == 7:
        newcard = 7
    if newvar == 8:
        newcard = 8
    if newvar == 9:
        newcard = 9
    if newvar == 10:
        newcard = 10
    if newvar == "queen":
        newcard = 10
    if newvar == "Jack":
        newcard = 10
    if newvar == "king":
        newcard = 10
    if newvar == "ace":
        newcard = 11
    print("Your new card is")
    print(newvar)
    print(" ")
    print("Your total is")
    playval = playval + newcard
    print(playval)
    if playval < 22:
        stand()
    else:
        bust()

def bust():
    global losses
    global currentbet
    global chips
    print("Bust!")
    print("New round.")
    print(" ")
    chips = chips - currentbet
    losses = losses + 1
    gamestart()

def stand():
    global dealvar
    global dealval
    global losses
    global playval
    global wins
    global currentbet
    global chips
    if playval == 21:
        print("You win!")
        wins = wins+1
        chips = chips + currentbet
        print("New round")
        gamestart()
    else:
        print("")
        print("It is the dealer's turn now.")
        print("They flip over their other card, and you see it is a")
        print(dealvar)
        print("Their total is")
        print(dealval)
        print(" ")
        dealerturn()

def dealerturn():
    global dealvar
    global dealval
    global playval
    global wins
    global losses
    global newcard
    global chips
    global currentbet
    if dealval < 18:
        print(" ")
        print("The dealer hits.")
        newvar = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "Jack", "queen", "king"])
        print("Their new card is a",newvar)
        if newvar == 2:
            newcard = 2
        if newvar == 3:
            newcard = 3
        if newvar == 4:
            newcard = 4
        if newvar == 5:
            newcard = 5
        if newvar == 6:
            newcard = 6
        if newvar == 7:
            newcard = 7
        if newvar == 8:
            newcard = 8
        if newvar == 9:
            newcard = 9
        if newvar == 10:
            newcard = 10
        if newvar == "queen":
            newcard = 10
        if newvar == "Jack":
            newcard = 10
        if newvar == "king":
            newcard = 10
        if newvar == "ace":
            if playval + 11 > 21:
                newcard = 1
            else:
                newcard = 11
        dealval = dealval + newcard
        if dealval > 21:
            print("The dealer busts!")
            wins = wins + 1
            chips = chips +currentbet
            print("New round")
            gamestart()
        else:
            print("The dealer's total is", dealval)
            dealerturn()
    else:
        print("The dealer stands with a total of", dealval)
        if playval>dealval:
            print("")
            print("You win!")
            chips = chips + currentbet
            print("New round")
            wins = wins +1
            gamestart()
        if playval<dealval:
            print("")
            print("You lose")
            chips = chips - currentbet
            print("New round")
            losses = losses +1
            gamestart()
        if playval == dealval:
            print("")
            print("Push")
            print("New round")
            gamestart()

def hit():
    global playval
    global newcard

    print("Your new card is a")
    newvar = choice([2,3,4,5,6,7,8,9,10,"ace","Jack","queen","king"])
    print(newvar)
    if newvar == 2:
        newcard = 2
    if newvar == 3:
        newcard = 3
    if newvar == 4:
        newcard = 4
    if newvar == 5:
        newcard = 5
    if newvar == 6:
        newcard = 6
    if newvar == 7:
        newcard = 7
    if newvar == 8:
        newcard = 8
    if newvar == 9:
        newcard = 9
    if newvar == 10:
        newcard = 10
    if newvar == "queen":
        newcard = 10
    if newvar == "Jack":
        newcard = 10
    if newvar == "king":
        newcard = 10
    if newvar == "ace":
        if playval + 11 > 21:
            newcard = 1
        else:
            newcard = 11
    playval = playval + newcard
    if playval > 21:
        bust()
    else:
        print("Your total", playval)
        options()

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
    global dealvar
    global playval
    global dealval
    global newcard
    global chips
    global currentbet
    global wins
    global losses
    print("You have two cards. They are a")
    dealval = 0
    playval = 0
    newcard = 0
    newvar = 0
    newvar = choice([2,3,4,5,6,7,8,9,10,"ace","Jack","queen","king"])
    if newvar == 2:
        newcard = 2
    if newvar == 3:
        newcard = 3
    if newvar == 4:
        newcard = 4
    if newvar == 5:
        newcard = 5
    if newvar == 6:
        newcard = 6
    if newvar == 7:
        newcard = 7
    if newvar == 8:
        newcard = 8
    if newvar == 9:
        newcard = 9
    if newvar == 10:
        newcard = 10
    if newvar == "queen":
        newcard = 10
    if newvar == "Jack":
        newcard = 10
    if newvar == "king":
        newcard = 10
    if newvar == "ace":
        newcard = 11
    print(newvar)
    playval = playval + newcard

    print("and a")

    newvar = choice([2,3,4,5,6,7,8,9,10,"ace","Jack","queen","king"])
    if newvar == 2:
        newcard = 2
    if newvar == 3:
        newcard = 3
    if newvar == 4:
        newcard = 4
    if newvar == 5:
        newcard = 5
    if newvar == 6:
        newcard = 6
    if newvar == 7:
        newcard = 7
    if newvar == 8:
        newcard = 8
    if newvar == 9:
        newcard = 9
    if newvar == 10:
        newcard = 10
    if newvar == "queen":
        newcard = 10
    if newvar == "Jack":
        newcard = 10
    if newvar == "king":
        newcard = 10
    if newvar == "ace":
        if playval + 11 > 21:
            newcard = 1
        else:
            newcard = 11
    playval = playval + newcard

    print(newvar)

    newvar = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "Jack", "queen", "king"])
    if newvar == 2:
        newcard = 2
    if newvar == 3:
        newcard = 3
    if newvar == 4:
        newcard = 4
    if newvar == 5:
        newcard = 5
    if newvar == 6:
        newcard = 6
    if newvar == 7:
        newcard = 7
    if newvar == 8:
        newcard = 8
    if newvar == 9:
        newcard = 9
    if newvar == 10:
        newcard = 10
    if newvar == "queen":
        newcard = 10
    if newvar == "Jack":
        newcard = 10
    if newvar == "king":
        newcard = 10
    if newvar == "ace":
        if playval + 11 > 21:
            newcard = 1
        else:
            newcard = 11
    dealval = dealval + newcard
    print(" ")
    print("You see the dealer has a")
    print(newvar)
    print("You don't know what their other card is.")

    dealvar = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "ace", "Jack", "queen", "king"])
    if dealvar == 2:
        newcard = 2
    if dealvar == 3:
        newcard = 3
    if dealvar == 4:
        newcard = 4
    if dealvar == 5:
        newcard = 5
    if dealvar == 6:
        newcard = 6
    if dealvar == 7:
        newcard = 7
    if dealvar == 8:
        newcard = 8
    if dealvar == 9:
        newcard = 9
    if dealvar == 10:
        newcard = 10
    if dealvar == "queen":
        newcard = 10
    if dealvar == "Jack":
        newcard = 10
    if dealvar == "king":
        newcard = 10
    if dealvar == "ace":
        if playval + 11 > 21:
            newcard = 1
        else:
            newcard = 11
    dealval = dealval + newcard

    if dealval == 21:
        print("The dealer flips their other card over. They have a BlackJack.")
        if playval < 21:
            losses = losses + 1
            print("")
            print("New round")
            gamestart()


    if playval == 21:
        if dealval == 21:
            print("Push!")
            print("New Round")
            gamestart()
        else:
            print("BlackJack!")
            chips = +currentbet*1.5
            print(" ")
            print("New round")
            wins = wins + 1
            gamestart()
    else:
        print("")
        print("Your card total is", playval)
        print("")


        options()

def start():
    global playval
    playval = 0
    print("Welcome to text-based BlackJack!")
    print(" ")
    if input("Do you want to start?") == "yes":
        gamestart()
    else:
        print("Goodbye")
def gameover():
    print("You have no more chips. bye")


stewie = tk.Tk ()
stewie.title("MythicalJay's")
stewie.minsize(1500, 1000)
stand=tk.Button(stewie, text="stand", command=stand, bg="hotpink")
stand.grid(row=5, column=8,)
hit=tk.Button(stewie, text="hit", command=hit, bg="lightblue")
hit.grid(row=5, column=7,)
double=tk.Button(stewie, text="double", command=double, bg="red")
double.grid(row=5, column=6,)
start()
stewie.mainloop ()
