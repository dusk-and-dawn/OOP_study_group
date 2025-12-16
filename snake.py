import pygame
from random import randint
from pathlib import Path

pygame.init()


class Snake():
    def __init__(self, spawn=(5, 5), head, length=3):
        self.spawn = spawn
        self.length = length 
        self.head = head
        self.grow_size = 0
    
    def movement(self):
        # up = (x=x, y+=1)
        # down = (x=x, y-=1)
        #left = (x-=1, y=y)
        #right = (x+=1, y=y)

    def grow(self):
        self.grow_size += 1

    def colision(self):
        pass
    
    

class Gamebackground():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        pygame.display.init()
        self.surface = pygame.display.set_mode([self.width, self.height])
        self.surface.fill(self.color)
        pygame.display.set_caption("Experimental Snake")

    def show_splash(self):
        pygame.display.flip()

    def spawn_food(self):
        self.surface.fill(self.color)
        location = (randint(0, 450), randint(0, 450))
        print(f"food is at {location}")
        self.surface.blit(food, location)


background = Gamebackground(500, 500, (50, 168, 82))
food = pygame.image.load(Path("static/food1.png")).convert_alpha()
food = pygame.transform.smoothscale(food, (64, 64))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                background.spawn_food()

    background.show_splash()
    clock.tick(60)

pygame.quit()