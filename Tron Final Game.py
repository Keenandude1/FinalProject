import pygame
import sys

pygame.init()

# Define playing area

width = 900
height = 900

# Define display and establish clock, set game caption

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Game")
clock = pygame.time.Clock()

# Set up coloring for backgrounds and bikes

background = (0, 0, 0)
white = (236, 240, 241)
blue = (100,149,237)
dark_blue = (0,0,205)
orange = (255, 140, 0)
dark_orange = (255, 97, 3)

# Set font

font = pygame.font.SysFont("arial.ttf", 50)

# Setting up bike size and coordinations for bike positioning

w = 10
h = 10

# Setting up bike class and assigning variables

class bike:
    def __init__(self, number, color, dark_color, side):
        self.w = w
        self.h = h
        self.x = abs(side - 100)
        self.y = height/2 - self.h
        self.color = color
        self.dark_color = dark_color
        self.speed = 10
        self.location = [[self.x, self.y]]
        self.number = number
        self.length = 1

# Draws the rect for the bike in the game, sets color and spawn points

    def draw(self):
         for i in range(len(self.location)):
              if i == self.length - 1:
                 pygame.draw.rect(display, self.dark_color, (self.location[i][0], self.location[i][1], self.w, self.h))
              else:    
                pygame.draw.rect(display, self.color, (self.location[i][0], self.location[i][1], self.w, self.h))
   
# Establishes bikes ability to move and the speed at which it moves by appending/changing location, also ensures bikes are right size

    def move(self, xdir, ydir):
        self.x += xdir*self.speed
        self.y += ydir*self.speed
        self.location.append([self.x, self.y])
        self.length += 1
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            game_over(self.number)

# Checking for collisions to end game, first if statement checks for player on player collision leading to tie, first for loop checks if the opponent ran into any trails or border,
# second for loop checks if the first player ran into any trails or border

    def check_if_collide(self, opponent):
         if abs(opponent.location[opponent.length - 1][0] - self.location[self.length - 1][0]) < self.w and abs(opponent.location[opponent.length - 1][1] - self.location[self.length - 1][1]) < self.h:
            game_over(0)
         for i in range(opponent.length):
            if abs(opponent.location[i][0] - self.location[self.length - 1][0]) < self.w and abs(opponent.location[i][1] - self.location[self.length - 1][1]) < self.h:
                game_over(self.number)

         for i in range(len(self.location) - 1):
            if abs(self.location[i][0] - self.x) < self.w and abs(self.location[i][1] - self.y) < self.h and self.length > 2:
                game_over(self.number)

# Establishes events to occur if the game ends and what text to show after game ends,
# also allows you to press e to quit game if you need a fast exit, and b to restart if you want to play again


def game_over(number):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    close()
                if event.key == pygame.K_b:
                    tron()
        if number == 0:
            text = font.render("Players Crash! Both Losers", True, white)
        else:
            text = font.render("Player %d Is A Loser!" %(number), True, white)

        display.blit(text, (50, height/2))
       
        pygame.display.update()
        clock.tick(60)

# Quits pygame and exits the system

def close():
    pygame.quit()
    sys.exit()

# Establishes the game assigning values to bike1 and bike2, takes key inputs from players that moves bike in said direction and diffirentaiates
# controls between bike1 and bike2
def tron():
    loop = True

    bike1 = bike(1, blue, dark_blue, 0)
    bike2 = bike(2, orange, dark_orange, width)

    x1 = 0
    y1 = 1
    x2 = 0
    y2 = -1
   
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_UP:
                    if not (x2 == 0 and y2 == 1):
                        x2 = 0
                        y2 = -1
                if event.key == pygame.K_DOWN:
                    if not (x2 == 0 and y2 == -1):
                        x2 = 0
                        y2 = 1
                if event.key == pygame.K_LEFT:
                    if not (x2 == 1 and y2 == 0):
                        x2 = -1
                        y2 = 0
                if event.key == pygame.K_RIGHT:
                    if not (x2 == -1 and y2 == 0):
                        x2 = 1
                        y2 = 0
                if event.key == pygame.K_w:
                    if not (x1 == 0 and y1 == 1):
                        x1 = 0
                        y1 = -1
                if event.key == pygame.K_s:
                    if not (x1 == 0 and y1 == -1):
                        x1 = 0
                        y1 = 1
                if event.key == pygame.K_a:
                    if not (x1 == 1 and y1 == 0):
                        x1 = -1
                        y1 = 0
                if event.key == pygame.K_d:
                    if not (x1 == -1 and y1 == 0):
                        x1 = 1
                        y1 = 0
               
               
           
        display.fill(background)
       
       
        bike1.draw()
        bike2.draw()

        bike1.move(x1, y1)
        bike2.move(x2, y2)

        bike1.check_if_collide(bike2)
        bike2.check_if_collide(bike1)
       
        pygame.display.update()
        clock.tick(20)


tron()
