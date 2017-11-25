import tkinter as tk
import random
hey=tk.Tk()
culurs=["green", "blue", "red", "black", "brown", "coral", "cyan", "chocolate", "DarkOrchid", "cornsilk2", "khaki", "honeydew1", "HotPink"]
global canvaswidth
global canvasheight
canvasheight=500
canvaswidth=1000
canvas=tk.Canvas(hey, bg=random.choice(culurs), height=canvasheight, width=canvaswidth)
canvas.grid(rowspan=1, columnspan=10)
ball_radius=random.randint(1,25)
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
    type="coolsquare"
def switchroles4():
    global type
    type="paint"
def switchroles5():
    global type
    type="square"
def switchroles6():
    global type
    type="trianglecomputerpuke"
def switchroles7():
    global type
    type="verticalline"
def switchroles8():
    global type
    type="horizontalline"
def switchroles9():
    global type
    type="eraser"

line=tk.Button(hey, text="line", command=switchroles1,)
line.grid(row=1, column =2)
verticalline=tk.Button(hey, text="verticalline", command=switchroles7,)
verticalline.grid(row=1, column =9)
horizontalline=tk.Button(hey, text="horizontalline", command=switchroles8,)
horizontalline.grid(row=1, column =6)
circle=tk.Button(hey, text="circle", command=switchroles2,)
circle.grid(row=1, column =5)
coolsquare=tk.Button(hey, text="coolsquare", command=switchroles3,)
coolsquare.grid(row=1, column =3)
square=tk.Button(hey, text="square", command=switchroles5,)
square.grid(row=1, column =7)
triangle=tk.Button(hey, text="paint", command=switchroles4,)
triangle.grid(row=1, column =4)
paint=tk.Button(hey, text="trianglecomputerpuke", command=switchroles6,)
paint.grid(row=1, column =8)
eraser=tk.Button(hey, text="eraser", command=switchroles9,)
eraser.grid(row=2, column =8)
def click(event):
    if type=="circle":
        oval = canvas.create_oval (event.x-ball_radius, event.y-ball_radius,
                                    event.x+ball_radius, event.y+ball_radius,
                                    fill=random.choice(culurs),  width=1,)
    #code coome from https://stackoverflow.com/questions/28615900/how-do-i-add-a-mouse-click-position-to-a-list-in-tkinter
    if type=="line":
        #ball.append ([event.x, event.y])
        lineitem = canvas.create_line(event.x-ball_radius, event.y- ball_radius,
                                      event.x+ball_radius, event.y+ ball_radius,
                                    fill=random.choice(culurs),  width=1,)
    if type == "horizontalline":
            # ball.append ([event.x, event.y])
        lineitem = canvas.create_line(event.x - ball_radius, event.y,
                                          event.x + ball_radius, event.y,
                                          fill=random.choice(culurs), width=1, )
    if type == "verticalline":
            # ball.append ([event.x, event.y])
        lineitem = canvas.create_line(event.x, event.y - ball_radius,
                                    event.x , event.y+ ball_radius,
                                        fill=random.choice(culurs), width=1, )
        #ball.pop()
    if type=="coolsquare":
        #missing a second postion. Need 2nd click to create actual line accomplish
        #have x1 and x2 and find difference between the two
        #ex:abs(event.x-event.x2)
        #make event.x2=items in ball[]. But still be an integer. Ex: ball[3]=event.x2. Event.x2 might be substituted for actual variable
        canvas.create_rectangle (event.x, event.y, canvaswidth/2, canvasheight/2, fill=random.choice(culurs))
        #squareitem = canvas.create_rectangle(#abs(event.x-event.x2), abs(event.y-event.x2),
                                             #abs (event.x - event.x2), abs(event.y-event.x2),
                                             #fill=random.choice(culurs),  width=1,)
    if type=="square":
        dog=random.randint(1,2)
        if dog==1:
            cat=random.randint(1, 250)
            x1, y1 = ( event.x - cat ), ( event.y - cat )
            x2, y2 = ( event.x + cat ), ( event.y + cat )
            canvas.create_rectangle (x1, y1, x2, y2, fill=random.choice(culurs))
        if dog==2:
            x1, y1 = (event.x - ball_radius), (event.y - ball_radius)
            x2, y2 = (event.x + ball_radius), (event.y + ball_radius)
            canvas.create_rectangle(x1, y1, x2, y2, fill=random.choice(culurs))

    if type=="eraser":
        x1, y1 = ( event.x - canvaswidth), ( event.y - canvasheight)
        x2, y2 = ( event.x + canvaswidth), ( event.y + canvasheight)
        canvas.create_rectangle (x1, y1, x2, y2, fill="White")
def paint( event ):
    if type == "trianglecomputerpuke":
        believe=0
        while (believe <= 100):
            x1, y1 = (event.x - believe), (event.y - believe) #http://www.codeskulptor.org/#user14_MxIPA78aRmnIJU3.py
            x2, y2 = (event.x + believe), (event.y + believe)
            lineitem = canvas.create_line(x1, y1 - ball_radius,
                                          x2, y1 + ball_radius,
                                          fill=random.choice(culurs), width=1, )
            believe=believe+1
    if type == "paint":
            x1, y1 = (event.x -ball_radius), (event.y -ball_radius)
            x2, y2 = (event.x +ball_radius), (event.y +ball_radius)
            paintitem= canvas.create_oval(x1, y1,
                                    x2, y2,
                                    fill=random.choice(culurs),  width=0,)

#othershapes
coolsquare.bind ("<Button-1>", click)
canvas.bind("<Button-1>", click)
line.bind ("<Button-1>", click)
verticalline.bind ("<Button-1>", click)
horizontalline.bind ("<Button-1>", click)
circle.bind ("<Button-1>", click)
square.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", paint)
triangle.bind("<B1-Motion>", paint)
eraser.bind("<Button-1>", click)

def settings():
    global input1
    global input2
    input1=input("what size of shape?")
    if input1>="1" and input1<="100":
        ball_radius=int(input1)
    input1= input("How many colors do you want?")
    if input1 >=1 and input1<=20:
        del culurs[:]
        print(len(culurs))
        while len(culurs) < input1:
            input2 = raw_input("What colors?")
            culurs.append(input2)
            print(culurs)
    tie=raw_input("Do you like these colors?")
    if tie=="no":
        print("Oh. Here are some possible color ideas: chocolate, pink, red, orange, aliceblue, bisque, crimson, cyan, darkblue, darkmagenta, darkorchid, olivegreen, gold, goldenrod, floralwhite, and more")
    input1=input ("what width of canvas?")
    if input1>="100" and input1<="1000":
        canvaswidth=int(input1)
    input1= input ("what height of canvas?")
    if input1<="100" and input1<="800":
        canvasheight=int(input1)
        canvas = tk.Canvas (hey, bg=random.choice (culurs), height=canvasheight, width=100)
        canvas.grid (rowspan=1, columnspan=10)
    print("Please do not answer the following questions.")
settings = tk.Button (hey, text="Advanced Settings", command=settings, )
settings.grid (row=2, column=2)
quit = settings = tk.Button (hey, text="Quit", command=hey.destroy, )
quit.grid (row=2, column=3)


hey.mainloop()
