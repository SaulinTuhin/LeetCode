from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        d = set()

        for src, dest in paths:
            s.add(src)
            d.add(dest)

        return list(d-s)[0]


if __name__ == "__main__":
    sol = Solution()

    input1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    input2 = [["B","C"],["D","B"],["C","A"]]
    input3 = [["A","Z"]]

    print(sol.destCity(input1))
    print(sol.destCity(input2))
    print(sol.destCity(input3))