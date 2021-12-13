class Solution:
    def twoSum(self, nums, target):
        dict_ = {}

        for i, n in enumerate(nums):
            m = target - n
            if n in dict_:
                return [i, dict_[n]]
            else:
                dict_[m] = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
