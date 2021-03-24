"""
Pygame Module is used for Making Games in Python.
"""

import pygame

pygame.init()  # this is for starting the pygame
window = pygame.display.set_mode((500, 600))  # making a window and giving it the size
pygame.display.set_caption("my game")  # setting title
screenwidth = 500
jump = False
jumpconut = 10
x = 50  # setting variables for the rectangle
y = 50
width = 40
height = 60
vel = 10  # this the speed of movement
run = True
while run:  # a loop for clean exit and also for movement of rectangle
    pygame.time.delay(100)  # this is for stability
    for event in pygame.event.get():  # to collect the events
        if event.type == pygame.QUIT:  # for a clean exit without problem
            run = False
    keys = pygame.key.get_pressed()  # collects the keys events
    if keys[pygame.K_LEFT] and x > vel:  # for left key this is for the staying in screen because the place of the
        # rect reaches 10 then this will not happen
        x -= vel  # the coordinate system so to move left we should subtract x coordinate with speed by that it will
        # move back 50-10 =40 so it x is 40
    if keys[pygame.K_RIGHT] and x < screenwidth - width - vel:  # for right key the screen the width is given because
        # the rect stops after the screen vel for the space between the rect and screen,vel is not compulsory
        x += vel  # to move right
    if not jump:
        if keys[pygame.K_UP] and y > vel:  # for up key in screen because the place of the rect reaches y=10 then
            # this will not happen
            y -= vel  # to move up we should subtract the y with speed
        if keys[pygame.K_DOWN] and y < screenwidth - height - vel:  # for down key the screen the height is given
            # because the rect stops after the screen vel for the space between the rect and screen,vel is not
            # compulsory
            y += vel  # to move down
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpconut >= -10:  # for jumping
            neg = 1
            if jumpconut < 0:  # check for its a negative number
                neg = -1
            y -= (jumpconut ** 2) * 0.5 * neg
            jumpconut -= 1  # to move down
        else:
            jump = False  # to conclude the jumping
            jumpconut = 10
    window.fill((0, 0, 0))  # for showing only one rectangle
    pygame.draw.rect(window, (255, 0, 0), (x, int(y), width, height))  # making the rectangle
    pygame.display.update()  # to move rectangle
pygame.quit()  # to exit
