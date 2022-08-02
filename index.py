import os
import pygame
Width, Height = 900, 500
game = pygame.display.set_mode((Width, Height))
white =(255, 255, 255)
RED =(255, 0, 0)
YELLOW = (255, 255, 0)
black = (0, 0, 0)
border = pygame.Rect(Width//2 - 5, 0, 10, Height)

FPS = 30
veLoCitY = 15
bulletVelcoity = 10

yellowHit = pygame.USEREVENT + 1
redHit = pygame.USEREVENT + 2
MaXBullets = 3

spaceShipHeight, spaceShipWidth = 55, 40
spaceBackGroung = pygame.transform.scale(pygame.image.load(os.path.join('Pics', 'left.png')), (Width, Height))
LeftSpaceShipImage = pygame.image.load(os.path.join("Pics", "left.png"))
LeftSpaceShip = pygame.transform.rotate(pygame.transform.scale(LeftSpaceShipImage, (spaceShipHeight, spaceShipWidth)), 140)
RightSpaceShipImage = pygame.image.load(os.path.join("Pics", "right.png"))
RightSpaceShip = pygame.transform.scale(RightSpaceShipImage, (spaceShipHeight, spaceShipWidth))



def drawWindow(red, yellow, RedBullets, YellowBulllets):
    game.fill(white)
    game.blit(spaceBackGroung, (0, 0))
    pygame.draw.rect(game, black, border)
    game.blit(LeftSpaceShip, (red.x, red.y))
    game.blit(RightSpaceShip, (yellow.x, yellow.y))

    for bullet in RedBullets:
        pygame.draw.rect(game, RED, bullet)
    
    for bullet in YellowBulllets:
        pygame.draw.rect(game, YELLOW, bullet)
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

def handleBullets(yellowBullets, redBullets, yellow, red):
    for bullets in redBullets:
        bullets.x += bulletVelcoity
        if red.colliderect(bullets):
            pygame.event.post(pygame.event.Event(redHit))
            redBullets.remove(bullets)
        elif bullets.x > Width:
            redBullets.remove(bullets)

    for bullets in yellowBullets:
        bullets.x -= bulletVelcoity
        if yellow.colliderect(bullets):
            pygame.event.post(pygame.event.Event(yellowHit))
            yellowBullets.remove(bullets)
        elif bullets.x < 0:
            yellowBullets.remove(bullets)

def main():
    red = pygame.Rect(100, 300, spaceShipHeight, spaceShipWidth)
    yellow = pygame.Rect(700, 300, spaceShipHeight, spaceShipWidth)
    RedBullet = []
    YellowBullet = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(RedBullet) < MaXBullets:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 - 2, 10, 5)
                    RedBullet.append(bullet)
                if event.key == pygame.K_RCTRL and len(YellowBullet) < MaXBullets: 
                    bullet = pygame.Rect(yellow.x, yellow.y + yellow.height//2 - 2, 10, 5)
                    YellowBullet.append(bullet)
        
        keysPressed = pygame.key.get_pressed()
        redHandleMovement(keysPressed, red) 
        YellowHandleMovement(keysPressed, yellow)
        
        handleBullets(YellowBullet, RedBullet, yellow, red)
        drawWindow(red, yellow, RedBullet, YellowBullet)
    pygame.quit()

if __name__ == "__main__":
    main()
