# Problem - 1496: https://leetcode.com/problems/path-crossing/
# Python3 Solution!
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        prev_pos = set()
        x, y = 0, 0

        prev_pos.add((x, y))

        for direction in path:
            if direction == 'N':
                x+=1
            elif direction == 'S':
                x-=1
            elif direction == 'E':
                y+=1
            else:
                y-=1

            if (x , y) in prev_pos:
                return True
            else:
                prev_pos.add((x, y))

        return False


if __name__=="__main__":
    sol = Solution()

    print(sol.isPathCrossing("NES"))
    print(sol.isPathCrossing("NESWW"))