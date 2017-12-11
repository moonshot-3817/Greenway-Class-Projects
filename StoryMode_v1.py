import tkinter
from tkinter import *
from tkinter.font import Font

window = tkinter.Tk()
window.configure(bg = "cyan")
window.title("Story")
window.geometry("800x400")

f = Font(family='courier', size=14)



def deads():
    global dead
    global fight
    dead.destroy()
    fight.destroy()
    new.insert(INSERT, "\nYou lay on the ground and play dead.")

def fights():
    global dead
    global fight
    dead.destroy()
    fight.destroy()
    new.insert(INSERT, "\nYou run up to the bear and try to fight.")


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
    new.insert(INSERT, "\nYou take the path to the left.")

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