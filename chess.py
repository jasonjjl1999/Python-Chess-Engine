from chessPlayer import *

board = genBoard()

# Move Maker
done = False
while done == False:
    print("The game will now begin")
    printBoard(board)

    while True:
        print(chessPlayer(board, 1))
        printBoard(board)
        white_index = int(input("White: Enter the index of the piece to move "))
        if (board[white_index] > 15 or board[white_index] < 10):
            print("There is no valid white piece at the index")
        else:
            movelist = GetPieceLegalMoves(board, white_index)
            if movelist == []:
                print("No valid moves available for piece")
            else:
                piece_id = board[white_index]
                break

    while True:
        movelist = GetPieceLegalMoves(board, white_index)
        print(movelist)
        white_move = int(input("White: Enter the index to move to "))
        for i in movelist:
            if white_move == i:
                board[white_index] = 0
                board[white_move] = piece_id
                break
        if board[white_index] == 0:
            break
        else:
            print("Invalid move")

    while True:
        print(chessPlayer(board, 2))
        printBoard(board)
        black_index = int(
            input("Black: Enter the index of the piece to move "))
        if (board[black_index] > 25 or board[black_index] < 20):
            print("There is no valid black piece at the index")
        else:
            movelist = GetPieceLegalMoves(board, black_index)
            if movelist == []:
                print("No valid moves available for piece")
            else:
                piece_id = board[black_index]
                break

    while True:
        movelist = GetPieceLegalMoves(board, black_index)
        print(movelist)
        black_move = int(input("Black: Enter the index to move to "))
        for i in movelist:
            if black_move == i:
                board[black_index] = 0
                board[black_move] = piece_id
                break
        if board[black_index] == 0:
            break
        else:
            print("Invalid move")
