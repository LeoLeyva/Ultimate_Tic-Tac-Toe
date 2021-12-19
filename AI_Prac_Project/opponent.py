import numpy as np
import random as rd
from copy import deepcopy
import state as stat
import board as bord


def possible_moves(bd, st):
    ans = []
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    if st.last_coordinates == None:
        for i in range(0, len(alpha)):
            for j in range(0, len(alpha)):
                ans.append((alpha[i], alpha[j]))
        return ans

    (x2, y2) = st.last_coordinates
    (x2, y2) = (bd.alpha_to_num[x2.capitalize()] %
                3, bd.alpha_to_num[y2.capitalize()] % 3)
    next_move = bd.coords_to_board[(y2, x2)]

    if bd.moves_left[next_move] == 0 or bd.board_winners[next_move] != "":
        for i in range(0, len(alpha)):
            for j in range(0, len(alpha)):
                next_move = bd.coords_to_board[(i // 3, j // 3)]
                if bd.moves_left[next_move] == 0 or bd.board_winners[next_move] != "":
                    continue
                if bd.get_tile_symbol(i, j) == " ":
                    ans.append((alpha[j], alpha[i]))
        return ans

    (x2, y2) = (x2*3, y2*3)

    for row in range(y2, y2+3):
        for col in range(x2, x2+3):
            if bd.get_tile_symbol(row, col) == " ":
                ans.append((alpha[col], alpha[row]))

    return ans


def random_ai(bd, st):
    pos = possible_moves(bd, st)
    return pos[rd.randrange(0, len(pos))]
# ------------------------


def is_center(x, y):
    if (x % 3 == 1 and y % 3 == 1):
        return True
    else:
        return False


def is_diagonal(x, y):
    if((x % 3 == 0 and y % 3 == 0) or (x % 3 == 2 and y % 3 == 0) or
       (x % 3 == 0 and y % 3 == 2) or (x % 3 == 2 and y % 3 == 2)):
        return True
    else:
        return False


def win_row(bd):
    bd = np.reshape(bd, (3, 3))
    for r in bd:
        if(len(set(r)) == 1 and ' ' not in r):
            return True
    return False


def win_diag(bd):
    s1 = []
    s2 = []
    for x in range(0, len(bd), 4):
        s1.append(bd[x])
    for y in [2, 4, 6]:
        s2.append(bd[y])

    if(' ' in s1 or ' ' in s2):
        return False

    if(len(set(s1)) == 1 or len(set(s2)) == 1):
        return True
    else:
        return False


def win_col(bd):
    bd = np.reshape(bd, (3, 3))
    for c in np.transpose(bd):
        if(len(set(c)) == 1 and ' ' not in c == 1):
            return True
    return False


def get_small_board(num, bd):
    return bd[num]


def get_board_move(x, y):
    return y + x//3


def greedy_ai(bd, st):
    alpha_to_num = {"A": 0, "B": 1, "C": 2, "D": 3,
                    "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    score = {"center": 10, "diagonal": 7, "other": 5, "win": 100}
    player_to_symbol = {"1": "X", "2": "O"}
    pos = possible_moves(bd, st)
    curr_matrix = deepcopy(bord.Board.get_matrix(bd))
    best_move = ("", "")
    best_score = 0
    ai_symbol = player_to_symbol[stat.State.get_cur_player(st)]
    print(ai_symbol)
    print(pos)
    for move in pos:
        curr_score = 0
        x = alpha_to_num[move[0].capitalize()]
        y = alpha_to_num[move[1].capitalize()]

        n = get_board_move(x, y)
        sm_bd = deepcopy(get_small_board(n, curr_matrix))
        print(sm_bd)
        sm_bd[(x % 3)*3+(y % 3)] = ai_symbol

        print(sm_bd)

        if(win_row(sm_bd) or win_diag(sm_bd) or win_col(sm_bd)):
            curr_score += score["win"]

        if(is_center(x, y)):
            curr_score += score["center"]
        elif(is_diagonal(x, y)):
            curr_score += score["diagonal"]
        else:
            curr_score += score["other"]
        print(move, curr_score)
        if curr_score > best_score:
            best_move = move
            best_score = curr_score
    return best_move


# ------------------------
def montecarlo_ai(real_bd, real_st, depth):

    score = (-depth*2, -depth*2)

    for i in possible_moves(real_bd, real_st):
        points = 0
        for j in range(depth):
            bd = deepcopy(real_bd)
            st = deepcopy(real_st)

            player = st.cur_player

            st.play(i, bd)
            bd.ttt_check(i)

            if bd.victory_check() == player:
                return i

            points += have_fun(player, bd, st)

        if score[0] < points:
            score = points, i
    return score[1]


def have_fun(player, bd, st):
    while bd.victory_check() == "" and not (bd.draw_check()):

        random_move = random_ai(bd, st)
        st.play(random_move, bd)
        bd.ttt_check(random_move)

        # bd.print_board()

    if bd.victory_check() == player:
        return 1
    elif bd.draw_check():
        return 0
    else:
        return -1
