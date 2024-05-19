import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL

def next_shape():
    global shape
    global previous_color
    global current_color

    previous_color = current_color

    c.delete(shape)
    if len(shapes) >0:
        shape = shapes.pop()
        c.itemconfigure(shape, state = NORMAL)
        current_color = c.itemcget(shape, 'fill')
        root.after(1000, next_shape)
    else:
        c.unbind('q')
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text(200, 200, text  = 'Winner: player 1!')
        elif player2_score > player1_score:
            c.create_text(200, 200, text = 'Winner: Player 2!')
        else:
            c.create_text(200,200,text = 'Draw')
        c.pack()
def snap(event):
    global shape
    global player1_score
    global player2_score
    global previous_color
    valid = False
    c.delete(shape)
    if previous_color == current_color:
        valid = True
    if valid:
        if event.char == 'q':
            player1_score = player1_score +1
            shape = c.create_text(200,200, text = 'SNAP! player 1 scores 1 point!')            
        else:
            player2_score = player2_score +1
            shape = c.create_text(200,200, text = 'SNAP! player 2 scores 1 point!')
        previous_color = ''

    else:
        if event.char == 'q':
            player1_score = player1_score -1
            shape = c.create_text(200,200, text = 'WRONG! player 1 lost 1 point!')
        else:
            player2_score = player2_score -1
            shape = c.create_text(200,200, text = 'WRONG! player 2 lost 1 point!')
    c.pack()
    root.update_idletasks()
    time.sleep() 

root = Tk()
root.title('Snap')
c = Canvas(root, width = 400, height = 400)

shapes = []

circle = c.create_oval(35, 20,365, 350, outline = 'black', fill = 'black', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20,365, 350, outline = 'red', fill = 'red', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20,365, 350, outline ='green', fill = 'green', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20,365, 350, outline = 'blue', fill = 'blue', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20,365, 350, outline = 'purple', fill = 'purple', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20,365, 350, outline = 'turquoise', fill = 'turquoise', state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20,365, 350, outline = 'dark khaki', fill = 'dark khaki', state = HIDDEN)
shapes.append(circle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'black', fill= 'black', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'red', fill= 'red', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'green', fill= 'green', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'black', fill= 'black', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'blue', fill= 'blue', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'purple', fill= 'purple', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'turquoise', fill= 'turquoise', state = HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270,outline = 'dark khaki', fill= 'dark khaki', state = HIDDEN)
shapes.append(rectangle)
square = c.create_rectangle(35, 20, 365, 350,outline = 'black', fill= 'black', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350,outline = 'blue', fill= 'blue', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350,outline = 'green', fill= 'green', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350,outline = 'red', fill= 'red', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350,outline = 'purple', fill= 'purple', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350,outline = 'turquoise', fill= 'turquoise', state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350,outline = 'dark khaki', fill= 'dark khaki', state = HIDDEN)
shapes.append(square)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'blue', fill = 'blue', state = HIDDEN)
shapes.append(polygon)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'black', fill = 'black', state = HIDDEN)
shapes.append(polygon)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'red', fill = 'red', state = HIDDEN)
shapes.append(polygon)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'green', fill = 'green', state = HIDDEN)
shapes.append(polygon)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'purple', fill = 'purple', state = HIDDEN)
shapes.append(polygon)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'turquoise', fill = 'turquoise', state = HIDDEN)
shapes.append(polygon)
polygon = c.create_polygon(35,200,365,200,200,35,outline = 'dark khaki', fill = 'dark khaki', state = HIDDEN)
shapes.append(polygon)


random.shuffle(shapes)

shape = None
previous_color = 'a'
current_color = 'b'
player1_score = 0
player2_score = 0

root.after(3000, next_shape)
c.bind('q', snap)
c.bind('p', snap)
c.focus_set()
c.pack()
root.mainloop()

