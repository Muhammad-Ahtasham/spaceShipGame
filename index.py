import os
from turtle import left
import pygame
Width, Height = 900, 500
game = pygame.display.set_mode((Width, Height))
white =(255, 255, 255)
FPS = 30
veLoCitY = 5
spaceShipHeight, spaceShipWidth = 55, 40
LeftSpaceShipImage = pygame.image.load(os.path.join("Pics", "left.png"))
LeftSpaceShip = pygame.transform.rotate(pygame.transform.scale(LeftSpaceShipImage, (spaceShipHeight, spaceShipWidth)), 140)
RightSpaceShipImage = pygame.image.load(os.path.join("Pics", "right.png"))
RightSpaceShip = pygame.transform.scale(RightSpaceShipImage, (spaceShipHeight, spaceShipWidth))



def drawWindow(red, yellow):
    game.fill(white)
    game.blit(LeftSpaceShip, (red.x, red.y))
    game.blit(RightSpaceShip, (yellow.x, yellow.y))
    pygame.display.update()

def redHandleMovement(keysPressed, red):
    if keysPressed[pygame.K_a]:
        #left
        red.x -= veLoCitY
    if keysPressed[pygame.K_d]:
        #Right
        red.x += veLoCitY
    if keysPressed[pygame.K_w]:
        #UP
        red.y -= veLoCitY
    if keysPressed[pygame.K_s]:
        #DOWN
        red.y += veLoCitY   
def YellowHandleMovement(keysPressed, yellow):
    if keysPressed[pygame.K_LEFT]:
        #left
        yellow.x -= veLoCitY
    if keysPressed[pygame.K_RIGHT]:
        #Right
        yellow.x += veLoCitY
    if keysPressed[pygame.K_UP]:
        #UP
        yellow.y -= veLoCitY
    if keysPressed[pygame.K_DOWN]:
        #DOWN
        yellow.y += veLoCitY       

def main():

    red = pygame.Rect(100, 300, spaceShipHeight, spaceShipWidth)
    yellow = pygame.Rect(700, 300, spaceShipHeight, spaceShipWidth)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keysPressed = pygame.key.get_pressed()
        redHandleMovement(keysPressed, red) 
        YellowHandleMovement(keysPressed, yellow)
        drawWindow(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()
