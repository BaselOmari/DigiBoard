import pygame

IMAGES = {}
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15


def load_images():
    for i in range(2):
        if i == 0:
            c = 'W'
        else:
            c = 'B'
        IMAGES[f'{c}pawn'] = pygame.image.load(f"")
        IMAGES[f'{c}king'] = pygame.image.load(f"C:\Users\romari\Desktop\Basel Code\Chess Piece Images\{c}_King")
        IMAGES[f'{c}queen'] = pygame.image.load(f"C:\Users\romari\Desktop\Basel Code\Chess Piece Images\{c}_Queen")
        IMAGES[f'{c}bishop'] = pygame.image.load(f"C:\Users\romari\Desktop\Basel Code\Chess Piece Images\{c}_Bishop")
        IMAGES[f'{c}knight'] = pygame.image.load(f"C:\Users\romari\Desktop\Basel Code\Chess Piece Images\{c}_Knight")
        IMAGES[f'{c}rook'] = pygame.image.load(f"C:\Users\romari\Desktop\Basel Code\Chess Piece Images\{c}_Rook")

load_images()