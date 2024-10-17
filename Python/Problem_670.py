# Problem - 670. Maximum Swap
# Python3 Solution!
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_val = max_i = -1
        left = right = -1
        for i in range(len(num_str) - 1, -1, -1):
            cur_num = int(num_str[i])
            if cur_num > max_val:
                max_val = cur_num
                max_i = i
            elif cur_num < max_val:
                left = i
                right = max_i
        
        if left == -1:
            return num
        
        num_str[left], num_str[right] = num_str[right], num_str[left]
        return int(''.join(num_str))
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.maximumSwap(2736))
    print(sol.maximumSwap(9973))