import pygame

#creating window
background_colour = (245, 245, 245)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bugz World')


screen.fill(background_colour)
pygame.display.flip()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

