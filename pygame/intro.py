import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("mohsen")

red = (255, 0, 0)
blue = (0, 0, 255)

turn = 0
running = True
while True:
    pygame.event.pump()

    if turn == 0:
        screen.fill(red)
    else:
        screen.fill(blue)
    turn = 1 - turn
    pygame.display.update()
    pygame.time.delay(1000)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if not running:
        pygame.quit()



