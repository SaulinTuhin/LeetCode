# Problem - 2337. Move Pieces to Obtain a String
# Python3 Solution!
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        need_left, right_count = 0, 0
        for s, t in zip(start, target):
            if t == 'L':
                if right_count > 0:
                    return False
                need_left += 1
            if s == 'L':
                if need_left == 0:
                    return False
                need_left -= 1
            if s == 'R':
                if need_left > 0:
                    return False
                right_count += 1
            if t == 'R':
                if right_count == 0:
                    return False
                right_count -= 1
        return need_left == right_count == 0

    def canChange_1(self, start: str, target: str) -> bool:
        start_pos = []
        for i, c in enumerate(start):
            if c != '_':
                start_pos.append((c, i))
        target_pos = []
        for i, c in enumerate(target):
            if c != '_':
                target_pos.append((c, i))

        if len(start_pos) != len(target_pos):
            return False
        for i in range(len(start_pos)):
            if target_pos[i][0] == start_pos[i][0]:
                if target_pos[i][0] == 'R' and target_pos[i][1] < start_pos[i][1]:
                    return False
                elif target_pos[i][0] == 'L' and target_pos[i][1] > start_pos[i][1]:
                    return False
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.canChange("_L__R__R_", "L______RR"))
    print(sol.canChange("R_L_", "__LR"))
    print(sol.canChange("_R", "R_"))
