import chessPlayer_tree


def GetPlayerPositions(board, player):
    owned = []
    for i in range(0, len(board)):
        if (player*10-1) < board[i] < (player*10+6):
            owned = owned + [i]
    return owned


def GetPieceLegalMoves(board, position):
    solution = []
    piece = board[position]
    row = position / 8
    col = position % 8

    if piece == 0:
        return []
    if 9 < piece < 16:
        player = 1
        opponent = 2
    if 19 < piece < 26:
        player = 2
        opponent = 1

    if piece == 10:
        potential = [position+8]
        if board[position+8] != 0:
            return []
        if position+8 > 63:
            return []
        if 19 < board[position+7] < 26 and (position+7)/8 != row:
            potential = potential + [position+7]
        if 19 < board[position+9] < 26 and (position+9)/8 != row:
            potential = potential + [position+9]
        return potential

    if piece == 20:
        potential = [position-8]
        if board[position-8] != 0:
            return []
        if position-8 < 0:
            return []
        if 9 < board[position-7] < 16 and (position-7)/8 != row:
            potential = potential + [position-7]
        if 9 < board[position-9] < 16 and (position-9)/8 != row:
            potential = potential + [position-9]
        return potential

    if piece == 11 or piece == 21:
        potential = []

        if position % 8 != 6 and position % 8 != 7:
            potential = potential + [position+17,
                                     position+10, position-6, position-15]
        elif position % 8 != 7:
            potential = potential + [position+17, position-15]

        if position % 8 != 1 and position % 8 != 0:
            potential = potential + [position+15,
                                     position+6, position-10, position-17]
        elif position % 8 != 0:
            potential = potential + [position-17, position+15]

        for i in potential:
            if i < 0 or i > 63:
                x = 1
            elif (player*10-1) < board[i] < (player*10+6):
                x = 1
            else:
                solution = solution + [i]
        return solution

    if piece == 12 or piece == 22:
        potential = []
        for x in [7, 9, -7, -9]:
            for i in range(1, 9):
                temp = position + i*x
                temprow = temp/8
                if temprow == (position + (i-1)*x)/8:
                    break
                if -1 < (position + i*x) < 64:
                    if x == 9 or x == -7:
                        if temp % 8 == 0:
                            break
                    if x == -9 or x == 7:
                        if temp % 8 == 7:
                            break
                    if (player*10-1) < board[position + i*x] < (player*10+6):
                        break

                    if (opponent*10-1) < board[position + i*x] < (opponent*10+6):
                        if (temp % 8 != col and temp/8 != row):
                            potential = potential + [position + i*x]
                            break

                    if (temp % 8 != col and temp/8 != row):
                        potential = potential + [position + i*x]
        solution = potential
        return solution

    if piece == 13 or piece == 23:
        potential = []
        for x in [1, -1, 8, -8]:
            for i in range(1, 9):
                temp = position + i*x
                if -1 < (position + i*x) < 64:
                    if (player*10-1) < board[position + i*x] < (player*10+6):
                        break
                    if (opponent*10-1) < board[position + i*x] < (opponent*10+6):
                        if (temp % 8 == col or temp/8 == row):
                            potential = potential + [position + i*x]
                            break
                    if (temp % 8 == col or temp/8 == row):
                        potential = potential + [position + i*x]
        solution = potential
        return solution

    if piece == 14 or piece == 24:
        potential = []
        for x in [7, 9, -7, -9]:
            for i in range(1, 9):
                temp = position + i*x
                temprow = temp/8
                if temprow == (position + (i-1)*x)/8:
                    break
                if -1 < (position + i*x) < 64:
                    if x == 9 or x == -7:
                        if temp % 8 == 0:
                            break
                    if x == -9 or x == 7:
                        if temp % 8 == 7:
                            break
                    if (player*10-1) < board[position + i*x] < (player*10+6):
                        break
                    if (opponent*10-1) < board[position + i*x] < (opponent*10+6):
                        if (temp % 8 != col and temp/8 != row):
                            potential = potential + [position + i*x]
                            break
                    if (temp % 8 != col and temp/8 != row):
                        potential = potential + [position + i*x]
        solution = potential

        potential = []
        for x in [1, -1, 8, -8]:
            for i in range(1, 9):
                temp = position + i*x
                if -1 < (position + i*x) < 64:

                    if (player*10-1) < board[position + i*x] < (player*10+6):
                        break
                    if (opponent*10-1) < board[position + i*x] < (opponent*10+6):
                        if (temp % 8 == col or temp/8 == row):
                            potential = potential + [position + i*x]
                            break
                    if (temp % 8 == col or temp/8 == row):
                        potential = potential + [position + i*x]
        solution = solution + potential
        return solution

    if piece == 15 or piece == 25:
        potential = []
        for x in [1, -1, 8, -8]:
            if -1 < (position + x) < 64:
                if (player*10-1) < board[position + x] < (player*10+6):
                    i = 0
                elif((position+x) % 8 == col or (position+x)/8 == row):
                    potential = potential + [position + x]
        solution = potential

        potential = []
        for x in [7, 9, -7, -9]:
            if -1 < (position + x) < 64:
                if (player*10-1) < board[position + x] < (player*10+6):
                    i = 0
                elif((position + x) % 8 != col and (position+x)/8 != row):
                    if x == 9 or x == -7:
                        if (position + x) % 8 == 0:
                            break
                    if x == -9 or x == 7:
                        if (position + x) % 8 == 7:
                            break
                    potential = potential + [position + x]
        solution = solution + potential
        return solution


def IsPositionUnderThreat(board, position, player):
    if player == 1:
        opponent = 2
    if player == 2:
        opponent = 1
    # Account for Pawn diagonal capture
    temp = board[position]
    board[position] = (player*10)
    for i in GetPlayerPositions(board, opponent):
        for n in GetPieceLegalMoves(board, i):
            if n == position:
                board[position] = temp
                return True
    board[position] = temp
    return False


def printBoard(board):
    for r in range(0, 8):
        for c in range(0, 8):
            index = r*8+c
            if board[index] == 0:
                print("X  "),
            if board[index] == 10:
                print("wP "),
            if board[index] == 11:
                print("wK "),
            if board[index] == 12:
                print("wB "),
            if board[index] == 13:
                print("wR "),
            if board[index] == 14:
                print("wQ "),
            if board[index] == 15:
                print("wK "),
            if board[index] == 20:
                print("bP "),
            if board[index] == 21:
                print("bK "),
            if board[index] == 22:
                print("bB "),
            if board[index] == 23:
                print("bR "),
            if board[index] == 24:
                print("bQ "),
            if board[index] == 25:
                print("bK "),
        print("")


def chessPlayer(board, player):
    if player != 1 and player != 2:
        return [False, [], [], 0]

    move_tree = chessPlayer_tree.tree([["Moves Tree Root"], 0.0])

    best_rating = minimax(move_tree, 0, 3, player, True, -99999, 99999, board)
    candidateMoves = []
    for i in range(0, len(move_tree.store[1])):
        candidateMoves = candidateMoves + [move_tree.store[1][i].store[0]]

    for i in candidateMoves:
        if i[1] == best_rating:
            movechoice = i[0]
            break

    return [True, movechoice, candidateMoves, move_tree.Get_LevelOrder()]


def minimax(move_node, depth, max_depth, player, isMaxPlayer, alpha, beta, board):
    if depth == max_depth:
        return move_node.store[0][1]

    if player == 1:
        opponent = 2
    if player == 2:
        opponent = 1

    if isMaxPlayer == True:
        maximum = -99999.0

        move_list = genPlayerMoves(board, player)
        testboard = list(board)

        for i in move_list:
            testboard = list(board)
            testboard[i[1]] = testboard[i[0]]
            testboard[i[0]] = 0
            rating = rateBoard(testboard, player)
            move_subnode = chessPlayer_tree.tree([i, rating])
            max_rating = (minimax(move_subnode, depth+1, max_depth,
                                  player, False, alpha, beta, testboard))
            if max_rating > maximum:
                maximum = max_rating
            move_subnode.store[0][1] = max_rating
            move_node.AddSuccessor(move_subnode)
            if maximum > alpha:
                alpha = maximum
            if beta <= alpha:
                break

        return maximum

    if isMaxPlayer == False:
        minimum = 99999.0

        move_list = genPlayerMoves(board, opponent)
        testboard = list(board)

        for i in move_list:
            testboard = list(board)
            testboard[i[1]] = testboard[i[0]]
            testboard[i[0]] = 0
            rating = rateBoard(testboard, player)
            move_subnode = chessPlayer_tree.tree([i, rating])
            min_rating = (minimax(move_subnode, depth+1, max_depth,
                                  player, True, alpha, beta, testboard))
            if min_rating < minimum:
                minimum = min_rating
            move_subnode.store[0][1] = min_rating
            move_node.AddSuccessor(move_subnode)
            if minimum < beta:
                beta = minimum
            if beta <= alpha:
                break

        return minimum


def genPlayerMoves(board, player):
    positions = GetPlayerPositions(board, player)
    moves_list = []
    for pos in positions:
        moves = GetPieceLegalMoves(board, pos)
        for i in moves:
            moves_list = moves_list + [[pos, i]]
    return moves_list


def playerScore(board, player):

    if player == 1:

        pawnbonus = [0,  0,  0,  0,  0,  0,  0,  0,
                     50, 50, 50, 50, 50, 50, 50, 50,
                     10, 10, 20, 30, 30, 20, 10, 10,
                     5,  5, 10, 25, 25, 10,  5,  5,
                     0,  0,  0, 20, 20,  0,  0,  0,
                     5, -5, -10,  0,  0, -10, -5,  5,
                     5, 10, 10, -20, -20, 10, 10,  5,
                     0,  0,  0,  0,  0,  0,  0,  0]

        knightbonus = [-50, -40, -30, -30, -30, -30, -40, -50,
                       -40, -20,  0,  0,  0,  0, -20, -40,
                       -30,  0, 10, 15, 15, 10,  0, -30,
                       -30,  5, 15, 20, 20, 15,  5, -30,
                       -30,  0, 15, 20, 20, 15,  0, -30,
                       -30,  5, 10, 15, 15, 10,  5, -30,
                       -40, -20,  0,  5,  5,  0, -20, -40,
                       -50, -40, -30, -30, -30, -30, -40, -50]

        bishopbonus = [-20, -10, -10, -10, -10, -10, -10, -20,
                       -10,  0,  0,  0,  0,  0,  0, -10,
                       -10,  0,  5, 10, 10,  5,  0, -10,
                       -10,  5,  5, 10, 10,  5,  5, -10,
                       -10,  0, 10, 10, 10, 10,  0, -10,
                       -10, 10, 10, 10, 10, 10, 10, -10,
                       -10,  5,  0,  0,  0,  0,  5, -10,
                       -20, -10, -10, -10, -10, -10, -10, -20]

        rookbonus = [0,  0,  0,  0,  0,  0,  0,  0,
                     5, 10, 10, 10, 10, 10, 10,  5,
                     -5,  0,  0,  0,  0,  0,  0, -5,
                     -5,  0,  0,  0,  0,  0,  0, -5,
                     -5,  0,  0,  0,  0,  0,  0, -5,
                     -5,  0,  0,  0,  0,  0,  0, -5,
                     -5,  0,  0,  0,  0,  0,  0, -5,
                     0,  0,  0,  5,  5,  0,  0,  0]

        queenbonus = [-20, -10, -10, -5, -5, -10, -10, -20,
                      -10,  0,  0,  0,  0,  0,  0, -10,
                      -10,  0,  5,  5,  5,  5,  0, -10,
                      -5,  0,  5,  5,  5,  5,  0, -5,
                      0,  0,  5,  5,  5,  5,  0, -5,
                      -10,  5,  5,  5,  5,  5,  0, -10,
                      -10,  0,  5,  0,  0,  0,  0, -10,
                      -20, -10, -10, -5, -5, -10, -10, -20]

        kingbonus = [-30, -40, -40, -50, -50, -40, -40, -30,
                     -30, -40, -40, -50, -50, -40, -40, -30,
                     -30, -40, -40, -50, -50, -40, -40, -30,
                     -30, -40, -40, -50, -50, -40, -40, -30,
                     -20, -30, -30, -40, -40, -30, -30, -20,
                     -10, -20, -20, -20, -20, -20, -20, -10,
                     20, 20,  0,  0,  0,  0, 20, 20,
                     20, 30, 10,  0,  0, 10, 30, 20]

    if player == 2:

        pawnbonus = [0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, -20, -20, 10, 10, 5, 5, -5, -10, 0, 0, -10, -5, 5, 0, 0, 0, 20, 20, 0, 0,
                     0, 5, 5, 10, 25, 25, 10, 5, 5, 10, 10, 20, 30, 30, 20, 10, 10, 50, 50, 50, 50, 50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0]

        knightbonus = [-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 5, 5, 0, -20, -40, -30, 5, 10, 15, 15, 10, 5, -30, -30, 0, 15, 20, 20, 15,
                       0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 10, 15, 15, 10, 0, -30, -40, -20, 0, 0, 0, 0, -20, -40, -50, -40, -30, -30, -30, -30, -40, -50]

        bishopbonus = [-20, -10, -10, -10, -10, -10, -10, -20, -10, 5, 0, 0, 0, 0, 5, -10, -10, 10, 10, 10, 10, 10, 10, -10, -10, 0, 10, 10, 10, 10,
                       0, -10, -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 5, 10, 10, 5, 0, -10, -10, 0, 0, 0, 0, 0, 0, -10, -20, -10, -10, -10, -10, -10, -10, -20]

        rookbonus = [0, 0, 0, 5, 5, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0,
                     0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, 5, 10, 10, 10, 10, 10, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0]

        queenbonus = [-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 0, 0, 0, 5, 0, -10, -10, 0, 5, 5, 5, 5, 5, -10, -5, 0, 5, 5, 5, 5,
                      0, 0, -5, 0, 5, 5, 5, 5, 0, -5, -10, 0, 5, 5, 5, 5, 0, -10, -10, 0, 0, 0, 0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20]

        kingbonus = [20, 30, 10, 0, 0, 10, 30, 20, 20, 20, 0, 0, 0, 0, 20, 20, -10, -20, -20, -20, -20, -20, -20, -10, -20, -30, -30, -40, -40, -30, -30, -20, -30, -
                     40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30, -30, -40, -40, -50, -50, -40, -40, -30]

    score = 0.0
    for i in range(0, 64):
        if board[i] == player*10:
            score = score + 100 + pawnbonus[i]
        if board[i] == player*10 + 1:
            score = score + 320 + knightbonus[i]
        if board[i] == player*10 + 2:
            score = score + 330 + bishopbonus[i]
        if board[i] == player*10 + 3:
            score = score + 500 + rookbonus[i]
        if board[i] == player*10 + 4:
            score = score + 900 + queenbonus[i]
        if board[i] == player*10 + 5:
            score = score + 30000 + kingbonus[i]
    return score


def rateBoard(board, player):
    if player == 1:
        return playerScore(board, 1) - playerScore(board, 2)
    if player == 2:
        return playerScore(board, 2) - playerScore(board, 1)


def genBoard():
    r = [0]*64
    White = 10
    Black = 20
    for i in [White, Black]:
        if i == White:
            factor = +1
            shift = 0
        else:
            factor = -1
            shift = 63

        r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
        r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
        r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
        if i == White:
            # queen is on its own color square
            r[shift+factor*4] = i+getPiece("queen")
            r[shift+factor*3] = i+getPiece("king")
        else:
            # queen is on its own color square
            r[shift+factor*3] = i+getPiece("queen")
            r[shift+factor*4] = i+getPiece("king")

        for j in range(0, 8):
            r[shift+factor*(j+8)] = i+getPiece("pawn")

    return r


def getPiece(name):
    if name == "pawn":
        return 0
    elif name == "knight":
        return 1
    elif name == "bishop":
        return 2
    elif name == "rook":
        return 3
    elif name == "queen":
        return 4
    elif name == "king":
        return 5
    else:
        return -1


# References

# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

# https://chessprogramming.wikispaces.com/Simplified+evaluation+function
