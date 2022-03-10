import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
sprite1 = pygame.image.load('./images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (50, 50))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
pygame.display.set_caption('Hello Resize')
screen.fill((0, 0, 0))
game_over = False
x, y = (0, 0)
clock = pygame.time.Clock()     # zegar sluzacy do odmierzania klatek na sekunde
while not game_over:
    dt = clock.tick(100)        # 100 frames per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:  # obiekt sledzi ruch myszy
            x, y = event.pos    # pozycjonowanie obiektu na aktualna pozycje kursora myszy
            x -= spriteWidth / 2    # wysrodkowanie spritea w osi x
            y -= spriteHeight / 2   # wysrodkowanie spritea w osi y
    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt   # jezeli chcemy zachowac stala szybkosc przesuwania sie obiektu niezaleznie od ilosci klatek na sekunde to nalezy skok pomnozyc razy ilosc klatek na sekunde
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x = 0
        y = 0

    if x > (screen.get_width() - spriteWidth):
        x = screen.get_width() - spriteWidth
    if y > (screen.get_height() - spriteHeight):
        y = screen.get_height() - spriteHeight
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
