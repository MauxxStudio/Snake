
import pygame, sys, time, random

pygame.init()

grid = 15,15
dim = 20

size = width, height = dim*grid[0], dim*grid[1]
screen = pygame.display.set_mode(size)

backColor = (0,180,0)
snakeColor = (32,96,0)
foodColor = (128,32,32)

snake = [ (int(grid[0]/2)-1,int(grid[1]/2)),(int(grid[0]/2),int(grid[1]/2)),(int(grid[0]/2)+1,int(grid[1]/2)) ]
snakehead = snake[2]
directions = [(1,0),(0,1),(-1,0),(0,-1)]
dir = 0
food = ()

game = True
pause = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = (dir - 1) % 4
            elif event.key == pygame.K_RIGHT:
                dir = (dir + 1) % 4
            else: pause = not pause

    snakehead = ((snakehead[0]+directions[dir][0]) % grid[0],(snakehead[1]+directions[dir][1]) % grid[1])

    if snake.count(snakehead):
        game = False
    else:
        snake.append(snakehead)
        if snakehead == food:
            food = ()
        else:
            snake.pop(0)
    
    while not food:
        food=(random.randint(0,grid[0]-1),random.randint(0,grid[1]-1))
        if snake.count(food): food = ()

    time.sleep(0.1)

    screen.fill(backColor)
    
    pygame.draw.rect(screen,foodColor,(food[0]*dim,food[1]*dim,dim,dim),width = 3)
    for cell in snake:
        pygame.draw.rect(screen,snakeColor,(cell[0]*dim,cell[1]*dim,dim,dim),width = 0)
    
    pygame.display.flip()


    
    
    



