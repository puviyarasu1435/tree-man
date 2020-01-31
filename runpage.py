
#------------------------------------------------import moduls-------------------------------------------------------------------------------------------------------------
import pygame
import time
import os
import sys
from random import sample


#init worke
pygame.init()


#------------------------------------------------display and imagess--------------------------------------------------------------------------------------------------------
win=pygame.display.set_mode((1020,481))

#images of left and right and center
cleft=[pygame.image.load(os.path.join("images","TL1.png")),pygame.image.load(os.path.join("images","TL2.png")),pygame.image.load(os.path.join("images","TL3.png")),pygame.image.load(os.path.join("images","TL4.png"))]
cright=[pygame.image.load(os.path.join("images","TR1.png")),pygame.image.load(os.path.join("images","TR2.png")),pygame.image.load(os.path.join("images","TR3.png")),pygame.image.load(os.path.join("images","TR4.png"))]
char=pygame.image.load(os.path.join("images","png.png"))
#background images
bg=pygame.image.load(os.path.join("images","background1.png"))
#attck

eni=pygame.image.load(os.path.join("images","eni1.png"))

#------------------------------------------------assigning-------------------------------------------------------------------------------------------------------------------
#main assigning
run=True
jump=False
jumpCount=10
(b,n)=(0,0)
(x,y)=(21,367)
mo=0
bullets=[]
walkCount=0
facing=0
count=0
count2=0
randomlist=[380,340,380,390,305]
z=800
c=0
n=sample(randomlist,1)
class user(object):
    def __init__(self,x,y,left,right,standing,walkCount,facing,n,z):
        self.x = x
        self.y = y
        self.n = n
        self.z = z
        self.vel = 5
        self.jump = False
        self.left = left
        self.right = right
        self.walkCount = walkCount
        self.jumpCount = 10
        self.standing = standing
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):

        win.blit(bg,(0,0))
        if not(self.standing):
            if self.left:
                win.blit(eni,(800,240))
                win.blit(cleft[self.walkCount], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(eni,(800,240))
                win.blit(cright[self.walkCount], (self.x,self.y))
                self.walkCount +=1
        else:
            win.blit(char,(self.x, self.y-2))
            pygame.display.update()
    def dra(self,win):
        pygame.draw.circle(win,(255,255,255), (self.x,self.y), 5)
    def randomdraw(self,win):
        win.blit(eni,(800,240))
        pygame.draw.circle(win,(0,0,0), (self.z,self.n[0]), 5)
        pygame.display.update()

#===================================================looping==================================================================================================================
running = True
while running:
    pygame.time.delay(-10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    c+=0.5
    if c==10.0:
        win.blit(eni,(800,240))
        pygame.time.delay(1)
        n=sample(randomlist,1)
        c=0

    for bullet in bullets:
        if bullet.x < 1020 and bullet.x > 0:
            bullet.x += bullet.vel
            if (bullet.x>800) and (bullet.y<300) and (bullet.y>200):
                count+=1
                print("count",count)

        else:
            bullets.pop(bullets.index(bullet))


    

#--------------------------------------------background images blit-----------------------------------------------------------------------------------------------------------

    win.blit(bg,(0,0))
    standing= True
    left = False
    right = False
    win.blit(eni,(800,240))
    #left and right moveing
    keys=pygame.key.get_pressed()
#_______________________________________key pressing____________________________________________________________________________________________________________________

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(user(round(x + 5),round(y + 5),left,right,standing,walkCount, facing,n,z))

    if keys[pygame.K_LEFT] and x > 5:
        x -= 4
        left = True
        right = False
        standing = False
        if x>500:
            mo-=10
    elif keys[pygame.K_RIGHT] and x <= 2010:
        x += 4
        right = True
        left = False
        standing = False
        if x>=500:
            mo+=10
    else:
        standing = True
        walkCount = 0
        
    
    if not(jump):
        if keys[pygame.K_UP]:
            jump = True
            right = False
            left = False
            walkCount = 0
        
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10
    
    man = user(x, y,left,right,standing,walkCount,facing,n,z)
    
    man = user(x, y,left,right,standing,walkCount,facing,n,z)
#------------------------------------------------cheking----------------------------------------------------------------------------------------------------------------
    win.blit(bg,(0,0))
#------------------------------------------------------------enimie------------------------------------------------------------------------------------------------------------------------
    man.draw(win)
    walkCount+=1
    if walkCount + 1 >= 4:
        walkCount = 0
    for bullet in bullets:
        bullet.dra(win)
    for i in randomlist:
        win.blit(eni,(800,240))
        z-=1
        if (z==x):
          count2+=1
          print(count2)
        win.blit(eni,(800,240))
        man.randomdraw(win)
        if z<=100:
            win.blit(eni,(800,240))
            z=800

    win.blit(eni,(800,240))

    
    
    
    
    
    
    
    
    
    
#-----------------------------------------------display.update----------------------------------------------------------------------------------------------------------
    pygame.display.update()


                    
#=================================================quit game============================================================================================================
pygame.quit()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

