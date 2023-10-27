import pygame
import time
import numpy
import random

def Apple(grid):
    while True:
        randList = random.randint(2,20)
        randItem = random.randint(2,20)
        if grid[randList][randItem] != 1:
            return randList, randItem
            
    

def gameOver(screen):
    pygame.display.set_caption("Game Over")
    SCREEN_SIZE = (440, 440)

    WHITE = (255, 255, 255)

    font = pygame.font.Font(None, 72)
 
    text_surface = font.render("GAME OVER", True, WHITE)
 
    text_rect = text_surface.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
 
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
     
      screen.fill((0, 0, 0))
     
      screen.blit(text_surface, text_rect)

     
      pygame.display.flip()
      time.sleep(2)
      pygame.quit()

def drawGrid(screen, grid):
    #draws the grid
    block=20
    x=0
    y=0
    for i in grid:
        
        x=0      
        for k in i:
            #convert k into int type instead of class numpy int32
            
            if int(k)==1:
                pygame.draw.rect(screen, (50, 50, 200), pygame.Rect(x, y, block, block))
            elif int(k)==2:
                pygame.draw.rect(screen, (200, 50, 50), pygame.Rect(x, y, block, block))
            elif int(k)==5:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, block, block))
                 
            else:
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x, y, block, block))
            
            x+=20
        y+=20   

def move(grid, direction,snake, screen, last):
        
    newItem = numpy.array([1,2])
    
    if direction=="up":
        newItem = [int(snake[0][0])-1, snake[0][1]]
                   
    elif direction=="down":
        newItem = [int(snake[0][0])+1, snake[0][1]]
    
    elif direction=="right":
        newItem = [snake[0][0], int(snake[0][1])+1]
    
    elif direction=="left":
        newItem = [snake[0][0], int(snake[0][1])-1]

    newSnake = numpy.vstack((newItem, snake))    
    #input the newSnake values in grid
    
    if int(grid[newSnake[:, 0], newSnake[:, 1]][0])==0 and int(grid[newSnake[:, 0], newSnake[:, 1]][0])!= 5:
        grid[newSnake[:, 0], newSnake[:, 1]] = 1
    elif int(grid[newSnake[:, 0], newSnake[:, 1]][0])==2:
        snakeTail = numpy.insert(newSnake, -1, last, axis=0)
        newSnake = snakeTail
    else:
        gameOver(screen)
    
    row, line = last
    grid[row][line] = 0
    
    containsValue = numpy.any(grid == 2)
    if containsValue == False:
        randRow, randItem = Apple(grid)
        grid[randRow][randItem] = 2
            
            
    drawGrid(screen, grid)

    return newSnake
    
        
        
          
 
def main():
    #grid from 0 - empty , 1 - snake, 2, apple, 5 - edge
    oneLine = [0 for i in range(22) ]
    grid = numpy.array([oneLine for j in range(22)])
    
    #edges in grid
    for i in grid:
        i[0]=5
        i[-1]=5
        
    for j in range(len(grid[0])):
        grid[0][j]=5
        grid[-1][j]=5
         
    
    
    pygame.init()

    width = 440
    length = 440
    screen = pygame.display.set_mode((width, length))
    
    screen.fill((0,0,0))
    
    Direction = "up" 
    snake = numpy.array([ [14,10], [15, 10], [16, 10], [17,10]])
    
    

    while True:
        
        time.sleep(0.07)
        last = snake[-1]
        snake = snake[:-1]
        snake = move(grid, Direction,snake, screen, last)
        
        for event in pygame.event.get():
            time.sleep(0.05)
            
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
            #basic functionality - give it some movement
            elif event.type == pygame.KEYDOWN:
                #always move
                
                if event.key == pygame.K_UP and Direction!="down":
                    Direction = "up"
                elif event.key == pygame.K_DOWN and Direction!="up":
                    Direction = "down"
                elif event.key == pygame.K_LEFT and Direction!="right":
                    Direction = "left"
                elif event.key == pygame.K_RIGHT and Direction!="left":
                    Direction = "right"
                

        pygame.display.update()
        

    

main()