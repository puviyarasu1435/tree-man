import pygame

import os
import webbrowser
pygame.font.init()

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('puvi')

BACKGROUND = pygame.image.load(os.path.join("images","background.jpeg")).convert()

play = (200, 140, 115, 30)
help = (200, 200, 115, 40)
story= (184, 260, 115, 40)
version=(400,470, 115, 40)
new=2
url="http://www.google.com";
large = pygame.font.Font("FreightSansBold.otf", 80)
medium = pygame.font.Font("FreightSansBold.otf", 40)
small = pygame.font.Font("FreightSansBold.otf", 35)
Vsmall = pygame.font.Font("FreightSansBold.otf", 18)

HEADING = large.render("TREE MAN", True, (250,250,250))
VERSION = Vsmall.render("Version ", True, (255,255,255))
VERSION_H = Vsmall.render("Version ", True, (200,200,200))

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
   
    
   
     
    win.blit(PLAY, (play[0],play[1]))
    win.blit(HELP, (help[0],help[1]))
    win.blit(STORY, (story[0],story[1]))
    win.blit(VERSION, (version[0],version[1]))
   
    
running = True
while running:
    pygame.display.flip()
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
    
            if play[0] < x < (play[0]+play[2]) and play[1] < y < (play[1]+play[3]):
               import runpage
            elif help[0] < x < (help[0]+help[2]) and help[1] < y < (help[1]+help[3]):
               print("Coming soon")
            elif story[0] < x < (story[0]+story[2]) and story[1] < y < (story[1]+story[3]):
                print("Coming soon")
            elif version[0] < x < (version[0]+version[2]) and version[1] < y < (version[1]+version[3]):
                
                 webbrowser.open(url,new=new);
          
        showMain()
        x,y = pygame.mouse.get_pos() 
        if play[0] < x < (play[0]+play[2]) and play[1] < y < (play[1]+play[3]):
            win.blit(PLAY_H, (play[0], play[1]))
            pygame.draw.rect(win, (255,255,255), (195, 135, 110, 50), 3)
    
        elif help[0] < x < (help[0]+help[2]) and help[1] < y < (help[1]+help[3]):
            win.blit(HELP_H, (help[0],help[1]))
            pygame.draw.rect(win, (255,255,255), (195, 195, 110, 50), 3)
            
        elif story[0] < x < (story[0]+story[2]) and story[1] < y < (story[1]+story[3]):
            win.blit(STORY_H, (story[0],story[1]))
            pygame.draw.rect(win, (255,255,255), (175, 255, 139,50), 3)
            
        elif version[0] < x < (version[0]+version[2]) and version[1] < y < (version[1]+version[3]):
            win.blit(VERSION_H, (version[0],version[1]))
            pygame.draw.rect(win, (255,255,255), (394,467,70,30), 3)
            
            
            
pygame.quit()
