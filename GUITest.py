import pygame
import Data Organization

IMAGES = {}
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15

board = 

def load_images():
    for i in range(2):
        if i == 0:
            c = 'W'
        else:
            c = 'B'
        IMAGES[f'{c}pawn'] = pygame.transform.scale(pygame.image.load(f"Chess Piece Images\\{c}_Pawn.png"), (SQ_SIZE,SQ_SIZE))
        IMAGES[f'{c}king'] = pygame.transform.scale(pygame.image.load(f"Chess Piece Images\\{c}_King.png"), (SQ_SIZE, SQ_SIZE))
        IMAGES[f'{c}queen'] = pygame.transform.scale(pygame.image.load(f"Chess Piece Images\\{c}_Queen.png"), (SQ_SIZE, SQ_SIZE))
        IMAGES[f'{c}knight'] = pygame.transform.scale(pygame.image.load(f"Chess Piece Images\\{c}_Knight.png"), (SQ_SIZE, SQ_SIZE))
        IMAGES[f'{c}bishop'] = pygame.transform.scale(pygame.image.load(f"Chess Piece Images\\{c}_Bishop.png"), (SQ_SIZE, SQ_SIZE))
        IMAGES[f'{c}rook'] = pygame.transform.scale(pygame.image.load(f"Chess Piece Images\\{c}_Rook.png"), (SQ_SIZE, SQ_SIZE))

def start_up():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("White"))
    load_images()

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        

        drawGameState(screen, board)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colours = [pygame.Color("white"),pygame.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour = colours[((r + c) % 2)]
            pygame.draw.rect(screen, colour, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
            

def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != 0:
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
