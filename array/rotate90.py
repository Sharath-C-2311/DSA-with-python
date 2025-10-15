#code to rotate the matrix by 90 degree

class Solution:
    def rotate(self, matrix):
        l = len(matrix)
        for i in range(l//2):
            matrix[i],matrix[l-i-1] = matrix[l-i-1],matrix[i] #reverse the elements (swap the rows)

        for i in range(l):
            for j in range(i+1,l):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] #take transpose of the matrix
        return matrix
    

