from typing import List
from collections import deque

# Problem - 773. Sliding Puzzle
# Python3 Solution!
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adjecent = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        board_state = "".join(str(ch) for row in board for ch in row)
        queue = deque([(board_state, 0)])
        visited = set(board_state)
        while queue:
            prev_board, moves = queue.popleft()
            if prev_board == "123450": return moves
            i = prev_board.index("0")
            prev_board = list(prev_board)
            for j in adjecent[i]:
                new_board = prev_board.copy()
                new_board[i], new_board[j] = prev_board[j], prev_board[i]
                new_board = "".join(new_board)
                if new_board not in visited:
                    queue.append([new_board, moves + 1])
                    visited.add(new_board)
            moves += 1
        return -1


if __name__=="__main__":
    sol = Solution()
    
    print(sol.slidingPuzzle([[1,2,3],[4,0,5]]))
    print(sol.slidingPuzzle([[1,2,3],[5,4,0]]))
    print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))