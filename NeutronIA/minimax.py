from copy import deepcopy
import pygame

BLUE = (36, 123, 160)
WHITE = (248, 244, 249)
YELLOW = (255, 249, 79)

scores = {YELLOW: 1,
          BLUE: -1}
'''
El problema esta en que al realizar la funcion minmax no devuelve un tablero "position"
'''

def bestMove(position, depth, game):
    bestScore = -1000
    best_move = None
    for move in get_all_moves(position, WHITE, game):
        evaluation = minimax(move, depth, True, WHITE, game)
        score = evaluation[0]
        print("El puntaje fue: "+str(score))
        #score = move.evaluate()
        if score > bestScore:
            bestScore = score
            best_move = move
    return best_move
def minimax(position, depth, max_player, color, game):
    result = game.winner2()
    # if (result != None):
    #     return scores[result], position
    if depth == 2:
        print("Tablero score: "+str(position.evaluate()))
        return position.evaluate(), position
    if max_player == True:
        print('max player: YELLOW')
        if color == WHITE:
            minEval = float('inf')
            best_move = None
            for move in get_all_moves(position, WHITE, game):
                score = minimax(move, depth + 1, True, YELLOW, game)[0]
                print("El puntaje del score es: "+str(score))
                if score < minEval:
                    minEval = score
                    best_move = move
                # minEval = min(minEval, evaluation)
                # if minEval == evaluation:
                #     best_move = move
            return minEval, best_move
        if color == YELLOW:
            minEval = float('inf')
            best_move = None
            for move in get_all_moves(position, YELLOW, game):
                score = minimax(move, depth + 1, False, WHITE, game)[0]
                if score < minEval:
                    minEval = score
                    best_move = move
            return minEval, best_move

    else:
        if color == WHITE:
            print('min player: BLUE')
            maxEval = float('-inf')
            best_move = None
            for move in get_all_moves(position, WHITE, game):
                score = minimax(move, depth + 1, False, BLUE, game)[0]
                if score < maxEval:
                    maxEval = score
                    best_move = move
            return maxEval, best_move
        if color == BLUE:
            maxEval = float('-inf')
            best_move = None
            for move in get_all_moves(position, BLUE, game):
                score = minimax(move, depth + 1, True, WHITE, game)[0]
                if score < maxEval:
                    maxEval = score
                    best_move = move
            return maxEval, best_move


def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.valid_moves(piece)
        for move in valid_moves:
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game)
            moves.append(new_board)
    # Nuevos tableros con cada movimiento
    return moves

def draw_moves(game, board, piece):
    valid_moves = board.valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves)
    pygame.display.update()
    pygame.time.delay(10)

def simulate_move(piece, move, board, game):
    board.move(piece, move[0], move[1])
    return board