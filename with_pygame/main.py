import pygame
from connect_four_logic import *
from time import sleep

pygame.font.init()

WIDTH, HEIGHT = 580, 500
COIN_WIDTH, COIN_HEIGHT = 60, 60
SPLITS = 80
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

offsets = [SPLITS] * 7
old_coins = []
turn = "r"
falling = False
moves = 0
board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]


pygame.display.set_caption("Connect four")

BOARD = pygame.image.load("./images/board.png")
RED_COIN_PICTURE = pygame.image.load("./images/coin-red.png")
BLUE_COIN_PICTURE = pygame.image.load("./images/coin-blue.png")

RED_COIN = pygame.transform.scale(RED_COIN_PICTURE, (COIN_WIDTH, COIN_HEIGHT))
BLUE_COIN = pygame.transform.scale(BLUE_COIN_PICTURE, (COIN_WIDTH, COIN_HEIGHT))


def get_id(x):
    if 0 < x <= 90:
        return 0
    elif 90 < x <= 170:
        return 1
    elif 170 < x <= 250:
        return 2
    elif 250 < x <= 330:
        return 3
    elif 330 < x <= 410:
        return 4
    elif 410 < x <= 490:
        return 5
    elif 490 < x <= 580:
        return 6


def draw_old_coins():
    for i in old_coins:
        if i[2] == "r":
            WIN.blit(RED_COIN, (i[0], i[1] - 5))
        else:
            WIN.blit(BLUE_COIN, (i[0], i[1] - 5))


def draw_coin(x, y, color, offset, col):
    global turn, moves

    if color == "r":
        while y <= HEIGHT - offset:
            WIN.fill((255, 255, 255))
            draw_old_coins()
            WIN.blit(RED_COIN, (x, y))
            draw_board()
            pygame.display.update()
            y += 5
        row = make_move(board, col)
        if row != -1:
            board[row][col] = turn
            moves += 1
            old_coins.append((x, y, color))
        turn = "b"

    else:
        while y <= HEIGHT - offset:
            WIN.fill((255, 255, 255))
            draw_old_coins()
            WIN.blit(BLUE_COIN, (x, y))
            draw_board()
            pygame.display.update()
            y += 5
        row = make_move(board, col)
        if row != -1:
            board[row][col] = turn
            moves += 1
            old_coins.append((x, y, color))
        turn = "r"


def draw_board():
    WIN.blit(BOARD, (0, 0))
    pygame.display.update()


def show_winner(winner):
    if winner != None:
        row, col, start_row, start_col = winner
        winner_char = board[row][col]
    else:
        row, col, start_row, start_col = 0, 0, 0, 0
        winner_char = board[row][col]

    pygame.draw.line(
        WIN,
        (0, 150, 0),
        (50 + start_col * SPLITS, 50 + start_row * SPLITS),
        (50 + col * SPLITS, 50 + row * SPLITS),
        7,
    )
    pygame.display.update()
    sleep(0.8)

    WIN.fill((80, 80, 80))
    font = pygame.font.SysFont(None, 72)
    img = font.render(
        [["Blue", "Red"][winner_char == "r"] + " won!", "It's tie!"][winner == None],
        True,
        (205, 92, 92),
    )
    text_w, text_h = img.get_size()
    WIN.blit(img, ((WIDTH - text_w) / 2, (HEIGHT - text_h) / 2))
    pygame.display.update()
    sleep(1.5)


def main():
    global falling

    WIN.fill((255, 255, 255))
    draw_board()

    clock = pygame.time.Clock()
    run = True
    while run:
        winner = check_winner(board)
        if type(winner) == tuple or moves == 42:
            show_winner(winner)
            break

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, _ = pygame.mouse.get_pos()
                num = get_id(mouse_x)
                draw_coin(20 + num * SPLITS, 20, turn, offsets[num], num)
                offsets[num] += SPLITS

    pygame.quit()


if __name__ == "__main__":
    main()
