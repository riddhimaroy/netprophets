nums = [9,7,3,5,6,2,0,8,1,9]
k=6


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        summ = 0
        avg = 0.0
        maxx = 0.0

        summ = sum(nums[:k])
        
        avg = summ/k
        print(avg)

        if(len(nums)==k):
            return avg

        for i in range(1, len(nums)-k+1):
            summ=summ-nums[i-1]+nums[i+k-1]
            avg=summ/k

            print(avg)

            if(avg>maxx):
                maxx=avg

        return maxx
                    

sol = Solution()
sol.findMaxAverage(nums, k)
