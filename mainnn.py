import pygame

import os
import pygame.font
pygame.font.init()

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('puvi')

BACKGROUND = pygame.image.load(os.path.join("images","background.jpg")).convert()

play = (200, 140, 115, 30)
help = (200, 200, 115, 40)
story= (200, 260, 115, 40)


large = pygame.font.Font("FreightSansBold.otf", 85)
medium = pygame.font.Font("FreightSansBold.otf", 40)
small = pygame.font.Font("FreightSansBold.otf", 35)
Vsmall = pygame.font.Font("FreightSansBold.otf", 18)
#### FOR MAIN ####
HEADING = large.render("GAME NAME", True, (255,255,255))
VERSION = Vsmall.render("Version 2.1", True, (255,255,255))

PLAY= medium.render("PLAY", True, (255,255,255))
PLAY_H = medium.render("PLAY", True, (200,200,200))

HELP = medium.render("HELP", True, (255,255,255))
HELP_H = medium.render("HELP", True, (200,200,200))

STORY= medium.render("STORY", True, (255,255,255))
STORY_H = medium.render("STORY", True, (200,200,200))


    
def showMain():
    WHITE = (255,255,255)

    win.blit(BACKGROUND, (0, 0))
    win.blit(HEADING,(85,20))
    win.blit(VERSION,(340,100))
    
   
     
    win.blit(PLAY, (play[0],play[1]))
    win.blit(HELP, (help[0],help[1]))
    win.blit(STORY, (story[0],story[1]))
   
    
running = True
while running:
    pygame.display.flip()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
    
            if play[0] < x < (play[0]+play[2]) and \
               play[1] < y < (play[1]+play[3]):
               import runpage2
            elif help[0] < x < (help[0]+help[2]) and \
               help[1] < y < (help[1]+help[3]):
               print("Coming soon")
            elif story[0] < x < (story[0]+story[2]) and \
               story[1] < y < (story[1]+story[3]):
                print("Coming soon")
           
          
        showMain()
        x,y = pygame.mouse.get_pos() 
        if play[0] < x < (play[0]+play[2]) and \
           play[1] < y < (play[1]+play[3]):
            win.blit(PLAY_H, (play[0], play[1]))
    
        elif help[0] < x < (help[0]+help[2]) and \
           help[1] < y < (help[1]+help[3]):
            win.blit(HELP_H, (help[0],help[1]))
        
        elif story[0] < x < (story[0]+story[2]) and \
           story[1] < y < (story[1]+story[3]):
            win.blit(STORY_H, (story[0],story[1]))
        
       
            
            
            
pygame.quit()