
#------------------------------------------------import moduls-------------------------------------------------------------------------------------------------------------
import pygame
import time
import os
import leaf

#init worke
pygame.init()


#------------------------------------------------display and imagess--------------------------------------------------------------------------------------------------------
win=pygame.display.set_mode((1020,574))

#images of left and right and center
cleft=[pygame.image.load(os.path.join("images","TL1.png")),pygame.image.load(os.path.join("images","TL2.png")),pygame.image.load(os.path.join("images","TL3.png")),pygame.image.load(os.path.join("images","TL4.png"))]
cright=[pygame.image.load(os.path.join("images","TR1.png")),pygame.image.load(os.path.join("images","TR2.png")),pygame.image.load(os.path.join("images","TR3.png")),pygame.image.load(os.path.join("images","TR4.png"))]
center=pygame.image.load(os.path.join("images","png.png"))
#background images
bg=pygame.image.load(os.path.join("images","puvi.jpg"))
#attck
leaf=pygame.image.load(os.path.join("images","leaf.png"))

#------------------------------------------------assigning-------------------------------------------------------------------------------------------------------------------
#main assigning
run=True
jump=False
jumpcount=10
(b,n)=(0,0)
(x,y)=(21,500)
mo=0

#sub assigning



#===================================================looping==================================================================================================================
while run:
    #quit game
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            
            run=False
            break
#--------------------------------------------background images blit-----------------------------------------------------------------------------------------------------------

    win.blit(bg,(0-mo,0))
    win.blit(bg,(1020-mo,0))
    win.blit(bg,(2040-mo,0))
   
    #left and right moveing
    bullet=False
    left=False
    right=False
    keys=pygame.key.get_pressed()
#____________________________________________key pressing____________________________________________________________________________________________________________________

#--------------------------------------------left move-----------------------------------------------------------------------------------------------------------------------
    if keys[pygame.K_LEFT] and x>20:
        x-=3
        left=True
        right=False
        if x<624:
            mo-=10
    #left images
    if (left==True) and (right==False):
        win.blit(cleft[b],(x,y))
        b+=1
        pygame.display.update()
       
#-------------------------------------------right move-----------------------------------------------------------------------------------------------------------------------
    if keys[pygame.K_RIGHT] and x<2020:
        x+=3
        left=False
        right=True
        if x<624:
            mo+=10
    #right images
    if (right==True)and (left==False):
        win.blit(cright[n],(x,y))
        n+=1
        pygame.display.update()
       
       
#-------------------------------------------rearrang-------------------------------------------------------------------------------------------------------------------------
    if (b==4) or (n==4):
        b=0
        n=0
   
#--------------------------------------------jumping-------------------------------------------------------------------------------------------------------------------------
    if (jump!=True):
        if keys[pygame.K_UP]:
            jump=True
    elif jumpcount>=-10:
        neg=1
        print(jump,"--")
        if jumpcount<0:
            neg=-1
        y-=(jumpcount**2)
        y-=1
        jumpcount-=1
        y+=(jumpcount**2)
    elif(neg==-1):
        jump=False
        jumpcount=10
   
#----------------------------------------------center images-------------------------------------------------------------------------------------------------------------
    if not(left) and not (right):
        win.blit(center,(x,y-5))

#------------------------------------------------cheking----------------------------------------------------------------------------------------------------------------
    print(x,y)
    print("x+300",x+300)
   
   
#------------------------------------------------------------enimie------------------------------------------------------------------------------------------------------------------------
    if keys[pygame.K_SPACE]:
        bullet=True
        leaf.leafac(x,y,leaf,b,n,cright,cleft)

#-----------------------------------------------display.update----------------------------------------------------------------------------------------------------------
    pygame.display.update()
    
    

                    


def prompt(win):
    pygame.draw.rect(win, (0,0,0), (70, 140, 360, 150))
    pygame.draw.rect(win, (255,255,255), (70, 140, 360, 150), 4)
    win.blit(MESSAGE1, (92,140))
    win.blit(MESSAGE2, (142,180))
    win.blit(YES, (100, 240))
    win.blit(NO, (340,240))
    pygame.draw.rect(win, (255,255,255), (85, 140, 330, 82), 2)
    pygame.draw.rect(win, (255,255,255), (100, 240, 60, 30), 2)
    pygame.draw.rect(win, (255,255,255), (340, 240, 50, 30), 2)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 240 < y < 270:
                    if 100 < x < 160:
                        return True
                    elif 340 < x < 390:
                        return False



                    
#=================================================quit game============================================================================================================
pygame.QUIT()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

