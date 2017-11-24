import Tkinter as tk
import random
hey=tk.Tk()
#DONT LOOK BELOW PLZ
culurs=["green", "blue", "red", "black", "brown", "coral", "cyan", "chocolate", "DarkOrchid", "cornsilk2", "khaki", "honeydew1", "HotPink"]
canvasheight=500
canvaswidth=1000
canvas=tk.Canvas(hey, bg=random.choice(culurs), height=canvasheight, width=canvaswidth)
canvas.grid(rowspan=1, columnspan=10)
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
    type="coolsquare"
def switchroles4():
    global type
    type="triangle"
def switchroles5():
    global type
    type="square"
def switchroles6():
    global type
    type="paint"
def switchroles7():
    global type
    type="verticalline"
def switchroles8():
    global type
    type="horizontalline"

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
triangle=tk.Button(hey, text="triangle", command=switchroles4,)
triangle.grid(row=1, column =4)
paint=tk.Button(hey, text="paint", command=switchroles6,)
paint.grid(row=1, column =8)
def click(event):
    if type=="circle":
        print("hi")
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
        print("yo")
        canvas.create_rectangle (event.x, event.y, canvaswidth/2, canvasheight/2, fill=random.choice(culurs))
        #squareitem = canvas.create_rectangle(#abs(event.x-event.x2), abs(event.y-event.x2),
                                             #abs (event.x - event.x2), abs(event.y-event.x2),
                                             #fill=random.choice(culurs),  width=1,)
    if type=="square":
        print("sigh")
        cat=random.randint(1, 250)
        x1, y1 = ( event.x - cat ), ( event.y - cat )
        x2, y2 = ( event.x + cat ), ( event.y + cat )
        canvas.create_rectangle (x1, y1, x2, y2, fill=random.choice(culurs))
    if type=="triangle":
        print("what up")
        if len (ball)== 3:
            triangleitem = canvas.create_polygon(event.x-ball_radius, event.y-ball_radius,
                                    event.x+ball_radius, event.y+ball_radius,
                                    fill=random.choice(culurs),  width=1,)

def paint( event ):
    if type == "paint":
        believe=0
        while believe <100:
            x1, y1 = ( event.x - 3 ), ( event.y - 3 )
            x2, y2 = ( event.x + 3 ), ( event.y + 3 )
            lineitem = canvas.create_line(event.x, event.y - ball_radius,
                                    event.x , event.y+ ball_radius,
                                        fill=random.choice(culurs), width=1, )
            believe=+ 1


#othershapes
coolsquare.bind ("<Button-1>", click)
triangle.bind ("<Button-1>", click)
canvas.bind("<Button-1>", click)
line.bind ("<Button-1>", click)
verticalline.bind ("<Button-1>", click)
horizontalline.bind ("<Button-1>", click)
circle.bind ("<Button-1>", click)
square.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", paint)

def settings():
    global input1
    input1=input("what size of shape?")
    if input1>="1" and input1<="50":
        ball_radius=int(input1)
    input1= input("what colors?")
    if input1 == "green" "blue" "red" "black" "brown" "coral" "cyan" "chocolate" "DarkOrchid" "cornsilk2" "khaki" "honeydew1" "HotPink":
        culurs.pop()
        culurs=input1
    input1=input ("what width of canvas?")
    if input1>="100" and input1<="2000":
        canvaswidth=int(input1)
    input1 = input ("what height of canvas?")
    if input1<="100" and input1<="2000":
        canvasheight=int(input1)
        canvas = tk.Canvas (hey, bg=random.choice (culurs), height=canvasheight, width=canvaswidth)
        canvas.grid (rowspan=1, columnspan=10)

settings = tk.Button (hey, text="Advanced Settings", command=settings, )
settings.grid (row=5, column=5)
quit = settings = tk.Button (hey, text="Quit", command=hey.destroy, )
quit.grid (row=4, column=5)


hey.mainloop()
#http://www.codeskulptor.org/#user14_MxIPA78aRmnIJU3.py
