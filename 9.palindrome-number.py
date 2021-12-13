#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            # arr = []
            reverted = 0
            while x > reverted:
                r = x % 10
                x = x // 10
                # arr.append(r)
                reverted = reverted * 10 + r

            # for i in range(len(arr) // 2):
            #     if arr[i] != arr[len(arr) - 1 - i]:
            #         return False

        return x == reverted or x == reverted // 10


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(12111121))
