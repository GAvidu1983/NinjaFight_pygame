# Simple pygame program


# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window
bg = pygame.image.load("../Pictures/paysage0.png")
bg = pygame.transform.scale(bg, (1280, 720))

hero_walk = pygame.image.load("../Pictures/hero0_marche.png")
hero_walk = pygame.transform.scale(hero_walk,(100,100))

screen = pygame.display.set_mode([1280, 720])


# Run until the user asks to quit

running = True

while running:
    
    screen.blit(bg, (0, 0))


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    #screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center

    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    screen.blit(hero_walk,(800,600))


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()