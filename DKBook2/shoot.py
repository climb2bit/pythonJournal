import pgzrun
from random import randint, sample

apple  = Actor("apple.png")
orange = Actor("orange.png")
pineapple = Actor("pineapple.png")

fruits = [apple, orange, pineapple]
# method 1: random
# selected_fruit = sample(fruits, 1)[0]

# method 2: round-robin
select_index = 0
selected_fruit = fruits[select_index]

def draw():
    screen.clear()
    selected_fruit.draw()

# def place_apple():
#     apple.x = randint(10, 800)
#     apple.y  = randint(10,600)

def place_fruit(fruit):
    fruit.x = randint(10, 800)
    fruit.y  = randint(10,600)

def on_mouse_down(pos):
    global select_index
    global selected_fruit
    if selected_fruit.collidepoint(pos):
        print('good shot!')
        # method 1: random next fruit
        # selected_fruit = sample(fruits, 1)[0]

        # method 2: round-robin
        # select_index += 1
        # if select_index >= 3:
        #     select_index = 0
        select_index = (select_index + 1) % (len(fruits))        
        selected_fruit = fruits[select_index]
        place_fruit(selected_fruit)
    else:
        print('you missed')
        quit()

place_fruit(selected_fruit)

pgzrun.go()