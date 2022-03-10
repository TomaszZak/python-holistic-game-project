import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Hello button")
test_colour = (255, 255, 255)
button_colour = (0, 0, 170)
button_over_colour = (255, 50, 50)
button_width = 100
button_hight = 50
button_rectangle = [(screen.get_width() - button_width) / 2,
                    (screen.get_height() - button_hight) / 2,
                    button_width, button_hight]
button_font = pygame.font.SysFont("Arial", 20)
button_text = button_font.render("Quit", True, test_colour)
screen.fill((100, 100, 100))

game_over = False
xPos, yPos = (0, 0)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:# wcisniecie przycisku myszy
            xPos, yPos = event.pos# pozycja mkursra podczas wcisniecia myszy
            if(button_rectangle[0] <= xPos <= button_rectangle[0] + button_rectangle[2] and # czy x jest w granicy przycisku
                    button_rectangle[1] <= yPos <= button_rectangle[1] + button_rectangle[3]):# czy y jest w granicy przycisku
                game_over = True
        if event.type == pygame.MOUSEMOTION:    # akcja na ruch mysza
            xPos, yPos = event.pos    # odczyt pozycji kursora po przesunieciu

    if (button_rectangle[0] <= xPos <= button_rectangle[0] + button_rectangle[2] and  # czy x jest w granicy przycisku
            button_rectangle[1] <= yPos <= button_rectangle[1] + button_rectangle[3]):  # czy y jest w granicy przycisku
        pygame.draw.rect(screen, button_over_colour, button_rectangle)   # rysujemy obiekt
    else:
        pygame.draw.rect(screen, button_colour, button_rectangle)   # rysujemy obiekt
    screen.blit(button_text, (button_rectangle[0] + (button_width - button_text.get_width()) / 2,
                              button_rectangle[1] + (button_hight - button_text.get_height()) / 2))    # pozycja tekstu na przycisku
    pygame.display.update()     # odswiezamy ekran po narysowaniu obiketu

pygame.quit()
