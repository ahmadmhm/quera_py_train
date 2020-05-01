import pygame
from math import pi

pygame.init()
screen = pygame.display.set_mode((800, 600))

red = (252.2, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (128, 128, 128)

screen.fill(gray)

pygame.draw.line(screen, red, (300.4, 300), (600, 400), 10)
pygame.draw.circle(screen, red, (200, 200), 20, 6)
pygame.draw.rect(screen, blue, (400, 400, 30, 80), 20)
pygame.draw.ellipse(screen, blue, (450, 450, 100, 50), 10)
pygame.draw.polygon(screen, green, [(700, 500), (600, 500), (550, 450), (650, 440)], 10)
pygame.draw.lines(screen, green, True, [(700, 200), (600, 200), (550, 150), (650, 140)], 20)
pygame.draw.lines(screen, green, False, [(700, 350), (600, 350), (550, 300), (650, 290)], 30)
pygame.draw.arc(screen, red,  (210, 75, 150, 125), 3*pi/2, 2*pi, 25)

pygame.display.update()
running = True
while True:
    pygame.event.pump()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if not running:
        pygame.quit()