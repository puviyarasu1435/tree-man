
#------------------------------------------------import moduls-------------------------------------------------------------------------------------------------------------
import pygame
import time
import os
import sys
from random import sample



#init worke
pygame.init()
pygame.font.init()


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

run=True
jump=False
jumpCount=10
(b,n)=(0,0)
(x,y)=(21,370)
mo=0
bullets=[]
walkCount=0
facing=0
count=0
count2=50
randomlist=[366,368,369,367,373,371,702,370]
c=0
n=sample(randomlist,1)
g=800
f=240
z=g
class user(object):
    def __init__(self,x,y,left,right,standing,walkCount,facing,n,z,text,text2):
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
        self.text=text
        self.text2=text2

    def draw(self, win):

        win.blit(bg,(0,0))
        if not(self.standing):

            if self.left:
                win.blit(eni,(g,f))
                win.blit(cleft[self.walkCount], (self.x,self.y))
                self.walkCount += 1
                win.blit(text,(20,0))
                win.blit(text2,(800,0))
            elif self.right:
                win.blit(eni,(g,f))
                win.blit(cright[self.walkCount], (self.x,self.y))
                self.walkCount +=1
                win.blit(text,(20,0))
                win.blit(text2,(800,0))
        else:
            win.blit(char,(self.x, self.y-5))
            pygame.display.update()
            win.blit(text,(20,0))
            win.blit(text2,(800,0))
    def dra(self,win):
        pygame.draw.circle(win,(255,255,255), (self.x,self.y), 5)
    def randomdraw(self,win):
        win.blit(eni,(g,f))
        pygame.draw.circle(win,(0,0,0), (self.z,self.n[0]), 5)
        pygame.display.update()
     



#===================================================looping==================================================================================================================
running = True
while running:
    font= pygame.font.Font("ALGER.TTF", 40)
    text=font.render(str(count2)+" %",1,(255,255,255))
    text2=font.render("socer "+str(count),1,(255,255,255))
    pygame.time.delay(-1000)
    win.blit(text,(20,0))
    win.blit(text2,(800,0))
    if g>=30:
        g-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    c+=1
    if c==100:
        win.blit(eni,(g,f))
        n=sample(randomlist,1)
        c=0
    if (x>g-2) or count2<=1 or count>=20 :

        break

    for bullet in bullets:
        pygame.time.delay(-10)
        if bullet.x < g+3 and bullet.x > 0:
            bullet.x += bullet.vel


        else:
            bullets.pop(bullets.index(bullet))

        if (bullet.x>g)  and (300>bullet.y>200):
            if bullet.x<g+10:
               count+=1


    for bullet in bullets:
        pygame.time.delay(-10)
        if bullet.x < g+3 and bullet.x > 0:
            bullet.x += bullet.vel


        else:
            bullets.pop(bullets.index(bullet))

        if (bullet.x>g)  and (300>bullet.y>200):
            if bullet.x<g+10:
               count+=1


    win.blit(bg,(0,0))
    standing= True
    left = False
    right = False
    win.blit(eni,(g,f))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(user(round(x + 5),round(y + 5),left,right,standing,walkCount, facing,n,z,text,text2))
    if keys[pygame.K_LEFT] and x > 5:
        x -= 10
        left = True
        right = False
        standing = False
        if x>500:
            mo-=10
    elif keys[pygame.K_RIGHT] and x <= 2010:
        x += 10
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
    win.blit(text,(20,0))
    win.blit(text2,(800,0))
    man = user(x, y,left,right,standing,walkCount,facing,n,z-1,text,text2)
    win.blit(bg,(0,0))
    man.draw(win)
    walkCount+=1
    if walkCount + 1 >= 4:
        walkCount = 0

    for i in randomlist:
        pygame.time.delay(-100000)
        win.blit(eni,(g,f))
        z-=3
        win.blit(eni,(g,f))
        man.randomdraw(win)
    for bullet in bullets:
        pygame.time.delay(-10)
        bullet.dra(win)

        if z<=10:
            win.blit(eni,(g,f))
            z=g

        if ((y>365) or (370<y)) and ((z+1<=x) or (x>=z-1)):
            count2-=1
      
    
    win.blit(eni,(g,f))
    win.blit(text,(20,0))
    win.blit(text2,(800,0))
    pygame.display.update()
    
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    if count<20:
        font= pygame.font.Font("ALGER.TTF", 60)
        text3=font.render(("game over"),1,(255,255,255))
        win.blit(text3,(400,100))
        pygame.display.update()
    elif count==20:
        font= pygame.font.Font("ALGER.TTF", 60)
        text4=font.render(("won!!!!!"),1,(255,255,255))
        win.blit(text4,(400,100))
        pygame.display.update()
    else:
        break
        
pygame.quit()
