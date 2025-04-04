# Question 01: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/
'''
Description:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
    


# Test Data

# Input
nums = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]

# Expected Output
output = [True, False, True]


# Testing

sol = Solution()
fail_count = 0

for i in range(len(nums)):
    if output[i] != sol.containsDuplicate(nums[i]):
        print(f"Test {i}: Failed.")
        fail_count += 1
    else:
        print(f"Test {i}: Passed")

if fail_count > 0:
    print(f"You had {fail_count} failures. Good effort, but go back and try again. ")
else:
    print(f"You nailed it! {fail_count} failures in your test. Try it on leetcode now!")
        

