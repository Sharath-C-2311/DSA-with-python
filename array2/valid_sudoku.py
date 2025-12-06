class Solution:
    def isValidSudoku(self, board):
        

        row=[set() for _ in range(9)]
        column=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):

                num=board[i][j]
                box_i = (i//3)*3+(j//3)

                if num!=".":
        
                    if num in row[i] or num in column[j] or num in box[box_i]:
                        return False

                    row[i].add(num)
                    column[j].add(num)
                    box[box_i].add(num)

        return True