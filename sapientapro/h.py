nums = [3, 1, 0]


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        c=0
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i]!=1):
                return (nums[i] + 1)
                c=2
        if(c!=2):
            return (nums[len(nums)-1]+1)

# nums.sort()
# print(nums)
sol = Solution()
sol.missingNumber(nums)
