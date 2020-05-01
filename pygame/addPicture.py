import pygame
img = pygame.image.load('/home/ahmadam/python/quera/pygame/sq.png')

white = (255, 255, 255)
screen = pygame.display.set_mode((640, 480))
screen.fill((white))

x, y = 0, 0
running = True
for i in range(58):
    screen.fill((white))
    screen.blit(img,(x, y))
    x, y = x + 5, y + 4
    pygame.display.update()
    pygame.time.delay(30)
    pygame.event.pump()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if not running:
        pygame.quit()
pygame.image.save(screen, '/home/ahmadam/python/quera/pygame/out.png')

img = pygame.image.load('/home/ahmadam/python/quera/pygame/out.png')
size = img.get_rect().size
pic_string = pygame.image.tostring(img, 'RGB')
img2 = pygame.image.fromstring(pic_string, size, 'RGB')
pygame.image.save(img2, '/home/ahmadam/python/quera/pygame/outed.png')