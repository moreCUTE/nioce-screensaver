import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("The best Pong ever")


bx = random.randrange(0,300)
by = random.randrange(0,300)
bx1 = random.randrange(0,300)
by1 = random.randrange(0,300)
bx2 = random.randrange(0,300)
by2 = random.randrange(0,300)
bx3 = random.randrange(0,300)
by3 = random.randrange(0,300)
bx4 = random.randrange(0,300)
by4 = random.randrange(0,300)
bVx = 3
bVy = 3
bVx1 = 3
bVy1 = 3
bVx2 = 3
bVy2 = 3
bVx3 = 3
bVy3 = 3
bVx4 = 3
bVy4 = 3
doExit = False
clock = pygame.time.Clock()
while not doExit:
    clock.tick(60)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
           

    bx += bVx
    by += bVy
    bx1 += bVx1
    by1 += bVy1
    bx2 += bVx2
    by2 += bVy2
    bx3 += bVx3
    by3 += bVy3
    bx4 += bVx4
    by4 += bVy4
   


    if bx < 0 or bx + 20 > 680:
        bVx *= -1
    if by < 0 or by + 20 > 470:
        bVy *= -1
    if bx1 < 0 or bx1 + 20 > 680:
        bVx1 *= -1
    if by1 < 0 or by1 + 20 > 470:
        bVy1 *= -1
    if bx2 < 0 or bx2 + 20 > 680:
        bVx2 *= -1
    if by2 < 0 or by2 + 20 > 470:
        bVy2 *= -1
    if bx3 < 0 or bx3 + 20 > 680:
        bVx3 *= -1
    if by3 < 0 or by3 + 20 > 470:
        bVy3 *= -1
    if bx4 < 0 or bx4 + 20 > 680:
        bVx4 *= -1
    if by4 < 0 or by4 + 20 > 470:
        bVy4 *= -1




#___________________________________RENDER SECTION____________________________________________________
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 74)
    text = font.render(str("V"),1, (0, 0, 250))
    screen.blit(text, (bx, by))
    text = font.render(str("D"),1, (0, 0, 250))
    screen.blit(text, (bx+30, by))
    text = font.render(str("D"),1, (0, 0, 250))
    screen.blit(text, (bx-30, by))
    text = font.render(str(":O"),1, (0, 0, 250))
    screen.blit(text, (bx3, by3))
    text = font.render(str(":)"),1, (0, 0, 250))
    screen.blit(text, (bx4, by4))
    pygame.display.flip()
pygame.quit()

