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
        background.update_food()

    def spawn_food(self):
        self.surface.fill(self.color)
        print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)
    
    def update_food(self):
        self.surface.fill(self.color)
        print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)

class Snake(Gamebackground):
    def __init__(self , length=3, spawn=(5, 5)):
        self.spawn = spawn
        self.length = length 
        self.head = (background.height/2, background.width/2)
        self.grow_size = 0
    
    def spawn_worm(self):
        location = (background.height/2, background.width/2)
        background.surface.blit(worm, location)

    def update_snake():
        pass

    def up(self):
        background.surface.fill(background.color)
        self.head = (self.head[0], self.head[1]-20)
        background.surface.blit(worm, self.head)
        

    def down(self):
        background.surface.fill(background.color)
        self.head = (self.head[0], self.head[1]+20)
        background.surface.blit(worm, self.head)
        
    
    def left(self):
        background.surface.fill(background.color)
        self.head = (self.head[0]-20, self.head[1])
        background.surface.blit(worm, self.head)
        

    def right(self):
        background.surface.fill(background.color)
        self.head = (self.head[0]+20, self.head[1])
        background.surface.blit(worm, self.head)
        

    def grow(self):
        self.grow_size += 1

    def colision(self):
        pass
    

background = Gamebackground(500, 500, (50, 168, 82))
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
    
    clock.tick(60)

pygame.quit()