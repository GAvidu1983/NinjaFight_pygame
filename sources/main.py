# Swiss NinjaFight pygame v 0.0
# By Geiser Father & Son


# Import and initialize the pygame library

import pygame
import time
import random

pygame.init()



#Hero class

class Mechant:
    
    def __init__(self):
        
        self.pic  = pygame.image.load("../Pictures/mechant0_marche.png")
        self.pic = pygame.transform.scale(self.pic,(100,100))
        
        self.pic_static = self.pic.copy()
        
        self.pic_marche  = pygame.image.load("../Pictures/mechant0_marche.png")
        self.pic_marche = pygame.transform.scale(self.pic_marche,(100,100))
        
        self.pic_attack  = pygame.image.load("../Pictures/mechant0_sabreattack.png")
        self.pic_attack = pygame.transform.scale(self.pic_attack,(100,100))
        
        self.pic_sdefence  = pygame.image.load("../Pictures/mechant0_sabredefence.png")
        self.pic_sdefence = pygame.transform.scale(self.pic_sdefence,(100,100))
        
        self.pic_arrow  = pygame.image.load("../Pictures/hero0_arrow.png")
        self.pic_arrow = pygame.transform.scale(self.pic_arrow,(100,140))
        
        self.pic_jump  = pygame.image.load("../Pictures/hero0_jump.png")
        self.pic_jump = pygame.transform.scale(self.pic_jump,(100,150))
        
        self.pic_shuriken  = pygame.image.load("../Pictures/hero0_shuriken.png")
        self.pic_shuriken = pygame.transform.scale(self.pic_shuriken,(100,100))
        
        self.pic_shield  = pygame.image.load("../Pictures/hero0_shield.png")
        self.pic_shield = pygame.transform.scale(self.pic_shield,(100,100))
        
        self.posx = 300
        self.posy = 400
        
        self.pos = (self.posx,self.posy)
        
        self.target_x = 640
        self.target_y = 360
        
        self.target = (self.target_x,self.target_y)
        
    def show(self,screen) :
        screen.blit(self.pic,(self.posx,self.posy))
        
    def update(self) :
        rx = random.randrange(-20,20,2)
        ry = random.randrange(-20,20,2)
        mv = random.randrange(0,10,1)
        if mv > 4 :
            self.posx = self.posx + rx
            self.posy = self.posy + ry
        if self.posx > 800 : self.posx = 800
        if self.posx < 200 : self.posx = 200
        if self.posy > 600 : self.posy = 600
        if self.posy < 200 : self.posy = 200
        
        self.pos = (self.posx ,self.posy)
        self.target = (self.target_x,self.target_y)



#Hero class

class Hero:
    
    def __init__(self):
        
        self.pic  = pygame.image.load("../Pictures/hero0_static.png")
        self.pic = pygame.transform.scale(self.pic,(100,100))
        
        self.pic_static = self.pic.copy()
        
        self.pic_marche  = pygame.image.load("../Pictures/hero0_marche.png")
        self.pic_marche = pygame.transform.scale(self.pic_marche,(100,100))
        
        self.pic_attack  = pygame.image.load("../Pictures/hero0_sabreattack.png")
        self.pic_attack = pygame.transform.scale(self.pic_attack,(100,100))
        
        self.pic_sdefence  = pygame.image.load("../Pictures/hero0_sabredefence.png")
        self.pic_sdefence = pygame.transform.scale(self.pic_sdefence,(100,100))
        
        self.pic_arrow  = pygame.image.load("../Pictures/hero0_arrow.png")
        self.pic_arrow = pygame.transform.scale(self.pic_arrow,(100,140))
        
        self.pic_jump  = pygame.image.load("../Pictures/hero0_jump.png")
        self.pic_jump = pygame.transform.scale(self.pic_jump,(100,150))
        
        self.pic_shuriken  = pygame.image.load("../Pictures/hero0_shuriken.png")
        self.pic_shuriken = pygame.transform.scale(self.pic_shuriken,(100,100))
        
        self.pic_shield  = pygame.image.load("../Pictures/hero0_shield.png")
        self.pic_shield = pygame.transform.scale(self.pic_shield,(100,100))
        
        self.posx = 800
        self.posy = 400
        
        self.pos = (self.posx,self.posy)
        
        self.target_x = 640
        self.target_y = 360
        
        self.target = (self.target_x,self.target_y)
        
    def show(self,screen) :
        screen.blit(self.pic,(self.posx,self.posy))
        
    def update(self) :
        self.pos = (self.posx,self.posy)
        self.target = (self.target_x,self.target_y)
        
        


class Arrows :
    
    def __init__(self):
        self.list = []   # [[(startx,starty),(endx,endy),(istx,isty),inc],()...]
        
        self.pic_bullet  = pygame.image.load("../Pictures/arrow.png")
        self.pic_bullet = pygame.transform.scale(self.pic_bullet,(100,15))
        
        self.step = 30
        
        
    def show(self,screen):
        
        for arr in self.list :
            screen.blit(self.pic_bullet,arr[2])
            
    def add(self,start,end) :
        self.list.append([start,end,start,0])
        
    def increment(self) :
        step = self.step
        for arr in self.list :
            x0,y0 = arr[0]
            x1,y1 = arr[1]
            dx = (x1-x0)/step
            dy = (y1-y0) /step
            x,y = arr[2]
            arr[2] = (x+dx,y+dy)
            arr[3] += 1
            if arr[3] >= self.step :
                self.list.remove(arr)
                

class Shuriken :
    
    def __init__(self):
        self.list = []   # [[(startx,starty),(endx,endy),(istx,isty),inc],()...]
        
        self.pic_sh  = pygame.image.load("../Pictures/shuriken.png")
        self.pic_sh = pygame.transform.scale(self.pic_sh,(40,25))
        
        self.step = 160
               
    def show(self,screen):
        
        for arr in self.list :
            screen.blit(self.pic_sh,arr[2])
            
    def add(self,start,end) :
        self.list.append([start,end,start,0])
        
    def increment(self) :
        step = self.step
        for arr in self.list :
            x0,y0 = arr[0]
            x1,y1 = arr[1]
            dx = (x1-x0)/step
            dy = (y1-y0) /step
            x,y = arr[2]
            arr[2] = (x+dx,y+dy)
            arr[3] += 1
            if arr[3] >= self.step :
                self.list.remove(arr)
                

            
        
        

#initialisation Objects

Hero1  = Hero()
Arrowl = Arrows()
Shurikenl = Shuriken()

Mechant1 = Mechant()

# Set up the background window and Characters
bg = pygame.image.load("../Pictures/paysage0.png")
bg = pygame.transform.scale(bg, (1280, 720))

hero_walk = pygame.image.load("../Pictures/hero0_marche.png")
hero_walk = pygame.transform.scale(hero_walk,(100,100))

screen = pygame.display.set_mode([1280, 720])


#set speed
clock = pygame.time.Clock()

# Run until the user asks to quit

running = True

while running:
    
    clock.tick(100)
    
    #background
    screen.blit(bg, (0, 0))
    
    Arrowl.increment()
    Shurikenl.increment()
    
    


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            
        if event.type == pygame.KEYDOWN:
            
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN] :
                Hero1.pic = Hero1.pic_marche
            
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
                
            if event.key == pygame.K_SPACE:
                Hero1.pic = Hero1.pic_jump
                Hero1.posy -= 160
                
            if event.key == pygame.K_d:
                Hero1.pic = Hero1.pic_sdefence
                
            if event.key == pygame.K_b:
                Hero1.pic = Hero1.pic_shield
                
            if event.key == pygame.K_s:
                Hero1.pic = Hero1.pic_shuriken
                Shurikenl.add(Hero1.pos,(0,Hero1.posy))
                
            if event.key == pygame.K_a:
                Hero1.pic = Hero1.pic_arrow
                Arrowl.add(Hero1.pos,Hero1.target)
            
        if event.type == pygame.KEYUP:
            if event.key in [ pygame.K_RETURN,pygame.K_d,pygame.K_a,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,
                              pygame.K_s,pygame.K_DOWN,pygame.K_SPACE,pygame.K_b ]:
                Hero1.pic = Hero1.pic_static
            if event.key == pygame.K_SPACE :
                Hero1.posy += 160
                
        
        if event.type == pygame.MOUSEBUTTONDOWN :
            Hero1.target_x,Hero1.target_y = pygame.mouse.get_pos()
            

                

    Hero1.update()
    Hero1.show(screen)
    Arrowl.show(screen)
    Shurikenl.show(screen)
    
    
    Mechant1.update()
    Mechant1.show(screen)


    # Flip the display

    pygame.display.flip()


# mainloop interupted it is Time to quit.

pygame.quit()