import pygame as p
from corridor.CorridorGame import CorridorEngine

width = heigth = 512
dimension = 17
size = heigth // dimension
max_fps = 15
images = {}


def LoadImages():
    pieces = ["Pl1", "Pl2", "Bl", "Vl", "Gl", "Cross"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (size, size))


def main():
    p.init()
    screen = p.display.set_mode((width, heigth))
    clock = p.time.Clock()
    screen.fill(p.Color('White'))
    gs = CorridorEngine.GameState()
    print(gs.board)
    LoadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawPieces(screen, gs.board)
        clock.tick(max_fps)
        p.display.flip()

def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            screen.blit(images[piece], p.Rect(c * size, r * size, size, size))


if __name__ == "__main__":
    main()
