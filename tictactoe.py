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

def play():
    global carryOn 
    global o
    global grid
    global round
    global mode
    screen.fill(WHITE)
    text = tttFont.render('TIC TAC TOE' , True , LAVENDER)
    screen.blit(text, (100, 40))
    drawGrid()
    carryOn = True # Variable that controls game operation
    o = True # keeps track of character
    grid = ["", "", "", "", "", "", "", "", ""] # Grid will be filled out as spots are taken
    round = 0
    mode = "play"
    
def restart():
    if checkWin():
        if o:
            char = "O"
        else:
            char = "X"
        text = tttFont.render("Congrats " + char, True, LAVENDER)
    else:
        text = tttFont.render("     " + "Draw", True, LAVENDER)
    screen.fill(WHITE)
    screen.blit(text, (110, 150))
    text = tttFont.render("Press space to", True, PINK)
    screen.blit(text, (90, 250))
    text = tttFont.render("play again", True, PINK)
    screen.blit(text, (115, 300))

# Globals
squares = []
coords = []
# setting constants for colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LAVENDER = (165, 153, 224)
PINK = (214, 139, 183)
BLUE = (114, 169, 224)
GREEN = (98, 181, 107)


# game window configuration
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TIC TAC TOE")
# fonts
tttFont = pygame.font.SysFont('helvetica', 40, bold = True)
ansFont = pygame.font.SysFont('helvetica', 100, bold = True)
play()

# Controls updates
clock = pygame.time.Clock()

# Loop continues for game duration
while carryOn and round < 9:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
        elif event.type == pygame.MOUSEBUTTONDOWN:      
            mouse_position = pygame.mouse.get_pos()
            if mode == "play":
                for t in range(9):
                    if squares[t].collidepoint( mouse_position ):
                        if grid[t] == "":
                            if o:
                                grid[t] = "O"
                                screen.blit(ansFont.render(grid[t], True , GREEN), (coords[t][0]+20, coords[t][1]-5))
                            else:
                                grid[t] = "X"
                                screen.blit(ansFont.render(grid[t], True , BLUE), (coords[t][0]+20, coords[t][1]-5))
                            if checkWin():
                                mode = "end"
                                restart()
                            round += 1
                            if round == 9:
                                round = 0
                                mode = "end"
                                restart()
                            o = not o
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and mode == "end":
                play()
    # updates the display
    pygame.display.flip()
     # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()