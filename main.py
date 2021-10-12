import pygame
from pygame.locals import *
import numpy
import sys
import math

# Y THEN X

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 800, 800
square_num = 8
square_size = width / square_num
screen = pygame.display.set_mode((width, height))


class pawn:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col

        self.isWhite = isWhite

    def get_moves(self, board_class):
        possible_moves = []

        board = board_class.board
        turn = board_class.turn

        color_mod = 0
        if self.isWhite == False:
            color_mod = 1

        color_mult = -1
        if self.isWhite == False:
            color_mult = 1

        if self.row != 0:
            if board[self.row + (1 * color_mult), self.col] == 0:
                possible_moves.append((self.col, self.row + (1 * color_mult)))

        if self.col != 7:
            if board[self.row + (1 * color_mult), self.col + 1] % 2 != color_mod and board[
                self.row + (1 * color_mult), self.col + 1] != 0:
                possible_moves.append((self.col + 1, self.row + (1 * color_mult)))

        if self.col != 0:
            if board[self.row + (1 * color_mult), self.col - 1] % 2 != color_mod and board[
                self.row + (1 * color_mult), self.col - 1] != 0:
                possible_moves.append((self.col - 1, self.row + (1 * color_mult)))

        if turn < 2:
            if  board[self.row + (2 * color_mult), self.col] == 0:
                possible_moves.append((self.col, self.row + (2 * color_mult)))

        return possible_moves

    def can_move(self, row, col, board):
        if (col, row) in self.get_moves(board):
            return True
        return False

    def render(self, screen, board):
        possible_moves = self.get_moves(board)
        for pos in range(len(possible_moves)):
            pygame.draw.circle(
                screen, (100, 255, 100),
                (
                    possible_moves[pos][0] * square_size + square_size / 2,
                    possible_moves[pos][1] * square_size + square_size / 2,
                ),
                square_size / 4,
            )


class rook:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col

        self.isWhite = isWhite

    def get_moves(self, board_class):
        possible_moves = []

        board = board_class.board

        color_mod = 0
        if self.isWhite == False:
            color_mod = 1

        checking_right = True
        for pos in range(self.col + 1, 8):
            if checking_right:
                if board[self.row, pos] == 0:
                    possible_moves.append((pos, self.row))
                elif board[self.row, pos] % 2 != color_mod:
                    possible_moves.append((pos, self.row))
                    checking_right = False
                else:
                    checking_right = False

        checking_left = True
        for pos in range(self.col - 1, -1, -1):
            if checking_left:
                if board[self.row, pos] == 0:
                    possible_moves.append((pos, self.row))
                elif board[self.row, pos] % 2 != color_mod:
                    possible_moves.append((pos, self.row))
                    checking_left = False
                else:
                    checking_left = False

        checking_down = True
        for pos in range(self.row + 1, 8):
            if checking_down:
                if board[pos, self.col] == 0:
                    possible_moves.append((self.col, pos))
                elif board[pos, self.col] % 2 != color_mod:
                    possible_moves.append((self.col, pos))
                    checking_down = False
                else:
                    checking_down = False

        checking_up = True
        for pos in range(self.row - 1, -1, -1):
            if checking_up:
                if board[pos, self.col] == 0:
                    possible_moves.append((self.col, pos))
                elif board[pos, self.col] % 2 != color_mod:
                    possible_moves.append((self.col, pos))
                    checking_up = False
                else:
                    checking_up = False

        return possible_moves

    def can_move(self, row, col, board):
        if (col, row) in self.get_moves(board):
            return True
        return False

    def render(self, screen, board):
        possible_moves = self.get_moves(board)
        for pos in range(len(possible_moves)):
            pygame.draw.circle(
                screen, (100, 255, 100),
                (
                    possible_moves[pos][0] * square_size + square_size / 2,
                    possible_moves[pos][1] * square_size + square_size / 2,
                ),
                square_size / 4,
            )


class queen:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col

        self.isWhite = isWhite

    def get_moves(self, board_class):
        possible_moves = []

        board = board_class.board

        color_mod = 0
        if self.isWhite == False:
            color_mod = 1

        checking_right = True
        for pos in range(self.col + 1, 8):
            if checking_right:
                if board[self.row, pos] == 0:
                    possible_moves.append((pos, self.row))
                elif board[self.row, pos] % 2 != color_mod:
                    possible_moves.append((pos, self.row))
                    checking_right = False
                else:
                    checking_right = False

        checking_left = True
        for pos in range(self.col - 1, -1, -1):
            if checking_left:
                if board[self.row, pos] == 0:
                    possible_moves.append((pos, self.row))
                elif board[self.row, pos] % 2 != color_mod:
                    possible_moves.append((pos, self.row))
                    checking_left = False
                else:
                    checking_left = False

        checking_down = True
        for pos in range(self.row + 1, 8):
            if checking_down:
                if board[pos, self.col] == 0:
                    possible_moves.append((self.col, pos))
                elif board[pos, self.col] % 2 != color_mod:
                    possible_moves.append((self.col, pos))
                    checking_down = False
                else:
                    checking_down = False

        checking_up = True
        for pos in range(self.row - 1, -1, -1):
            if checking_up:
                if board[pos, self.col] == 0:
                    possible_moves.append((self.col, pos))
                elif board[pos, self.col] % 2 != color_mod:
                    possible_moves.append((self.col, pos))
                    checking_up = False
                else:
                    checking_up = False

        right = self.col + 1
        checking_up = True
        up = self.row - 1
        checking_down = True
        down = self.row + 1
        while right < 8:
            if up > -1 and checking_up:
                if board[up, right] == 0:
                    possible_moves.append((right, up))
                    up -= 1
                elif board[up, right] != color_mod:
                    possible_moves.append((right, up))
                    checking_up = False
                else:
                    checking_up = False

            if down < 7 and checking_down:
                if board[down, right] == 0:
                    possible_moves.append((right, down))
                    down += 1
                elif board[down, right] != color_mod:
                    possible_moves.append((right, down))
                    checking_down = False
                else:
                    checking_down = False
            right += 1

        left = self.col - 1
        checking_up = True
        up = self.row - 1
        checking_down = True
        down = self.row + 1
        while left > -1:
            if up > -1 and checking_up:
                if board[up, left] == 0:
                    possible_moves.append((left, up))
                    up -= 1
                elif board[up, left] != color_mod:
                    possible_moves.append((left, up))
                    checking_up = False
                else:
                    checking_up = False

            if down < 7 and checking_down:
                if board[down, left] == 0:
                    possible_moves.append((left, down))
                    down += 1
                elif board[down, left] != color_mod:
                    possible_moves.append((left, down))
                    checking_down = False
                else:
                    checking_down = False
            left -= 1

        return possible_moves

    def can_move(self, row, col, board):
        if (col, row) in self.get_moves(board):
            return True
        return False

    def render(self, screen, board):
        possible_moves = self.get_moves(board)
        for pos in range(len(possible_moves)):
            pygame.draw.circle(
                screen, (100, 255, 100),
                (
                    possible_moves[pos][0] * square_size + square_size / 2,
                    possible_moves[pos][1] * square_size + square_size / 2,
                ),
                square_size / 4,
            )


class bishop:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col

        self.isWhite = isWhite

    def get_moves(self, board_class):
        possible_moves = []

        board = board_class.board

        color_mod = 0
        if self.isWhite == False:
            color_mod = 1

        right = self.col + 1
        checking_up = True
        up = self.row - 1
        checking_down = True
        down = self.row + 1
        while right < 8:
            if up > -1 and checking_up:
                if board[up, right] == 0:
                    possible_moves.append((right, up))
                    up -= 1
                elif board[up, right] != color_mod:
                    possible_moves.append((right, up))
                    checking_up = False
                else:
                    checking_up = False

            if down < 8 and checking_down:
                if board[down, right] == 0:
                    possible_moves.append((right, down))
                    down += 1
                elif board[down, right] != color_mod:
                    possible_moves.append((right, down))
                    checking_down = False
                else:
                    checking_down = False
            right += 1

        left = self.col - 1
        checking_up = True
        up = self.row - 1
        checking_down = True
        down = self.row + 1
        while left > -1:
            if up > -1 and checking_up:
                if board[up, left] == 0:
                    possible_moves.append((left, up))
                    up -= 1
                elif board[up, left] != color_mod:
                    possible_moves.append((left, up))
                    checking_up = False
                else:
                    checking_up = False

            if down < 7 and checking_down:
                if board[down, left] == 0:
                    possible_moves.append((left, down))
                    down += 1
                elif board[down, left] != color_mod:
                    possible_moves.append((left, down))
                    checking_down = False
                else:
                    checking_down = False
            left -= 1

        return possible_moves

    def can_move(self, row, col, board):
        if (col, row) in self.get_moves(board):
            return True
        return False

    def render(self, screen, board):
        possible_moves = self.get_moves(board)
        for pos in range(len(possible_moves)):
            pygame.draw.circle(
                screen, (100, 255, 100),
                (
                    possible_moves[pos][0] * square_size + square_size / 2,
                    possible_moves[pos][1] * square_size + square_size / 2,
                ),
                square_size / 4,
            )


class knight:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col

        self.isWhite = isWhite

    def get_moves(self, board_class):
        possible_moves = []

        board = board_class.board

        color_mod = 0
        if self.isWhite == False:
            color_mod = 1

        moves_to_try = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in moves_to_try:
            if -1 < self.col + move[0] < 8 and -1 < self.row + move[1] < 8:
                if board[self.row + move[1], self.col + move[0]] % 2 != color_mod or board[
                    self.row + move[1], self.col + move[0]] == 0:
                    possible_moves.append((self.col + move[0], self.row + move[1]))

        return possible_moves

    def can_move(self, row, col, board):
        if (col, row) in self.get_moves(board):
            return True
        return False

    def render(self, screen, board):
        possible_moves = self.get_moves(board)
        for pos in range(len(possible_moves)):
            pygame.draw.circle(
                screen, (100, 255, 100),
                (
                    possible_moves[pos][0] * square_size + square_size / 2,
                    possible_moves[pos][1] * square_size + square_size / 2,
                ),
                square_size / 4,
            )


class king:
    def __init__(self, row, col, isWhite):
        self.row = row
        self.col = col

        self.isWhite = isWhite

    def get_moves(self, board_class):
        possible_moves = []

        board = board_class.board

        color_mod = 0
        if self.isWhite == False:
            color_mod = 1

        moves_to_try = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        for move in moves_to_try:
            if -1 < self.col + move[0] < 8 and -1 < self.row + move[1] < 8:
                if board[self.row + move[1], self.col + move[0]] % 2 != color_mod or board[
                    self.row + move[1], self.col + move[0]] == 0:
                    possible_moves.append((self.col + move[0], self.row + move[1]))

        return possible_moves

    def can_move(self, row, col, board):
        if (col, row) in self.get_moves(board):
            return True
        return False

    def render(self, screen, board):
        possible_moves = self.get_moves(board)
        for pos in range(len(possible_moves)):
            pygame.draw.circle(
                screen, (100, 255, 100),
                (
                    possible_moves[pos][0] * square_size + square_size / 2,
                    possible_moves[pos][1] * square_size + square_size / 2,
                ),
                square_size / 4,
            )


class chessboard:
    def __init__(self):
        self.board = numpy.zeros((8, 8))
        self.white = (121, 71, 56)
        self.black = (93, 50, 49)

        self.turn = 0

        for x in range(0, 8):
            # Black Pawns
            self.board[1, x] = 1
            # White Pawns
            self.board[6, x] = 2

        # Black Rooks
        self.board[0, 0] = 3
        self.board[0, 7] = 3

        # White Rooks
        self.board[7, 0] = 4
        self.board[7, 7] = 4

        # Black Knights
        self.board[0, 1] = 5
        self.board[0, 6] = 5

        # White Knights
        self.board[7, 1] = 6
        self.board[7, 6] = 6

        # Black Bishops
        self.board[0, 2] = 7
        self.board[0, 5] = 7

        # White Bishops
        self.board[7, 2] = 8
        self.board[7, 5] = 8

        # Black Queen
        self.board[0, 3] = 9

        # White Queen
        self.board[7, 3] = 10

        # # Black King
        self.board[0, 4] = 11

        # White King
        self.board[7, 4] = 12

    def move(self, piece_pos, new_pos):
        piece_num = self.board[piece_pos[0], piece_pos[1]]
        self.board[piece_pos[0], piece_pos[1]] = 0
        self.board[new_pos[0], new_pos[1]] = piece_num
        self.turn += 1

    def render(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                color = self.black
                if row % 2 + col % 2 != 1:
                    color = self.white

                pygame.draw.rect(screen, color, Rect(
                    col * square_size,
                    row * square_size,
                    square_size,
                    square_size
                ))

                if self.board[row, col] != 0:
                    sprite = pygame.image.load(r'assets/pieces/' + str(int(self.board[row, col])) + '.png')
                    piece_size = square_size * 0.8
                    buffer_size = square_size * 0.2
                    sprite = pygame.transform.scale(sprite, (int(piece_size), int(piece_size)))
                    screen.blit(sprite, (col * square_size + buffer_size/2, row * square_size + buffer_size/2))


board = chessboard()
selected_piece = None
# 0 - 255(white)
# Game loop.
while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = int((pos[0] - (pos[0] % square_size)) / square_size)
            row = int((pos[1] - (pos[1] % square_size)) / square_size)
            clicked = board.board[row, col]
            if selected_piece == None:
                if clicked == 0:
                    selected_piece = None
                if clicked == 1 and board.turn % 2 == 1:
                    selected_piece = pawn(row, col, False)
                if clicked == 2 and board.turn % 2 == 0:
                    selected_piece = pawn(row, col, True)
                if clicked == 3 and board.turn % 2 == 1:
                    selected_piece = rook(row, col, False)
                if clicked == 4 and board.turn % 2 == 0:
                    selected_piece = rook(row, col, True)
                if clicked == 5 and board.turn % 2 == 1:
                    selected_piece = knight(row, col, False)
                if clicked == 6 and board.turn % 2 == 0:
                    selected_piece = knight(row, col, True)
                if clicked == 7 and board.turn % 2 == 1:
                    selected_piece = bishop(row, col, False)
                if clicked == 8 and board.turn % 2 == 0:
                    selected_piece = bishop(row, col, True)
                if clicked == 9 and board.turn % 2 == 1:
                    selected_piece = queen(row, col, False)
                if clicked == 10 and board.turn % 2 == 0:
                    selected_piece = queen(row, col, True)
                if clicked == 11 and board.turn % 2 == 1:
                    selected_piece = king(row, col, False)
                if clicked == 12 and board.turn % 2 == 0:
                    selected_piece = king(row, col, True)
            else:
                if selected_piece.can_move(row, col, board):
                    board.move((selected_piece.row, selected_piece.col), (row, col))
                    selected_piece = None
                else:
                    selected_piece = None

    # Update.
    board.render(screen)
    if selected_piece != None:
        selected_piece.render(screen, board)

    # Draw.

    pygame.display.flip()
    fpsClock.tick(fps)
