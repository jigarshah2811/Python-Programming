from re import X
from typing import List
import collections

# class Point:
#     def __init__(self, row, col) -> None:
#         self.row = row
#         self.col = col

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.rows = height
        self.cols = width

        # Initialize Snake
        self.snake = collections.deque([0, 0])   # Starting with (0, 0) position

        # Initialize Food
        self.d = collections.defaultdict(bool)
        for f in food:
            row, col = f[0], f[1]
            self.d[[row, col]] = True

    def move(self, direction: str) -> int:
        curPos = 
        newPos = curPos.copy()
        match direction:
            case "U":
                newPos[0] = self.snake[0][0] - 1
            case "D":
                newPos = Point(curPos.row + 1, curPos.col)
            case "L":
                newPos = Point(curPos.row, curPos.col - 1)
            case "R":
                newPos = Point(curPos.row, curPos.col + 1)
        
        print(f"NewPos: {newPos.row}, {newPos.col}")
        # Check if curPos is OOB
        if (newPos.row < 0 or newPos.row >= self.rows) or (newPos.col < 0 or newPos.col >= self.cols):
            return -1

        # Check if newPos is within Head & Tail!
        if newPos in self.snake and newPos != self.snake[-1]: # Dragged to self body!
            return -1

        # Check if there is food here
        if newPos in self.d:
            del self.d[newPos] # Delete food that's already eaten
            self.snake.appendleft(newPos)
        else:
            self.snake.appendleft(newPos)
            self.snake.pop()

        for point in self.snake:
            print(point.row, point.col)
        return len(self.snake)-1

game = SnakeGame(3, 2, [[1, 2], [0, 1]])
moves = [["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
for move in moves:
    print(game.move(move))

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)