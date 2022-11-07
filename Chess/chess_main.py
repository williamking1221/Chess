"""
Main driver.
"""

import pygame as p
from Chess import chess_engine

p.init()

WIDTH = HEIGHT = 512
DIMS = 8
SQ_SIZE = HEIGHT // DIMS
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = chess_engine.GameState()
    load_images()
    running = True
    sq_selected = () # No square selected initially, track last square selected by user.
    player_clicks = []  # Keep track of player clicks -- made of two tuples
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()    # Location of the mouse (x,y) coords
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, col):   # User clicked same square twice
                    sq_selected = ()    # Reset square selected
                    player_clicks = []  # Clear player clicks
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)   # Add first and second clicks
                if len(player_clicks) == 2:             # If this is the second click, make move if possible
                    move = chess_engine.Move(player_clicks[0], player_clicks[1], game_state.board)
                    print(move.get_chess_not())
                    game_state.make_move(move)
                    sq_selected = ()                    # Reset play clicks
                    player_clicks = []

        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, game_state):
    draw_board(screen)      # Draw the board
    draw_pieces(screen, game_state.board)


"""
Draw the squares on board
"""
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMS):
        for col in range(DIMS):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the pieces on the board via the current game_state board
"""
def draw_pieces(screen, board):
    for row in range(DIMS):
        for col in range(DIMS):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()