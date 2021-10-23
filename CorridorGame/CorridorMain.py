import pygame as p
from corridor.CorridorGame import CorridorEngine

width = heigth = 500
dimension = 18
size = heigth // dimension
max_fps = 15
images = {}


def LoadImages():
    pieces = ["pl1", "pl2"]
    for piece in pieces:
        images["pieces"] = p.transform.scale(p.image.load("images/pawn.png"), (size, size))


def main():
    p.init()
    screen = p.display.set_mode((width, heigth))
    clock = p.time.Clock()
    screen.fill(p.Color('White'))
    gs = CorridorEngine.GameState()
    LoadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(max_fps)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color('White'), p.Color('gray')]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * size, r * size, size, size))


def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "." and piece != '|':
                screen.blit(images[piece], p.Rect(c * size, r * size, size, size))


if __name__ == "__main__":
    main()
