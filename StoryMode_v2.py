import tkinter
from tkinter import *
from tkinter.font import Font
import time

window = tkinter.Tk()
window.configure(bg = "cyan")
window.title("Story")
window.geometry("800x400")

f = Font(family='courier', size=14)

def uniform():
    yes.destroy()
    note.destroy()
    new.insert(INSERT, "\nYou enter the cave and see a pile of gold!\nYou are rich!")
    new.insert(INSERT, "\nThanks for playing!")
    q = Button(window, height = 3, width = 8, text = "Quit", command = no)
    q.pack(side = BOTTOM)

def foxtrot():
    yes.destroy()
    note.destroy()
    new.insert(INSERT, "\nYou do not go in the cave.\nThe bear has returned!")
    new.insert(INSERT, "\nYou are unprepared and the bear eats you.")
    q = Button(window, height = 3, width = 8, text = "Quit", command = no)
    q.pack(side = BOTTOM)

def bravo():
    global yes
    global note
    nothing.destroy()
    tie.destroy()
    new.insert(INSERT, "\nYou tie your jacket around the wound.\nThe bleeding stops.\nYou finally reach the mountain.")
    new.insert(INSERT, "\nYou see a cave.\nDo you enter?")
    yes = Button(window, height = 3, width = 8, text = "Yes!",command = uniform)
    yes.pack(side = BOTTOM)
    note = Button(window, height = 3, width = 8, text = "NO!", command = foxtrot)
    note.pack(side = BOTTOM)

def olive():
    queen.destroy()
    whiskey.destroy()
    new.insert(INSERT, "\nYou open the box and a monster jumps out of it!\nYou get eaten.")
    k = Button(window, width = 8, height = 3, text = "Quit",command = no)
    k.pack(side = BOTTOM)

def canary():
    whiskey.destroy()
    queen.destroy()
    new.insert(INSERT, "\nYou walk away from the box and see another box!\nThis one looks like a treasure chest.\n"
                       "You open it and find gold!\nYou are rich!\nThanks for playing!")
    slade = Button(window, height = 3, width = 8, text = "Quit", command = no)
    slade.pack(side = BOTTOM)

def jum():
    global whiskey
    global queen
    jump.destroy()
    charlie.destroy()
    new.insert(INSERT, "\nYou successfully jump across the river.")
    new.insert(INSERT, "\nYou walk along the river bank towards the ocean.\nWhen you reach the ocean, you find a box in the sand.")
    new.insert(INSERT, "\nDo you open it?")
    whiskey = Button(window, height = 3, width = 8, text = "Yes!",command = olive)
    whiskey.pack(side = BOTTOM)
    queen = Button(window, height = 3, width =8, text = "No!", command = canary)
    queen.pack(side = BOTTOM)

def swi():
    jump.destroy()
    charlie.destroy()
    new.insert(INSERT, "\nYou attempt to swim across, but drown.")
    qu = Button(window, height = 3, width = 8, text = "Quit", command = no)
    qu.pack(side = BOTTOM)

def alpha():
    global nothing
    global tie
    tie.destroy()
    nothing.destroy()
    new.insert(INSERT, "\nYou bleed out and die.")
    qu = Button(window, height = 3, width = 8, text ="Quit",command = no)
    qu.pack(side = BOTTOM)


def ocea():
    global jump
    global charlie
    mountains.destroy()
    ocean.destroy()
    new.insert(INSERT, "\nYou start walking to the ocean in the distance.")
    new.insert(INSERT, "\nThere is a small river in your way.")
    new.insert(INSERT, "\nDo you jump across or try to swim?")
    jump = Button(window, height = 3, width = 8, text = "Jump", command = jum)
    jump.pack(side = BOTTOM)
    charlie = Button(window, height = 3, width = 8, text = "Swim", command = swi)
    charlie.pack(side = BOTTOM)

def mount():
    global nothing
    global tie
    mountains.destroy()
    ocean.destroy()
    new.insert(INSERT, "\nYou start walking towards the mountains in the distance.")
    new.insert(INSERT, "\nWhile walking, you trip on a rock and start bleeding.")
    new.insert(INSERT, "\nWhat do you do?")
    nothing = Button(window, height = 3, width = 8, text = "Do nothing", command = alpha)
    nothing.pack(side = BOTTOM)
    tie = Button(window, height = 3, width = 8, text = "Stop Bleeding", command = bravo)

    tie.pack(side = BOTTOM)


def no():
    window.destroy()

def deads():
    global mountains
    global ocean
    dead.destroy()
    fight.destroy()
    new.insert(INSERT, "\nYou lay on the ground and play dead.")
    new.insert(INSERT, "\nThe bear ignores you and walks away.")
    new.insert(INSERT, "\nYou stand up and continue through the forest.")
    new.insert(INSERT, "\nDo you want to go towards the mountains or the ocean?")
    mountains = Button(window, height = 3, width = 8, text = "Mountains", command = mount)
    mountains.pack(side = BOTTOM)
    ocean = Button(window, height = 3, width = 8, text = "Ocean", command = ocea)
    ocean.pack(side = BOTTOM)

def fights():
    global dead
    global fight

    dead.destroy()
    fight.destroy()
    new.insert(INSERT, "\nYou run up to the bear and try to fight.\nThe bear is stronger than you and kills you.")
    qu = Button(window, height = 3, width = 8, text ="Quit",command = no)
    qu.pack(side = BOTTOM)


def right():
    global fight
    global dead
    left.destroy()
    right.destroy()
    new.insert(INSERT,"\nYou take the path to the right.")
    new.insert(INSERT,"\nYou are walking down the right path, and you come across a bear.")
    new.insert(INSERT,"\nWhat do you do?")
    dead = Button(window, height = 3, width = 8, text = "Play Dead", command = deads)
    dead.pack(side = BOTTOM)
    fight = Button(window, height = 3, width = 8, text = "Attack", command = fights)
    fight.pack(side = BOTTOM)


def left():
    left.destroy()
    right.destroy()
    new.insert(INSERT, "\nYou take the path to the left.\nThis was the wrong descision.\nA rabid"
                       " lion is in your way.\nYou have no chance.\nYou get eaten.")
    lance = Button(window, height = 3, width =8, text = "Quit", command = no)
    lance.pack(side = BOTTOM)

#scrollbar and start
scroll = Scrollbar(window)
scroll.pack(side = RIGHT, fill = Y)


new = Text (window, font = f, height = 13, yscrollcommand = scroll.set)
new.insert(INSERT,"Welcome to interactive story mode!")
new.insert(INSERT,"\nOne day, you were walking in the forest and you came across a path.\n")
new.insert(INSERT,"Do you go RIGHT or LEFT?")

right = Button(window, height = 3, width = 8, text = "RIGHT", command = right )
right.pack(side = BOTTOM)

left = Button(window, height = 3, width = 8, text = "LEFT", command = left )
left.pack(side = BOTTOM)


new.pack()



window.mainloop()