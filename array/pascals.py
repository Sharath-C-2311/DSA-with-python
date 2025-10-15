class Solution:
    def generate(self, numRows: int):
        arr=[[1]]
        if numRows == 1:
            return arr
        elif numRows == 2:
            arr.append([1,1])
            return arr
        for i in range(2,numRows+1):
            f=[1]
            for j in range(len(arr[-1])-1):
                f.append((arr[-1][j]+arr[-1][j+1]))
            f.append(1)
            arr.append(f)
        return arr
    
