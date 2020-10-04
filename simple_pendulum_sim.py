# Extra Requirement pygame
# $pip install pygame

import pygame
import math

win_width, win_height = 1280, 720

out = False
acceleration = False
length, angle, vel, Aacc = 0,0,0,0

#Colors
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)

pygame.init()
background = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

class ball(object):

    def __init__(self, XY, radius):  # Set ball coordenates and radius
        self.x = XY[0]
        self.y = XY[1]
        self.radius = radius

    def draw(self, bg):  # Draw circle and line based on XY coordinates
        pygame.draw.lines(bg, white, False, [(win_width/2, 50), (self.x, self.y)], 2)
        pygame.draw.circle(bg, white, (self.x, self.y), self.radius)
        pygame.draw.circle(bg, Dark_red, (self.x, self.y), self.radius - 2)

def angle_Length():  # Send back the length and angle at the first click on screen
    length = math.sqrt(math.pow(pendulum.x - win_width/2, 2) + math.pow(pendulum.y - 50, 2))
    angle = math.asin((pendulum.x - win_width/2)/ length)
    return (angle, length)

def get_path(first_angle, length): # with angle and length calculate x and y position
    pendulum.x = round(win_width/2 + length * math.sin(angle))
    pendulum.y = round(50 + length * math.cos(angle))

def redraw(): # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    background.fill(black)
    pendulum.draw(background)
    pygame.display.update()

pendulum = ball((int(win_width / 2),-100), 5)

#Main Loop
while not out:
    clock.tick(60)             

    for event in pygame.event.get():                     
        if event.type == pygame.QUIT:                    
            out = True                                   
        if event.type == pygame.MOUSEBUTTONDOWN:         
            pendulum = ball(pygame.mouse.get_pos(), 15)  
            angle, length = angle_Length()               
            acceleration = True                          

    if acceleration:   # Increase acceleration and damping in the pendulum moviment
        Aacc = -0.005 * math.sin(angle)
        vel += Aacc
        vel *= 1 - 1e-09  # damping factor
        angle += vel
        get_path(angle, length)

    redraw()

pygame.quit()
