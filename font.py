
import pygame.font
pygame.font.init()

large = pygame.font.Font("FreightSansBold.otf", 85)
medium = pygame.font.Font("FreightSansBold.otf", 40)
small = pygame.font.Font("FreightSansBold.otf", 35)
Vsmall = pygame.font.Font("FreightSansBold.otf", 18)
#### FOR MAIN ####
HEADING = large.render("VIP Chess", True, (255,255,255))
VERSION = Vsmall.render("Version 2.1", True, (255,255,255))

SINGLE = medium.render("Single Player", True, (255,255,255))
SINGLE_H = medium.render("Single Player", True, (200,200,200))














