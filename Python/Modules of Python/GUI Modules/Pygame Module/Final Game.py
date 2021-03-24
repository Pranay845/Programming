import pygame

pygame.init()  # this is for starting the pygame

win = pygame.display.set_mode((852, 480))  # making a window and giving it the size

pygame.display.set_caption("First Game")  # setting title

# A list of images for game
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()  # for changing the fps

# Sound effects for the game
bulletSound = pygame.mixer.Sound('Gunfire.wav')
hitSound = pygame.mixer.Sound('PUNCH.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

score = 0  # score for player


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x  # for placing the character
        self.y = y
        self.width = width  # his size
        self.height = height
        self.vel = 5  # speed for the character
        self.isJump = False  # for jumping the character
        self.left = False  # for keeping track of character direction
        self.right = False
        self.walkCount = 0  # the steps he moves
        self.jumpCount = 10  # for counting jumps
        self.standing = True  # to keep track of his standing
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)  # a hitbox for the player

    def draw(self, win):  # draws the character
        if self.walkCount + 1 >= 27:  # to control the images
            self.walkCount = 0

        if not self.standing:
            if self.left:  # to change the image to left character
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:  # to change the image to right character
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:  # if he is standing
            if self.right:  # show right image
                win.blit(walkRight[0], (self.x, self.y))
            else:  # or left image
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)  # making the hitbox
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):  # for hitting the enemy
        self.isJump = False  # resetting the value
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)  # the font of of score
        text = font1.render('-5', 1, (255, 0, 0))  # to show the removed points when he touches the enemy
        win.blit(text, (250 - (text.get_width() / 2), 200))  # to show the score on screen
        pygame.display.update()  # updating the display
        i = 0  # for clean exit while delay
        while i < 200:
            pygame.time.delay(10)  # to show the score for some time
            i += 1  # to run while loop
            for event in pygame.event.get():  # brings all the events
                if event.type == pygame.QUIT:  # for clean exit
                    i = 201  # To break the loop
                    pygame.quit()  # to quit


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x  # place of it
        self.y = y
        self.radius = radius  # size of it
        self.color = color  # and the color
        self.facing = facing  # facing of it (left,right)
        self.vel = 8 * facing  # speed of it

    def draw(self, win):  # drawing the circle to screen
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    # images for enemy
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x  # for placing the character
        self.y = y
        self.width = width  # his size
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0  # the steps he moves
        self.vel = 3  # speed for the character
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)  # a hitbox for the enemy
        self.health = 10  # health for him
        self.visible = True  # to remove him from screen

    def draw(self, win):  # draws the character
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:  # to control the images
                self.walkCount = 0

            if self.vel > 0:  # continually moving right until the end
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:  # continually moving left until the end
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))  # the green heath bar
            pygame.draw.rect(win, (0, 128, 0), (
                self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))  # the deletion of points
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)  # a hit box for enemy
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:  # check for positive
            if self.x + self.vel < self.path[1]:  # check for the left path end
                self.x += self.vel  # resetting the values
            else:
                self.vel = self.vel * -1  # to move the character left
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:  # check for the right path end
                self.x += self.vel  # resetting the values
            else:
                self.vel = self.vel * -1  # to move the character right
                self.walkCount = 0

    def hit(self):  # to hit
        if self.health > 0:  # check for positive
            self.health -= 1  # delete 1 health
        else:
            self.visible = False  # remove him from screen


def redrawGameWindow():  # a function for drawing the window after movement
    win.blit(bg, (0, 0))  # This will draw our background image at (0,0)
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))  # makes score
    win.blit(text, (350, 10))  # shows score
    man.draw(win)  # drawing man and enemy
    goblin.draw(win)
    for bullet in bullets:  # drawing the bullets
        bullet.draw(win)

    pygame.display.update()  # updating the display


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)  # giving font
man = player(200, 410, 64, 64)  # a instance
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0  # to count shoot of bullets
bullets = []  # a list of bullets
run = True
while run:  # a loop for checking events
    clock.tick(27)  # to start fps 27 because we that many images

    if goblin.visible:  # check for enemy
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[
            1]:  # check for dimensions of hit box colliding of width
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[
                2]:  # check for dimensions of hit box colliding of height
                man.hit()  # called hit method
                score -= 5  # changed the score of player

    if shootLoop > 0:  # check for positive
        shootLoop += 1  # increasing it
    if shootLoop > 3:  # check for more
        shootLoop = 0  # reseted it

    for event in pygame.event.get():  # brings all the events
        if event.type == pygame.QUIT:  # for clean exit
            run = False

    for bullet in bullets:  # for every bullet
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:  # check for dimensions of hit box colliding of width
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:  # check for dimensions of hit box colliding of height
                hitSound.play()  # to play the sound
                goblin.hit()  # hit of enemy
                score += 1  # increasing the score after bullet hit
                bullets.pop(bullets.index(bullet))  # removes the bullet

        if 500 > bullet.x > 0:  # check for bullet in screen
            bullet.x += bullet.vel  # setted to speed
        else:  # removing the bullet
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()  # collects all the events

    if keys[pygame.K_SPACE] and shootLoop == 0:  # to hit bullets
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:  # to move left
        man.x -= man.vel  # to move character
        man.left = True  # for no confusion to computer
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:  # to move left
        man.x += man.vel  # to move character
        man.right = True  # for no confusion to computer
        man.left = False
        man.standing = False
    else:
        man.standing = True  # for confirmation that the character is not moving
        man.walkCount = 0

    if not man.isJump:  # to jump
        if keys[pygame.K_UP]:
            man.isJump = True  # for jumping
            man.right = False  # for confirmation that the character is not moving before jumping
            man.left = False
            man.walkCount = 0
    else:  # to jump the character
        if man.jumpCount >= -10:  # for jumping
            neg = 1
            if man.jumpCount < 0:  # check for its a negative number
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg  # to move down
            man.jumpCount -= 1
        else:
            man.isJump = False  # to conclude the jumping
            man.jumpCount = 10

    redrawGameWindow()  # for changing images(fps)

pygame.quit()  # to complete

# Documentation: https://www.pygame.org/docs/
