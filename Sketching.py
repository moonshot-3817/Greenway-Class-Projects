import tkinter as tk
import random
hey=tk.Tk()
#DONT LOOK BELOW PLZ
culurs=["green", "blue", "red", "black", "brown", "coral", "cyan", "chocolate", "DarkOrchid", "cornsilk2", "khaki", "honeydew1", "HotPink"]
canvas=tk.Canvas(hey, bg=random.choice(culurs), height=250, width=300)
canvas.grid(row=1, column=1)
ball_radius=random.randint(5,25)
ball=[]
#ball.append((event.x,event.y))
global type
def switchroles1():
    global type
    type="line"
def switchroles2():
    global type
    type="circle"
def switchroles3():
    global type
    type="square"
def switchroles4():
    global type
    type="triangle"

line=tk.Button(hey, text="line", command=switchroles1,)
line.grid(row=1, column =2)
circle=tk.Button(hey, text="cirlce", command=switchroles2,)
circle.grid(row=1, column =5)
square=tk.Button(hey, text="square", command=switchroles3,)
square.grid(row=1, column =3)
triangle=tk.Button(hey, text="triangle", command=switchroles4,)
triangle.grid(row=1, column =4)
def click(event):
    if type=="circle":
        print("hi")
        oval = canvas.create_oval (event.x-ball_radius, event.y-ball_radius,
                                    event.x+ball_radius, event.y+ball_radius,
                                    fill=random.choice(culurs),  width=1,)
    #code coome from https://stackoverflow.com/questions/28615900/how-do-i-add-a-mouse-click-position-to-a-list-in-tkinter
    if type=="line":
        #ball.append ([event.x, event.y])
        lineitem = canvas.create_line(event.x-ball_radius, event.y-ball_radius,
                                      event.x+ball_radius, event.y+ball_radius,
                                    fill=random.choice(culurs),  width=1,)
        #ball.pop()
    if type=="square":
        #missing a second postion. Need 2nd click to create actual line accomplish
        #have x1 and x2 and find difference between the two
        #ex:abs(event.x-event.x2)
        #make event.x2=items in ball[]. But still be an integer. Ex: ball[3]=event.x2. Event.x2 might be substituted for actual variable
        print("yo")
        squareitem = canvas.create_rectangle(abs(event.x-event.x2), abs(event.y-event.x2),
                                             abs (event.x - event.x2), abs(event.y-event.x2),
                                             fill=random.choice(culurs),  width=1,)
    if type=="triangle":
        print("what up")
        if len (ball)== 3:
            triangleitem = canvas.create_polygon(event.x-ball_radius, event.y-ball_radius,
                                    event.x+ball_radius, event.y+ball_radius,
                                    fill=random.choice(culurs),  width=1,)

#othershapes
square.bind ("<Button-1>", click)
triangle.bind ("<Button-1>", click)
canvas.bind("<Button-1>", click)
line.bind ("<Button-1>", click)
circle.bind ("<Button-1>", click)

hey.mainloop()

'''''''''
import math
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw  (simplegui)
"""
def click(pos):
    changed = False
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "Green"
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])
"""

def click(event):
    """ replacement mouse handler inside Canvas, draws a red ball on each click"""
    changed = False
    print ("Canvas: mouse clicked at ", event.x, event.y)
    for ball in ball_list:
        if distance([ball[0], ball[1]], [event.x, event.y]) < ball_radius:
            ball[2] = "Green"
            changed = True       #  I didn't use this yet

    if not changed:
        ball_list.append([event.x, event.y, "Red"])  # didn't use this either

    canvas.create_oval(event.x - ball_radius, event.y - ball_radius, \
                       event.x + ball_radius, event.y + ball_radius,\
                       width=2, fill= "Red")


def callback_frame(event):
    """ handler for mouse click in the Frame instead of the Canvas """
    print ("Frame: mouse clicked at", event.x, event.y)

"""
don't need a draw handler because the balls aren't moving
def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball[2])
"""

# create frame
#frame = simplegui.create_frame("Mouse selection", width, height)
#frame.set_canvas_background("White")

# register event handler
#frame.set_mouseclick_handler(click)
#frame.set_draw_handler(draw)

# start frame
#frame.start()

root = Tk()

root.title('Mouse click makes red ball')
frame = Frame(root, width = 200, height = 200)
frame.grid(column = 0, row = 1)

canvas = Canvas(root,width=200, height=200, bg='white')
canvas.grid(column = 1, row = 1)

frame.bind("<Button-1>", callback_frame)
canvas.bind("<Button-1>", click)

mainloop()
'''''
#http://www.codeskulptor.org/#user14_MxIPA78aRmnIJU3.py