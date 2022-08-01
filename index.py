import os
import pygame
Width, Height = 900, 500
game = pygame.display.set_mode((Width, Height))
white =(255, 255, 255)
black = (0, 0, 0)
border = pygame.Rect(Width/2 - 5, 0, 10, Height)

FPS = 30
veLoCitY = 15
spaceShipHeight, spaceShipWidth = 55, 40
LeftSpaceShipImage = pygame.image.load(os.path.join("Pics", "left.png"))
LeftSpaceShip = pygame.transform.rotate(pygame.transform.scale(LeftSpaceShipImage, (spaceShipHeight, spaceShipWidth)), 140)
RightSpaceShipImage = pygame.image.load(os.path.join("Pics", "right.png"))
RightSpaceShip = pygame.transform.scale(RightSpaceShipImage, (spaceShipHeight, spaceShipWidth))



def drawWindow(red, yellow):
    game.fill(white)
    pygame.draw.rect(game, black, border)
    game.blit(LeftSpaceShip, (red.x, red.y))
    game.blit(RightSpaceShip, (yellow.x, yellow.y))
    pygame.display.update()

def redHandleMovement(keysPressed, red):
    if keysPressed[pygame.K_a] and red.x - veLoCitY > 0:
        #left
        red.x -= veLoCitY
    if keysPressed[pygame.K_d] and red.x + veLoCitY + red.width < border.x:
        #Right
        red.x += veLoCitY
    if keysPressed[pygame.K_w] and red.y - veLoCitY > 0 :
        #UP
        red.y -= veLoCitY
    if keysPressed[pygame.K_s] and red.y + veLoCitY + red.height < Height:
        #DOWN
        red.y += veLoCitY   
def YellowHandleMovement(keysPressed, yellow):
    if keysPressed[pygame.K_LEFT] and yellow.x - veLoCitY > border.x + border.width:
        #left
        yellow.x -= veLoCitY
    if keysPressed[pygame.K_RIGHT] and yellow.x + veLoCitY + yellow.width < Width:
        #Right
        yellow.x += veLoCitY
    if keysPressed[pygame.K_UP] and yellow.y - veLoCitY > 0 :
        #UP
        yellow.y -= veLoCitY
    if keysPressed[pygame.K_DOWN] and yellow.y + veLoCitY + yellow.height < Height:
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
