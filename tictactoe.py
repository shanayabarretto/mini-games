# initialization for pygame
import pygame
pygame.init()

# Functions
# Draws the grid
def drawGrid():
    xstart, ystart, length = 50, 125, 100
    for x in range(3):
        for y in range(3):
            sq = pygame.Rect(xstart+length*(x), ystart+length*(y), length, length)
            squares.append(sq)
            coords.append([xstart+length*(x),ystart+length*(y)])
            pygame.draw.rect(screen, BLACK, squares[x*3+y], 1)

# checks if the game has been won
def checkWin():
    check = False
    for i in range(0, 9, 3):
        if grid[i] == grid[i+1] and grid[i+1] == grid[i+2] and grid[i+2] != "":
            check = True
    for j in range(3):
        if grid[j] == grid[j+3] and grid[j+3] == grid[j+6] and grid[j+6] != "":
            check = True
    if grid[0] == grid[4] and grid[4] == grid[8] and grid[8] != "":
            check = True
    if grid[2] == grid[4] and grid[4] == grid[6] and grid[6] != "":
            check = True
    return check

# Globals
squares = []
coords = []
endsq = pygame.Rect(50, 225, 300, 100)

# setting constants for colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# game window configuration
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TIC TAC TOE")
tttFont = pygame.font.SysFont('helvetica', 40, bold = True)
ansFont = pygame.font.SysFont('helvetica', 100, bold = True)

screen.fill(WHITE)
text = tttFont.render('TICTACTOE' , True , BLACK)
screen.blit(text, (110, 40))
drawGrid()
# Variable that controls game operation
carryOn = True
# keeps track of character
o = True
# Grid will be filled out as spots are taken
grid = ["", "", "", "", "", "", "", "", ""]
round = 0
play = True

# Controls updates
clock = pygame.time.Clock()

# Loop continues for game duration
while carryOn and round < 9:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            if play:
                for t in range(9):
                    if squares[t].collidepoint( mouse_position ):
                        if grid[t] == "":
                            if o:
                                grid[t] = "O"
                            else:
                                grid[t] = "X"
                            screen.blit(ansFont.render(grid[t], True , BLACK), (coords[t][0]+20, coords[t][1]-5))
                            if checkWin():
                                carryOn = False
                            round += 1
                            o = not o 

    # updates the display
    pygame.display.flip()
     # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()