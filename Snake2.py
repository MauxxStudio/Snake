
import pygame, sys, random

from pygame.event import clear

pygame.init()

grid = 15,15
dim = 20
banner = 50

width, height = dim*grid[0], dim*grid[1]
size = width, height + banner

screen = pygame.display.set_mode(size)

backColor = (0,180,0)
bannerColor = (32,0,32)
snakeColor = (32,96,0)
foodColor = (128,32,32)
fontColor = (255,200,200)

font = pygame.font.Font(pygame.font.get_default_font(), 30)

directions = [(1,0),(0,1),(-1,0),(0,-1)]
dir = 0

game = True
play = False
pause = True
init = True
score = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if play:
                if event.key == pygame.K_LEFT:
                    dir = (dir - 1) % 4
                elif event.key == pygame.K_RIGHT:
                    dir = (dir + 1) % 4
                elif event.key == pygame.K_SPACE:
                    pause = not pause
            else:
                if event.key == pygame.K_ESCAPE:
                    game = False
                else:
                    play = True

    if play == False:

        snake = [ (int(grid[0]/2)-1,int(grid[1]/2)),(int(grid[0]/2),int(grid[1]/2)),(int(grid[0]/2)+1,int(grid[1]/2)) ]
        snakehead = snake[2]
        food = ()
        score = 0
        time_0 = pygame.time.get_ticks()
        if init:
            init = False
            play = True

    elif pause:
        snakehead = ((snakehead[0]+directions[dir][0]) % grid[0],(snakehead[1]+directions[dir][1]) % grid[1])

        if snake.count(snakehead):
            play = False
        else:
            snake.append(snakehead)
            if snakehead == food:
                score = score + 5
                
                
                food = ()
            else:
                snake.pop(0)
        
        while not food:
            food=(random.randint(0,grid[0]-1),random.randint(0,grid[1]-1))
            if snake.count(food): food = ()

        screen.fill(backColor)
        
        pygame.draw.rect(screen,bannerColor,(0,0,width,banner),width = 0)
        text = pygame.font.Font.render(font, str(((pygame.time.get_ticks()-time_0)//100)/10) ,True,fontColor)
        screen.blit(text,(30,13))
        text = pygame.font.Font.render(font,str(score),True,fontColor)
        screen.blit(text,(width-70,13))
        pygame.draw.rect(screen,foodColor,(food[0]*dim,food[1]*dim+banner,dim,dim),width = 0)

        for cell in snake:
            pygame.draw.rect(screen,snakeColor,(cell[0]*dim,cell[1]*dim+banner,dim,dim),width = 0)
        
        pygame.display.flip()

        pygame.time.wait(120)


pygame.quit()
sys.exit()
    
    
    



