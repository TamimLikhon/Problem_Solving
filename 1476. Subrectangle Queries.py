class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
       self.rectangle = rectangle
       self.updatelist = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updatelist.append((row1, col1, row2, col2, newValue))


    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, val in reversed(self.updatelist):
            if row >= row1 and col >=  col1 and row <= row2 and col <= col2:
                return(val)
        
        return (self.rectangle[row][col])


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)