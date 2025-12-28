import pygame
from random import randint
from pathlib import Path

pygame.init()

class Gamebackground():
    def __init__(self, width, height, color, food_location = (randint(0, 450), randint(0, 450))):
        self.width = width
        self.height = height
        self.color = color
        self.food_location = food_location
        pygame.display.init()
        self.surface = pygame.display.set_mode([self.width, self.height])
        self.surface.fill(self.color)
        pygame.display.set_caption("Experimental Snake")

    def show_splash(self):
        pygame.display.flip()
        # background.update_food()
        self.show_food()

    def spawn_food(self):
        self.surface.fill(self.color)
        print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)

    def show_food(self):
        # self.surface.fill(self.color)
        print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)
    
    def update_food(self):
        self.food_location = (randint(0, 450), randint(0, 450))
        # self.surface.fill(self.color)
        # print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)

    def check_snake(self, snake):
        print(f"self.foodlocation: {self.food_location} background.head: {snake.head}")
        if self.food_location == snake.head:
            background.update_food()
            snake.grow()


class Snake(Gamebackground):
    def __init__(self , length=3, spawn=(5, 5)):
        self.spawn = spawn
        self.length = length 
        self.head = (int(background.height/2), int(background.width/2))
        self.grow_size = 0
    
    def spawn_worm(self):
        location = (background.height/2, background.width/2)
        background.surface.blit(worm, location)

    def update_snake(self):
        if self.grow_size > 0:
            background.surface.blit(worm, (self.head[0], self.head[1]-60))

    def up(self):
        # up = (x=x, y+=1)
        background.surface.fill(background.color)
        self.head = (self.head[0], self.head[1]-100)
        background.surface.blit(worm, self.head)
        print(f"worm is at {self.head}")
        self.update_snake()

    def down(self):
        # down = (x=x, y-=1)
        pass
    
    def left(self):
        #left = (x-=1, y=y)
        pass

    def right(self):
        #right = (x+=1, y=y)
        pass

    def grow(self):
        self.grow_size += 1

    def colision(self):
        pass
    

background = Gamebackground(500, 500, (50, 168, 82), food_location=(250.0, 250.0))
snake = Snake()
food = pygame.image.load(Path("static/food1.png")).convert_alpha()
food = pygame.transform.smoothscale(food, (64, 64))
worm = pygame.image.load(Path("static/worm.png")).convert_alpha()
worm = pygame.transform.smoothscale(worm, (64, 64))

clock = pygame.time.Clock()
running = True
snake.spawn_worm()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snake.left()
            elif event.key == pygame.K_w:
                snake.up()
            elif event.key == pygame.K_d:
                snake.right()
            elif event.key == pygame.K_s:
                snake.down()
            elif event.key == pygame.K_f:
                background.spawn_food()
    background.show_splash()
    background.check_snake(snake=snake)
    
    clock.tick(60)

pygame.quit()