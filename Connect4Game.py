try:
    import numpy as np
    import sys, pygame, math
except:
    raise Exception('Numpy and Pygame modules are required.')


# Constant var
SQUARESIZE = 100
ROW_COUNT = 6
COLUMN_COUNT = 7
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 90
RADIUS = 30
xCen = 50
yCen = 150
CENTER = xCen, yCen
ArrowLeftCorner = 35
ArrowRightCorner = 65
ArrowBotCorner = 50
posx = 0




# Screen info
height = SQUARESIZE * (ROW_COUNT + 1)
width = SQUARESIZE * COLUMN_COUNT
Size = width, height
Screen = pygame.display.set_mode(Size)

pygame.display.set_caption('Connect 4')




    
def Create_Board():
    Board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype='int32')
    return Board

def Drop_Piece(Board, row, Column, piece):
    # Recognizes the piece placed in Column is placed
    Board[row][Column] = piece 

def is_Valid_Location(Board, Column):
    # recognizes that the column selected is empty
    return Board[ROW_COUNT - 1][Column] == 0 

def is_Winner(Board, piece):
    # checking for a horizontal win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if Board[r][c] == piece and Board[r][c + 1] == piece and Board[r][c + 2] == piece and Board[r][c + 3]== piece:
                return True

    # checking for a vertical win
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if Board[r][c] == piece and Board[r + 1][c] == piece and Board[r + 2][c] == piece and Board[r + 3][c] == piece:
                return True

    # checking for positive diagonals win
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if Board[r][c] == piece and Board[r + 1][c + 1] == piece and Board[r + 2][c + 2] == piece and Board[r + 3][c +  3] == piece:
                return True

    # checking for negative diagonals win
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if Board[r][c] == piece and Board[r - 1][c + 1] == piece and Board[r - 2][c + 2] == piece and Board[r - 3][c +  3] == piece:
                return True        

def Next_Row(Board, Column):
    # notices when each row is empty 
    for row in range(ROW_COUNT):
        if Board[row][Column] == 0:
            return row

def Print_Board(Board):
    print(np.flip(Board, 0))

def Draw_Board(Board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(Screen, YELLOW, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(Screen, BLACK, (int(c*SQUARESIZE + 50), int(r*SQUARESIZE+SQUARESIZE + 50)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if Board[r][c] == 1:
                pygame.draw.circle(Screen, RED, (c*SQUARESIZE + 50, height - (r*SQUARESIZE + 50)), RADIUS)
            elif Board[r][c] == 2:
                pygame.draw.circle(Screen, BLUE, (c*SQUARESIZE + 50, height - (r*SQUARESIZE + 50)), RADIUS)
    pygame.display.update()
                

            
Board = Create_Board()
Print_Board(Board)
GameOver = False
clock = pygame.time.Clock()
Turn = 0
pygame.display.update()







while not GameOver:
    Screen.fill(BLACK)
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    pygame.mouse.set_visible(False)
    
    for event in events:
        print(event)
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    
    if event.type == pygame.KEYUP:
        pygame.draw.rect(Screen, BLACK, (0,0, width, SQUARESIZE))
        if Turn == 0:
            pygame.draw.polygon(Screen, RED, [(ArrowLeftCorner, 50), (ArrowRightCorner, 50), (ArrowBotCorner, 80)])
        

        elif Turn == 1:
            pygame.draw.polygon(Screen, BLUE, [(ArrowLeftCorner, 50), (ArrowRightCorner, 50), (ArrowBotCorner, 80)])
        
    
    if event.type == pygame.KEYDOWN:
        # Player 1
        if Turn == 0:
            pygame.draw.polygon(Screen, RED, [(ArrowLeftCorner, 50), (ArrowRightCorner, 50), (ArrowBotCorner, 80)])
            # movement 
            if keys[pygame.K_RIGHT] and ArrowLeftCorner < 635:
                ArrowLeftCorner += 100
                ArrowRightCorner += 100
                ArrowBotCorner += 100
                posx += 100
            elif keys[pygame.K_LEFT] and ArrowLeftCorner > 35:
                ArrowLeftCorner -= 100
                ArrowRightCorner -= 100
                ArrowBotCorner -= 100
                posx -= 100
            elif keys[pygame.K_RETURN]:
                pygame.draw.polygon(Screen, RED, [(ArrowLeftCorner, 50), (ArrowRightCorner, 50), (ArrowBotCorner, 80)])
                Column = int(posx / SQUARESIZE)
                if is_Valid_Location(Board, Column): # if it's a valid loc, drop piece
                    row = Next_Row(Board, Column)
                    Drop_Piece(Board, row, Column, 1)
                
                if is_Winner(Board, 1):
                    GameOver = False
                    break                
                
                Turn += 1
                Turn %= 2                       
                
            Print_Board(Board)

            print(Turn)

    
        # Player 2
        elif Turn == 1:
            pygame.draw.polygon(Screen, BLUE, [(ArrowLeftCorner, 50), (ArrowRightCorner, 50), (ArrowBotCorner, 80)])
            # movement 
            if keys[pygame.K_RIGHT] and ArrowLeftCorner < 635:
                ArrowLeftCorner += 100
                ArrowRightCorner += 100
                ArrowBotCorner += 100
                posx += 100
            elif keys[pygame.K_LEFT] and ArrowLeftCorner > 35:
                ArrowLeftCorner -= 100
                ArrowRightCorner -= 100
                ArrowBotCorner -= 100
                posx -= 100
            elif keys[pygame.K_RETURN]:
                pygame.draw.polygon(Screen, BLUE, [(ArrowLeftCorner, 50), (ArrowRightCorner, 50), (ArrowBotCorner, 80)])
                Column = int(posx / SQUARESIZE)
                if is_Valid_Location(Board, Column): # if it's a valid loc, drop piece
                    row = Next_Row(Board, Column)
                    Drop_Piece(Board, row, Column, 2)
                
                if is_Winner(Board, 2):
                    GameOver = False
                    break
                
                Turn += 1
                Turn %= 2
                        

    

            Print_Board(Board)
        
            print(Turn)
    
    
    


    
    Draw_Board(Board)
    pygame.display.update()
    clock.tick(10)