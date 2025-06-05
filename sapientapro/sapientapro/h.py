nums = [0,0,1,0,0,3,0,2]


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        j=0
        k=-1
        
        for i in range(n):
            j=0
            k=k+1
            while j < n and (nums[j]!=0):
                j=j+1
            while k < n and (nums[k]==0):
                k=k+1

            if(j<n and k<n):
                nums[j], nums[k] = nums[k], nums[j]
                j, k = k, j

            print(nums)
        
sol = Solution()
sol.moveZeroes(nums)