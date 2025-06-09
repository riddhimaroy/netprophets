nums = [-1, 1, 0, 3, -3]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]: 

        pre = [1]* len(nums)
        suf = [1]* len(nums)
        
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]

        print(pre)

        for i in range(len(nums)-1, 0, -1):
            suf[i-1] = suf[i]*nums[i]

        print(suf)

        for i in range(len(nums)):
            nums[i] = pre[i]*suf[i]

        print(nums)

# nums.sort()
# print(nums)
sol = Solution()
sol.productExceptSelf(nums)
