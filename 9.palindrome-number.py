#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (51.79%)
# Likes:    4586
# Dislikes: 1943
# Total Accepted:    1.7M
# Total Submissions: 3.2M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
#
# For example, 121 is a palindrome while 123 is not.
#
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Example 4:
#
#
# Input: x = -101
# Output: false
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
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
