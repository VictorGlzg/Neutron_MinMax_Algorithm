import pygame
from bobail.constants import WIDTH, HEIGHT, SQUARE_SIZE,WHITE, YELLOW
from minimax import bestMove
from bobail.game import Game

pygame.init()

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Neutron + IA')
row = col = 5
print("Blue player's turn")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    test = True

    while run:
        clock.tick(FPS)

        if game.ai_turn is True:
            if test:
                #value, new_board = minimax(game.get_board(), 3, True, game.turn, game)
                new_board = bestMove(game.get_board(), 0, game, WHITE)
                game.board = new_board
                game.ai_move()
                new_board = bestMove(game.get_board(), 0, game, YELLOW)
                game.board = new_board
                game.ai_move()
                game.ai_turn = False
                # print(value)
                # # print(game.ai_turn)
                # print(type(new_board))

        if game.winner() != None:
            print('Hola')
            #run = False
        #
        # if game.winner2() != None:
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

main()