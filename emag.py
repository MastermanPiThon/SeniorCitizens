# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 750, 750
screen=pygame.display.set_mode((width, height))
playerpos=[592,8]
playerpos1 = playerpos
keys = [False, False, False, False]
scale = 12
playerthere = True
white = screen.get_at((0, 0))
q = False

# 3 - Load images
player = pygame.image.load("pictures/player.png")
player = pygame.transform.scale (player, (scale*5,scale*5))
maze = pygame.image.load("pictures/mazes/level1.jpeg")
maze = pygame.transform.scale (maze, (width, height))
                        
screen.blit(maze, (0,0))
# 4 - keep looping through
while not q:
    # 6 - draw the screen elements
    playerl = (int)(playerpos1[0]+(player.get_width()*.24))
    playert = (int)(playerpos1[1]+(player.get_height()*.13))
    playerr = (int)(playerl+(player.get_height()*.8))
    playerb = (int)(playert+(player.get_width()*.65))
    pygame.draw.rect(screen, 0xFFFFFF, (playerl, playert, player.get_width()*.65, player.get_height()*.8))
    if playerthere:
        screen.blit(player, playerpos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
            elif event.key == K_d:
                if playerthere == True:
                    playerthere = False
                elif playerthere == False:
                    playerthere = True
            elif event.key == K_s:
                scale += 1
            elif event.key == K_a:
                screen.fill(0x000000)
            elif event.key == K_q:
                q = True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False

    playerpos1 = playerpos

    # 9 - Move player
    if keys[0] and screen.get_at((playert, playerl)) == white and screen.get_at((playert, playerr)) == white:
        playerpos[1] -= scale*.25
    elif keys[2]:
        playerpos[1] += scale*.25
    if keys[1]:
        playerpos[0] -= scale*.25
    elif keys[3]:
        playerpos[0] += scale*.25
