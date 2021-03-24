import pygame

# to fade the screen


def fade(width, height):
    fade = pygame.surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawwindow()
        win.bilt(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

# a button class
class button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        if outline:
            pygame.draw.rect(win, outline, self.x - 2, self.y - 2, self.width + 4, self.height + 4)
            if self.text != "":
                font = pygame.font.SysFont("comics", 60)
                text = font.render(self.text, 1, (0, 0, 0))
                win.bilt(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

                def isover():
                    if self.x < pos[0] < self.x + self.width:
                        if self.y < pos[1] < self.y + self.height:
                            return True
                    return False
