# Question 02: Missing Number - https://leetcode.com/problems/missing-number/description/
'''
Description:

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        if n not in nums:
            return len(nums)
        if 0 not in nums:
            return 0
        
        sorted_nums = sorted(nums)

        for i in range(n):
            if sorted_nums[i + 1] - sorted_nums[i] == 2:
                return sorted_nums[i] + 1



# Test Data

nums = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1], [1]]
ans = [2, 2, 8, 0]

# Test

sol = Solution()

for i in range(len(ans)):
    myAns = sol.missingNumber(nums[i])
    if myAns != ans[i]:
        print(f"Test {i} Failed. My Answer: {myAns}. Correct Answer: {ans[i]}")
    else:
        print(f"Test {i} Passed.")