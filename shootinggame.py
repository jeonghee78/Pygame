import pygame
import sys
import random
from time import sleep

BLACK =(0, 0, 0)
padWidth = 480 #게임 화면의 가로크기
padHeight =640 #게임 화면의 세로크기
rockImage = ['10.png','11.png','12.png','13.png','14.png','15.png','16.png','17.png',\
             '18.png', '19.png','20.png','21.png','22.png','23.png','24.png','25.png',\
             '25.png','26.png','27.png','28.png','29.png','30.png']

def drawObject(obj, x , y):
    global gamePad
    gamePad.blit(obj, (x,y))

def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    clock = pygame.time.Clock()


def runGame():
    global gamePad, clock , background, fighter, missile, explosion

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    # 전투기 초기 위치 (x,y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    
    missileXY = []
    
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2
    
    isShot = False
    shotCount = 0
    rockPassed = 0
    
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:#게임 프로그램 종료
               pygame.quit()
               sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT: # 전투기 왼쪽으로 이동
                    fighterX -= 5
                elif event.key == pygame.K_RIGHT: # 전투기 오른쪽으로 이동
                    fighterX += 5
                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            if event.type in [pygame.KEYUP]: #방향키를 떼면 전투기 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
            
        
    # 전투기 위치 재조정
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
               
        gamePad.fill(BLACK)
        drawObject(background, 0, 0)
        drawObject(fighter, x, y)
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]
            
                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1
            
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
                
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by) 
        
        rockY += rockSpeed
        
        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
        drawObject(rock, rockX, rockY)
        
        if isShot:
            drawObject(explosion, rockX, rockY)
            
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            isShot = False
        
        drawObject(rock,rockX, rockY)
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    
    

       
     #비행기를 게임 화면의 (x,y) 좌표에 그림

#전투기 움직이기

initGame()
runGame()