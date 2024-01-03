from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])

        for r in range(row):
            for c in range(col):
                total, count = 0, 0
            
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0  or i == row or j < 0 or j == col:
                            continue
                        total += img[i][j] % 256
                        count += 1

                img[r][c] |= (total // count) << 8
        
        for r in range(row):
            for c in range(col):
                img[r][c] >>= 8
        
        return img


def printImg(img: List[List[int]]):
    for r in range(len(img)):
        for c in range(len(img[0])):
            print(img[r][c], end=" ")
        print()

if __name__ == '__main__':
    sol = Solution()

    input1 = [[1,1,1],[1,0,1],[1,1,1]]
    input2 = [[100,200,100],[200,50,200],[100,200,100]]

    printImg(sol.imageSmoother(input1))
    printImg(sol.imageSmoother(input2))