# Swiss NinjaFight pygame v 0.0
# By Geiser Father & Son


# Import and initialize the pygame library

import pygame
import time

pygame.init()


#Hero class

class Hero:
    
    def __init__(self):
        self.pic  = pygame.image.load("../Pictures/hero0_marche.png")
        self.pic = pygame.transform.scale(self.pic,(100,100))
        
        self.pic_marche = self.pic.copy()
        
        self.pic_attack  = pygame.image.load("../Pictures/hero0_sabreattack.png")
        self.pic_attack = pygame.transform.scale(self.pic_attack,(100,100))
        
        self.pic_sdefence  = pygame.image.load("../Pictures/hero0_sabredefence.png")
        self.pic_sdefence = pygame.transform.scale(self.pic_sdefence,(100,100))
        
        self.pic_arrow  = pygame.image.load("../Pictures/hero0_arrow.png")
        self.pic_arrow = pygame.transform.scale(self.pic_arrow,(100,140))
        
        self.pic_bullet  = pygame.image.load("../Pictures/arrow.png")
        self.pic_bullet = pygame.transform.scale(self.pic_bullet,(100,15))
        
        self.posx = 800
        self.posy = 400
        
        self.target_x = 640
        self.target_y = 360
        
    def show(self,screen) :
        screen.blit(self.pic,(self.posx,self.posy))
        
    
    def shoot(self,screen) :
        '''
        start = (self.posx,self.posy)
        target = (self.target_x,self.target_y)
        
        for i in range(10) :
            screen.blit(self.pic_bullet,(i*50,i*50))
            time.sleep(0.1)
            '''
        pass
        

#initialisation Objects

Hero1  = Hero()

# Set up the background window and Characters
bg = pygame.image.load("../Pictures/paysage0.png")
bg = pygame.transform.scale(bg, (1280, 720))

hero_walk = pygame.image.load("../Pictures/hero0_marche.png")
hero_walk = pygame.transform.scale(hero_walk,(100,100))

screen = pygame.display.set_mode([1280, 720])


# Run until the user asks to quit

running = True

while running:
    
    #background
    screen.blit(bg, (0, 0))
    
    


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Hero1.posx -= 10
            if event.key == pygame.K_RIGHT:
                Hero1.posx += 10
            if event.key == pygame.K_UP:
                Hero1.posy -= 10
            if event.key == pygame.K_DOWN:
                Hero1.posy += 10
                

            if event.key == pygame.K_LEFT and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                Hero1.posx -= 50
            if event.key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                Hero1.posx += 50
            if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                Hero1.posy -= 50
            if event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                Hero1.posy += 50
                
            if event.key == pygame.K_RETURN:
                Hero1.pic = Hero1.pic_attack
                
            if event.key == pygame.K_d:
                Hero1.pic = Hero1.pic_sdefence
                
            if event.key == pygame.K_a:
                Hero1.pic = Hero1.pic_arrow
                Hero1.shoot(screen)
            
        if event.type == pygame.KEYUP:
            if event.key in [ pygame.K_RETURN,pygame.K_d,pygame.K_a ]:
                Hero1.pic = Hero1.pic_marche
                
        
        if event.type == pygame.MOUSEBUTTONDOWN :
            Hero1.target_x,Hero1_target_y = pygame.mouse.get_pos()

                

    
    Hero1.show(screen)


    # Flip the display

    pygame.display.flip()


# mainloop interupted it is Time to quit.

pygame.quit()