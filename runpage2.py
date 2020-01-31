
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
char=pygame.image.load(os.path.join("images","png.png"))
#background images
bg=pygame.image.load(os.path.join("images","puvi.jpg"))
#attck
leaf=pygame.image.load(os.path.join("images","leaf.png"))

#------------------------------------------------assigning-------------------------------------------------------------------------------------------------------------------
#main assigning
jump=False
jumpCount=10
(b,n)=(0,0)
(x,y)=(21,500)
mo=0
bullets=[]
walkCount=0
facing=0
X=x + 700

class user(object):
    def __init__(self,x,y,left,right,standing,walkCount,facing):
        self.x = x
        self.y = y
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


        if not(self.standing):
            if self.left:
                win.blit(cleft[self.walkCount], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(cright[self.walkCount], (self.x,self.y))
                self.walkCount +=1
        else:
            win.blit(char,(self.x, self.y))
        pygame.display.update()
    def dra(self,win):
        pygame.draw.circle(win,(0,0,0), (self.x,self.y), 3)
        print("x bu",self.x)
#===================================================looping==================================================================================================================
while True:
    #quit game
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             sys.QUIT()
             break
    
    for bullet in bullets:
        if bullet.x <1020 and bullet.x > 0 :
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

#--------------------------------------------background images blit-----------------------------------------------------------------------------------------------------------

    win.blit(bg,(0,0))
    standing= True
    left = False
    right = False
    
    
    #left and right moveing
    keys=pygame.key.get_pressed()
#_______________________________________key pressing____________________________________________________________________________________________________________________

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(user(round(x + 5),round(y + 5),left,right,standing,walkCount, facing))


    if keys[pygame.K_LEFT] and x > 5:
        x -= 2
        left = True
        right = False
        standing = False
        if x>500:
            mo-=10
    elif keys[pygame.K_RIGHT] and x <=570:
        x += 4
        right = True
        left = False
        standing = False
        if x>=500:
            mo+=15
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
 

    man = user(x, y,left,right,standing,walkCount,facing)
#------------------------------------------------cheking----------------------------------------------------------------------------------------------------------------
    print(x,y)
    print("x+300",mo)
    
   
    win.blit(bg,(0,0))
#------------------------------------------------------------enimie------------------------------------------------------------------------------------------------------------------------
    man.draw(win)
    walkCount+=1
    if walkCount + 1 >= 4:
        walkCount = 0
    for bullet in bullets:
        bullet.dra(win)

#-----------------------------------------------display.update----------------------------------------------------------------------------------------------------------
    pygame.display.update()


                    
#=================================================quit game============================================================================================================
pygame.QUIT()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

