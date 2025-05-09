# Question 03: Find All Numbers Diappeared in an array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
'''
Description:

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        min = 1
        max = len(nums)
        missing_nums = []

        if min not in nums:
            missing_nums.append(min)
        if max not in nums:
            missing_nums.append(max)

        sorted_nums = sorted(nums)

        for i in range(max-1):
            diff = sorted_nums[i+1] - sorted_nums[i]

            if diff > 1:
                for j in range(1, diff):
                    missing_nums.append(sorted_nums[i] + j)
        

        return missing_nums
    
# Test Data
nums = [[4,3,2,7,8,2,3,1], [1,1]]
ans = [[5,6], [2]]


# Run Test
sol = Solution()

for i in range(len(ans)):
    myAns = sol.findDisappearedNumbers(nums[i])
    if myAns != ans[i]:
        print(f"Test {i} Failed. My Answer: {myAns}. Correct Answer: {ans[i]}")
    else:
        print(f"Test {i} Passed.")