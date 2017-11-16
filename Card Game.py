from random import *
import string
import sys
import random
from tkinter import *

import tkinter


root = Tk()

Font_1 = ("Courier New", 12)
Font_2 = ("Times New Roman", 14)

root.title("Game")
root.geometry("1250x650")

cardval = 0
dealval = 0


def drawcards():
    # two random cards for you (images)
    # two random cards for dealer (images)
    # cardval = sum of cards
    # dealval = sum of dealer's cards

def dealdraw():
    #flip over hidden card
    if dealval == #17 or more
        if dealval == #more than cardval
            #loss
            round()
        if dealval == #less than cardval
            #win
            round()
    else:
        #dealer hits
        #add new card value
        if dealval == #more than 21
            #win
            round()
        if dealval == #less than 21
            dealdraw()
        if dealval == #21
            #loss
            round()


def moredraw():
    #draw another card
    #add new card to cardval
    if cardval == #less than 21
        #hit, stand, etc.
        #if hit, moredraw()
        #if stand, dealdraw()
    if cardval == #21
        #win
        round()
    if cardval == #morethan21
        #loss
        round()


def round():
    drawcards()
    #hide one of dealer's cards
    if dealval == #21
        if cardval == #21
            #push
            round()
        else:
            #loss
            round()
    if cardval == #lessthan21
        #buttons to hit or stand
        #if stand, dealdraw()
        #if hit, moredraw()
    if cardval == #21
        if dealval == #21
            #push
            round()
        else:
            #winround
            round()
    if cardval == #morethan21
        #loss
        round()


root.mainloop()