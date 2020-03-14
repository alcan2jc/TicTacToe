from graphics import *
import random

win = GraphWin("Tic Tac Toe", 750, 500, autoflush=False)
win.setBackground('black')

# Game Variables
quad_is_taken = [False for i in range(9)]
EMPTY = ' '
O = 'O'
X = 'X'
board_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
board = {board_pos[0]: EMPTY, board_pos[1]: EMPTY, board_pos[2]: EMPTY, board_pos[3]: EMPTY, board_pos[4]: EMPTY,
         board_pos[5]: EMPTY, board_pos[6]: EMPTY, board_pos[7]: EMPTY, board_pos[8]: EMPTY}
moves = 0
tie, first_move = False, False
ai = True
grades = {O: -5, 'tie': 0, X: 5}
ai_result = ''
move = 0


def minimax(game_board, depth, is_max):

    # Terminal Point
    score = evaluate(game_board)
    if score != 'N':
        return grades[score]

    # Maximizing player
    if is_max:
        best_grade = -10000
        for i in range(9):
            if game_board[i] == EMPTY:
                game_board[i] = X
                grade = minimax(game_board, depth + 1, not is_max)
                game_board[i] = EMPTY
                if grade > best_grade:
                    best_grade = grade
        return best_grade

    # Minimizing player
    else:
        best_grade = 10000
        for i in range(9):
            if game_board[i] == EMPTY:
                game_board[i] = O
                grade = minimax(game_board, depth + 1, not is_max)
                game_board[i] = EMPTY
                if grade < best_grade:
                    best_grade = grade
        return best_grade


def evaluate(game_board):
    winner = 'N'
    # check if row win
    if game_board[0] != EMPTY and game_board[0] == game_board[1] and game_board[1] == game_board[2]:  # top row
        winner = game_board[0]

    elif game_board[3] != EMPTY and game_board[3] == game_board[4] and game_board[4] == game_board[5]:  # middle row
        winner = game_board[3]

    elif game_board[6] != EMPTY and game_board[6] == game_board[7] and game_board[7] == game_board[8]:  # bottom row
        winner = game_board[6]

    # check if column win
    elif game_board[0] != EMPTY and game_board[0] == game_board[3] and game_board[3] == game_board[6]:  # left col
        winner = game_board[0]

    elif game_board[1] != EMPTY and game_board[1] == game_board[4] and game_board[4] == game_board[7]:  # middle col
        winner = game_board[1]

    elif game_board[2] != EMPTY and game_board[2] == game_board[5] and game_board[5] == game_board[8]:  # right row
        winner = game_board[2]

    # check if diagonal win left to right
    elif game_board[0] != EMPTY and game_board[0] == game_board[4] and game_board[4] == game_board[8]:
        winner = game_board[0]

    # check if diagonal win right to left
    elif game_board[2] != EMPTY and game_board[2] == game_board[4] and game_board[4] == game_board[6]:
        winner = game_board[2]

    spots = 0
    for i in range(9):
        if game_board[i] == EMPTY:
            spots += 1

    if winner == 'N' and spots == 0:
        return 'tie'
    else:
        return winner


def drawShape(game_board, player1_turn, correct_move, ai):
    global X, EMPTY, first_move
    pos = 0
    pcir = Point(0, 0)
    px1 = Point(0, 0)
    px2 = Point(0, 0)
    px3 = Point(0, 0)
    px4 = Point(0, 0)
    radius = 0.4

    if not ai:
        clickPoint = win.getMouse()
        if clickPoint.getX() < 1 and clickPoint.getY() > 2:
            pos = 0

            pcir.x = 0.5
            pcir.y = 2.5

            px1.x, px1.y = 0.85, 2.15
            px2.x, px2.y = 0.10, 2.85

            px3.x, px3.y = 0.85, 2.85
            px4.x, px4.y = 0.10, 2.15

            if quad_is_taken[0]:
                print("Incorrect move, try again")
                correct_move = False
            quad_is_taken[0] = True
        elif 1 < clickPoint.getX() < 2 < clickPoint.getY():
            pos = 1
            pcir.x = 1.5
            pcir.y = 2.5

            px1.x, px1.y = 1.85, 2.15
            px2.x, px2.y = 1.10, 2.85

            px3.x, px3.y = 1.85, 2.85
            px4.x, px4.y = 1.10, 2.15

            if quad_is_taken[1]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[1] = True
        elif clickPoint.getX() > 2 and clickPoint.getY() > 2:
            pos = 2

            pcir.x = 2.5
            pcir.y = 2.5

            px1.x, px1.y = 2.85, 2.15
            px2.x, px2.y = 2.10, 2.85

            px3.x, px3.y = 2.85, 2.85
            px4.x, px4.y = 2.10, 2.15

            if quad_is_taken[2]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[2] = True
        elif clickPoint.getX() < 1 < clickPoint.getY() < 2:
            pos = 3

            pcir.x = 0.5
            pcir.y = 1.5

            px1.x, px1.y = 0.85, 1.15
            px2.x, px2.y = 0.10, 1.85

            px3.x, px3.y = 0.85, 1.85
            px4.x, px4.y = 0.10, 1.15

            if quad_is_taken[3]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[3] = True
        elif 1 < clickPoint.getX() < 2 and 1 < clickPoint.getY() < 2:
            pos = 4

            pcir.x = 1.5
            pcir.y = 1.5

            px1.x, px1.y = 1.85, 1.15
            px2.x, px2.y = 1.10, 1.85

            px3.x, px3.y = 1.85, 1.85
            px4.x, px4.y = 1.10, 1.15

            if quad_is_taken[4]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[4] = True
        elif clickPoint.getX() > 2 and 1 < clickPoint.getY() < 2:
            pos = 5

            pcir.x = 2.5
            pcir.y = 1.5

            px1.x, px1.y = 2.85, 1.15
            px2.x, px2.y = 2.10, 1.85

            px3.x, px3.y = 2.85, 1.85
            px4.x, px4.y = 2.10, 1.15

            if quad_is_taken[5]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[5] = True
        elif clickPoint.getX() < 1 and clickPoint.getY() < 1:
            pos = 6

            pcir.x = 0.5
            pcir.y = 0.5

            px1.x, px1.y = 0.85, 0.15
            px2.x, px2.y = 0.10, 0.85

            px3.x, px3.y = 0.85, 0.85
            px4.x, px4.y = 0.10, 0.15

            if quad_is_taken[6]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[6] = True
        elif 1 < clickPoint.getX() < 2 and clickPoint.getY() < 1:
            pos = 7

            pcir.x = 1.5
            pcir.y = 0.5

            px1.x, px1.y = 1.85, 0.15
            px2.x, px2.y = 1.10, 0.85

            px3.x, px3.y = 1.85, 0.85
            px4.x, px4.y = 1.10, 0.15

            if quad_is_taken[7]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[7] = True
        elif clickPoint.getX() > 2 and clickPoint.getY() < 1:
            pos = 8

            pcir.x = 2.5
            pcir.y = 0.5

            px1.x, px1.y = 2.85, 0.15
            px2.x, px2.y = 2.10, 0.85

            px3.x, px3.y = 2.85, 0.85
            px4.x, px4.y = 2.10, 0.15

            if quad_is_taken[8]:
                print("Incorrect move, try again")
                correct_move = False

            quad_is_taken[8] = True

        if player1_turn and correct_move:
            circle = Circle(Point(pcir.getX(), pcir.getY()), radius)
            circle.setOutline('white')
            circle.draw(win)
            game_board[pos] = O

        elif not player1_turn and correct_move:
            cross1 = Line(Point(px1.getX(), px1.getY()), Point(px2.getX(), px2.getY()))
            cross2 = Line(Point(px3.getX(), px3.getY()), Point(px4.getX(), px4.getY()))
            cross1.setFill('white')
            cross2.setFill('white')
            cross1.draw(win)
            cross2.draw(win)
            game_board[pos] = X

    if ai:
        move = 0
        played = 0
        for i in range(9):
            if game_board[i] != EMPTY:
                played += 1
        first_move = played < 1
        if first_move:
            pos = random.randint(0, 8)
        else:
            best_grade = -10000
            for i in range(9):
                if game_board[i] == EMPTY:
                    game_board[i] = X
                    grade = minimax(board, 0, False)
                    game_board[i] = EMPTY
                    if grade > best_grade:
                        best_grade = grade
                        move = i
            pos = move

        # Drawing X shapes in
        if pos == 0:

            pcir.x = 0.5
            pcir.y = 2.5

            px1.x, px1.y = 0.85, 2.15
            px2.x, px2.y = 0.10, 2.85

            px3.x, px3.y = 0.85, 2.85
            px4.x, px4.y = 0.10, 2.15

            if quad_is_taken[0]:
                print("invalid move")
                correct_move = False
            quad_is_taken[0] = True
        elif pos == 1:
            pcir.x = 1.5
            pcir.y = 2.5

            px1.x, px1.y = 1.85, 2.15
            px2.x, px2.y = 1.10, 2.85

            px3.x, px3.y = 1.85, 2.85
            px4.x, px4.y = 1.10, 2.15

            if quad_is_taken[1]:
                print("invalid move")
                correct_move = False

            quad_is_taken[1] = True
        elif pos == 2:
            pcir.x = 2.5
            pcir.y = 2.5

            px1.x, px1.y = 2.85, 2.15
            px2.x, px2.y = 2.10, 2.85

            px3.x, px3.y = 2.85, 2.85
            px4.x, px4.y = 2.10, 2.15

            if quad_is_taken[2]:
                correct_move = False

            quad_is_taken[2] = True
        elif pos == 3:
            pcir.x = 0.5
            pcir.y = 1.5

            px1.x, px1.y = 0.85, 1.15
            px2.x, px2.y = 0.10, 1.85

            px3.x, px3.y = 0.85, 1.85
            px4.x, px4.y = 0.10, 1.15

            if quad_is_taken[3]:
                correct_move = False

            quad_is_taken[3] = True
        elif pos == 4:
            pcir.x = 1.5
            pcir.y = 1.5

            px1.x, px1.y = 1.85, 1.15
            px2.x, px2.y = 1.10, 1.85

            px3.x, px3.y = 1.85, 1.85
            px4.x, px4.y = 1.10, 1.15

            if quad_is_taken[4]:
                correct_move = False

            quad_is_taken[4] = True
        elif pos == 5:
            pcir.x = 2.5
            pcir.y = 1.5

            px1.x, px1.y = 2.85, 1.15
            px2.x, px2.y = 2.10, 1.85

            px3.x, px3.y = 2.85, 1.85
            px4.x, px4.y = 2.10, 1.15

            if quad_is_taken[5]:
                correct_move = False

            quad_is_taken[5] = True
        elif pos == 6:
            pcir.x = 0.5
            pcir.y = 0.5

            px1.x, px1.y = 0.85, 0.15
            px2.x, px2.y = 0.10, 0.85

            px3.x, px3.y = 0.85, 0.85
            px4.x, px4.y = 0.10, 0.15

            if quad_is_taken[6]:
                correct_move = False

            quad_is_taken[6] = True
        elif pos == 7:
            pcir.x = 1.5
            pcir.y = 0.5

            px1.x, px1.y = 1.85, 0.15
            px2.x, px2.y = 1.10, 0.85

            px3.x, px3.y = 1.85, 0.85
            px4.x, px4.y = 1.10, 0.15

            if quad_is_taken[7]:
                correct_move = False

            quad_is_taken[7] = True
        elif pos == 8:
            pcir.x = 2.5
            pcir.y = 0.5

            px1.x, px1.y = 2.85, 0.15
            px2.x, px2.y = 2.10, 0.85

            px3.x, px3.y = 2.85, 0.85
            px4.x, px4.y = 2.10, 0.15

            if quad_is_taken[8]:
                correct_move = False

            quad_is_taken[8] = True

        if correct_move:
            cross1 = Line(Point(px1.getX(), px1.getY()), Point(px2.getX(), px2.getY()))
            cross2 = Line(Point(px3.getX(), px3.getY()), Point(px4.getX(), px4.getY()))
            cross1.setFill('white')
            cross2.setFill('white')
            cross1.draw(win)
            cross2.draw(win)
            game_board[pos] = X
    return correct_move


def drawBoard():
    win.setCoords(0, 0, 3, 3)
    line1 = Line(Point(1, 0), Point(1, 3))
    line2 = Line(Point(2, 0), Point(2, 3))
    line3 = Line(Point(3, 0), Point(3, 3))
    line4 = Line(Point(0, 1), Point(3, 1))
    line5 = Line(Point(0, 2), Point(3, 2))
    line6 = Line(Point(0, 3), Point(3, 3))
    line1.setFill('white')
    line2.setFill('white')
    line3.setFill('white')
    line4.setFill('white')
    line5.setFill('white')
    line6.setFill('white')
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)


def draw_winning_circle(pos1, pos2, pos3):
    p_cir1 = Point(0, 0)
    p_cir2 = Point(0, 0)

    # Rows
    if pos1 == 0 and pos2 == 1 and pos3 == 2:  # top row
        p_cir1.x, p_cir1.y = -0.05, 1.95
        p_cir2.x, p_cir2.y = 3.05, 2.99

    elif pos1 == 3 and pos2 == 4 and pos3 == 5:  # middle row
        p_cir1.x, p_cir1.y = -0.05, 0.95
        p_cir2.x, p_cir2.y = 3.05, 2.05

    elif pos1 == 6 and pos2 == 7 and pos3 == 8:  # bottom row
        p_cir1.x, p_cir1.y = -0.05, -0.05
        p_cir2.x, p_cir2.y = 3.05, 1.05

    # Columns
    elif pos1 == 0 and pos2 == 3 and pos3 == 6:  # left column
        p_cir1.x, p_cir1.y = 0, -0.05
        p_cir2.x, p_cir2.y = 1.05, 3.05

    elif pos1 == 1 and pos2 == 4 and pos3 == 7:  # middle column
        p_cir1.x, p_cir1.y = 0.95, -0.05
        p_cir2.x, p_cir2.y = 2.05, 3.05

    elif pos1 == 2 and pos2 == 5 and pos3 == 8:  # right column
        p_cir1.x, p_cir1.y = 1.95, -0.05
        p_cir2.x, p_cir2.y = 3.00, 3.05

    # Diagonal Left to Right
    elif pos1 == 0 and pos2 == 4 and pos3 == 8:  # left column
        diag_cir = Polygon(Point(0.08, 2.1), Point(0.09, 2.9), Point(0.89, 2.9),
                           Point(2.9, 0.9), Point(2.95, 0.08), Point(2.1, 0.09))

        diag_cir.setOutline(color_rgb(51, 255, 51))
        diag_cir.draw(win)

    elif pos1 == 2 and pos2 == 4 and pos3 == 6:  # left column
        diag_cir = Polygon(Point(2.1, 2.91), Point(2.9, 2.90), Point(2.90, 2.1),
                           Point(0.9, 0.09), Point(0.09, 0.1), Point(0.1, 0.9))

        diag_cir.setOutline(color_rgb(51, 255, 51))
        diag_cir.draw(win)

    circle = Oval(Point(p_cir1.getX(), p_cir1.getY()), Point(p_cir2.getX(), p_cir2.getY()))
    circle.setOutline(color_rgb(51, 255, 51))
    circle.draw(win)


def checkWin():
    global tie, moves, board
    # check if row win
    if board[0] != EMPTY and board[0] == board[1] and board[1] == board[2]:  # top row
        pos1, pos2, pos3 = 0, 1, 2
        draw_winning_circle(pos1, pos2, pos3)
        return True

    elif board[3] != EMPTY and board[3] == board[4] and board[4] == board[5]:  # middle row
        pos1, pos2, pos3 = 3, 4, 5
        draw_winning_circle(pos1, pos2, pos3)
        return True

    elif board[6] != EMPTY and board[6] == board[7] and board[7] == board[8]:  # bottom row
        pos1, pos2, pos3 = 6, 7, 8
        draw_winning_circle(pos1, pos2, pos3)
        return True

    # check if column win
    elif board[0] != EMPTY and board[0] == board[3] and board[3] == board[6]:  # left col
        pos1, pos2, pos3 = 0, 3, 6
        draw_winning_circle(pos1, pos2, pos3)
        return True

    elif board[1] != EMPTY and board[1] == board[4] and board[4] == board[7]:  # middle col
        pos1, pos2, pos3 = 1, 4, 7
        draw_winning_circle(pos1, pos2, pos3)
        return True

    elif board[2] != EMPTY and board[2] == board[5] and board[5] == board[8]:  # right row
        pos1, pos2, pos3 = 2, 5, 8
        draw_winning_circle(pos1, pos2, pos3)
        return True

    # check if diagonal win left to right
    elif board[0] != EMPTY and board[0] == board[4] and board[4] == board[8]:
        pos1, pos2, pos3 = 0, 4, 8
        draw_winning_circle(pos1, pos2, pos3)
        return True

    # check if diagonal win right to left
    elif board[2] != EMPTY and board[2] == board[4] and board[4] == board[6]:
        pos1, pos2, pos3 = 2, 4, 6
        draw_winning_circle(pos1, pos2, pos3)
        return True

    # check tie
    if moves == 9:
        tie = True
        return True


def buttons():
    CPU = Rectangle(Point(8, 10), Point(12, 14))  # points are ordered ll, ur
    two_players = Rectangle(Point(8, 2), Point(12, 6))

    CPU.setFill(color_rgb(0, 250, 0))
    two_players.setFill(color_rgb(0, 250, 0))

    CPU.draw(win)
    two_players.draw(win)

    return CPU, two_players


def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


def draw_menu():
    win.setCoords(0, 0, 20, 20)

    # Draw Tic Tac Toe Text
    ttt = Text(Point(10, 18), "Tic Tac Toe")
    ttt.setSize(36)
    ttt.setTextColor('white')
    ttt.setStyle('bold')
    ttt.draw(win)

    # name
    name = Text(Point(10, 16), "By: John Alcantara")
    name.setSize(25)
    name.setTextColor('white')
    name.draw(win)

    # Draw AI button
    cpu = Text(Point(10, 12), 'AI')
    cpu.setSize(20)
    cpu.setTextColor('white')
    cpu.draw(win)

    # Draw
    two_players = Text(Point(10, 4), 'Two Players')
    two_players.setSize(20)
    two_players.setTextColor('white')
    two_players.draw(win)

def clear_board():
    win.setCoords(0, 0, 3, 3)

    rect = Rectangle(Point(0, 0), Point(3, 3))
    rect.setFill('black')
    rect.draw(win)

    drawBoard()


def main():

    # Global Variables
    global board
    global quad_is_taken
    global moves
    global tie
    global ai
    global ai_result

    # Game Variables
    if random.randint(0, 1) == 0:
        player1_turn = True
    else:
        player1_turn = False

    # menu states
    menu = -999
    game_2player = -998
    game_1player = -997

    # Score
    player1 = 0
    player2 = 0

    state = menu

    # Main menu (Not done yet)
    while state == menu:
        CPU, two_players = buttons()
        draw_menu()
        clickPoint = win.getMouse()

        if inside(clickPoint, CPU):
            state = game_1player
        elif inside(clickPoint, two_players):
            state = game_2player

    drawBoard()  # Draws Board


    # Game Loop for 2 Players
    while state == game_2player:

        # initialize variables
        correct_move = True
        if player1_turn:
            print("O's turn")
        else:
            print("X's turn")
        correct_move = drawShape(board, player1_turn, correct_move, False)  # Draws X and O

        if correct_move:
            moves += 1

        # Check if game is over
        game_over = checkWin()

        if game_over:
            if player1_turn and not tie:
                player1 += 1
                print("O Wins \n O: {} \n X: {}".format(player1, player2))
            elif not player1_turn and not tie:
                player2 += 1
                print("X Wins \n O: {} \n X: {}".format(player1, player2))
            elif tie:
                print("Tie! \n O: {} \n X: {}".format(player1, player2))

            # Reset Game if over
            win.getMouse()
            clear_board()
            board = {board_pos[0]: EMPTY, board_pos[1]: EMPTY, board_pos[2]: EMPTY, board_pos[3]: EMPTY,
                     board_pos[4]: EMPTY,
                     board_pos[5]: EMPTY, board_pos[6]: EMPTY, board_pos[7]: EMPTY, board_pos[8]: EMPTY}

            quad_is_taken = [False for i in range(9)]
            if random.randint(0, 1) == 0:
                player1_turn = True
            else:
                player1_turn = False
            moves = 0
            tie = False
            print("\n\n\n\n\n")

        # Prints who's turn it is. Determines who's turn it is and move is valid
        if player1_turn and correct_move:

            player1_turn = False
        elif not player1_turn and correct_move:
            player1_turn = True

    # Game Loop for Playing against AI. (AI will be playing X)
    while state == game_1player:

        # initialize variables
        correct_move = True
        ai = not player1_turn
        correct_move = drawShape(board, player1_turn, correct_move, ai)  # Draws X and O

        if correct_move:
            moves += 1

        # Check if game is over
        game_over = checkWin()

        if game_over:
            if player1_turn and not tie:
                player1 += 1
                print("O Wins \n O: {} \n X: {}".format(player1, player2))
                ai_result = 'lose'
            elif not player1_turn and not tie:
                player2 += 1
                print("X Wins \n O: {} \n X: {}".format(player1, player2))
                ai_result = 'win'
            elif tie:
                print("Tie! \n O: {} \n X: {}".format(player1, player2))
                ai_result = 'tie'

            # Reset Game if over
            win.getMouse()
            clear_board()
            board = {board_pos[0]: EMPTY, board_pos[1]: EMPTY, board_pos[2]: EMPTY, board_pos[3]: EMPTY,
                     board_pos[4]: EMPTY,
                     board_pos[5]: EMPTY, board_pos[6]: EMPTY, board_pos[7]: EMPTY, board_pos[8]: EMPTY}

            quad_is_taken = [False for i in range(9)]
            if random.randint(0, 1) == 0:
                player1_turn = True
            else:
                player1_turn = False
            moves = 0
            tie = False
            ai_result = ''
            print("\n\n\n\n\n")

        # Prints who's turn it is. Determines who's turn it is and move is valid
        if player1_turn and correct_move:
            player1_turn = False
        elif not player1_turn and correct_move:
            player1_turn = True

    win.getMouse()
    win.close()


main()
