class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        #this is not the efficient method as it uses more space but very fast
        rowinarr=[]
        colinarr=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowinarr.append(i)
                    colinarr.append(j)
        
        for i in range(len(rowinarr)):
            matrix[rowinarr[i]] = [0]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(colinarr)):
                matrix[i][colinarr[j]] = 0

        return matrix