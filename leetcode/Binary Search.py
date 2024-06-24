class Solution:
    def search(self, nums, target):
        print("hello ")
        left = 0
        right = len(nums)-1
        nums.sort()
        while left<= right:
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle +1
            elif target < nums[middle]:
                right = middle -1 
        if left > right:
            return -1

print(Solution().search([-1,0,3,5,9,12], 9))