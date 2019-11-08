import random
from tkinter import *

# movement player1
def move(direction):
    global player
    global canvas
    global RAQUETTE_MOVEMENT
    global HEIGHT

    coords = canvas.coords(player)

    if (direction == 'haut' and coords[1] <= 10) or \
       (direction == 'bas' and coords[3] >= HEIGHT):
       return False

    if direction == 'haut':
        movement = -RAQUETTE_MOVEMENT
    else:
        movement = RAQUETTE_MOVEMENT

    canvas.move(player, 0, movement)

# movement player2
def move2(direction):
    global player2
    global canvas
    global RAQUETTE_MOVEMENT
    global HEIGHT

    coords = canvas.coords(player)

    if (direction == 'bas' and coords[1] <= 10) or \
       (direction == 'bas' and coords[3] >= HEIGHT):
       return False

    if direction == 'haut':
        movement = -RAQUETTE_MOVEMENT
    else:
        movement = RAQUETTE_MOVEMENT

    canvas.move(player2, 0, movement)

def move_ball():
    global ball
    global canvas
    global dx
    global dy

    canvas.move(ball, dx, dy)

# mouvement des joueurs
def move_up(event):
    move('haut')

def move_up2(event):
    move2('haut')

def move_down(event):
    move('bas')
    
def move_down2(event):
    move2('bas')

# rebond de la balle 
def bounce_ball():
    global dx
    global dy

    dx = -dx
    dy = random.randint(1, 3)
    flip_y = random.randint(0, 1) * 1

    if flip_y:
        dy = -dy

# affichage du score des deux joueurs
def show_scores():
    global canvas
    global player_score
    global player2_score
    global player_score_label
    global player2_score_label

    canvas.delete(player_score_label)
    canvas.delete(player2_score_label)

    player_score_label = canvas.create_text(190, 15, text=player2_score, fill='white', font=('Arial', 15))
    player2_score_label = canvas.create_text(210, 15, text=player_score, fill='white', font=('Arial', 15))

def reset_ball():
    global canvas
    global ball
    global dx
    global dy

    flip_x = random.randint(0, 1) * 1
    dx = random.randint(2, 3)
    dy = random.randint(1, 3)

    if flip_x == 1:
        dx = -dx

    canvas.delete(ball)
    ball = canvas.create_oval((190, 190, 210, 210), fill="white")

# ça permet de tout reset
def refresh():
    global canvas
    global ball
    global player
    global player2
    global player_score
    global player2_score
    global WIDTH
    global HEIGHT
    global dx
    global dy
    global master
    global REFRESH_TIME

    show_scores()
    move_ball()
    ball_coords = canvas.coords(ball)

    if ball_coords[0] < 0:
        player_score = player_score + 1
        reset_ball()
    elif ball_coords[0] > WIDTH:
        player2_score = player2_score + 1
        reset_ball()

    if ball_coords[1] < 0 or ball_coords[3] > HEIGHT:
        dy = -dy

    overlapping = canvas.find_overlapping(*ball_coords)

    if len(overlapping) > 1:
        collided_item = overlapping[0]

        if collided_item == player or collided_item == player2:
            bounce_ball()

    master.after(REFRESH_TIME, refresh)

# dimention de la fenetre 
WIDTH = 400
HEIGHT = 400
RAQUETTE_MOVEMENT = 10
REFRESH_TIME = 20  # milliseconds

# interface graphique 
master = Tk()
master.title("Pong in Python / Tk!")

canvas = Canvas(master, background="black", width=WIDTH, height=HEIGHT)
canvas.create_line((200, 0, 200, 400), fill="red")

# rectangles players
player = canvas.create_rectangle((10, 150, 30, 250), fill="red")
player2 = canvas.create_rectangle((370, 150, 390, 250), fill="red")
ball = None  

# Commandes joueur1
master.bind("a", move_up)
master.bind("q", move_down)

# Commandes joueur2
master.bind("<KeyPress-Up>", move_up2)
master.bind("<KeyPress-Down>", move_down2)

# Game variables
player_score = 0
player2_score = 0

# score des joueurs
player_score_label = None
player2_score_label = None

# reset au centre
dx = 0
dy = 0

canvas.pack()


reset_ball()
master.after(REFRESH_TIME, refresh)
master.mainloop()
