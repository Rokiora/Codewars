board1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

def done_or_not(board):
    testset = set([i for i in range(1,10)])  
    for row in board:
            if set(row) != testset:
                print(set(row))
                return 'Try again!1'
    for col in [[row[i] for row in board] for i in range(9)]:
        if set(col) != testset:
            return 'Try again!2'
    for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                    if set(board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]) != testset:
                            return 'Try again!3'
    else:
        return 'Finished!'

print(done_or_not(board1))

# def done_or_not(board):
#   rows = board
#   cols = [map(lambda x: x[i], board) for i in range(9)]
#   squares = [
#     board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
#       for i in range(0, 9, 3)
#       for j in range(0, 9, 3)]

#   for clusters in (rows, cols, squares):
#     for cluster in clusters:
#       if len(set(cluster)) != 9:
#         return 'Try again!'
#   return 'Finished!'
# def done_or_not(baord):
#         testset = set([i for i in range(9)])  
#         for row in board:
#                 if row != testset:
#                         return 'try again'

# for i in range(9):
#         print([row[i] for row in board])
        

                



#         for i in range(0, 9, 3):
#                 for j in range(0, 9, 3):
#                         if board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3] != testset:
#                                 return 'try again'


 
# print(testset)

# y = [[row[i] for row in board] for i in range(9)]

# print(y)

# set coordinate for start
# 0/0
# 3/0
# 6/0
# 0/3
# 3/3
# 6/3....