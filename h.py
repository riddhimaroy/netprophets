nums = [0,0,1,0,0,3,0,2]


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        j=0
        k=-1
        for i in range(n):
            j=0
            for x in range(i, n):
                if(nums[x]!=0):
                    j=j+1
                    print('j')
                else:
                    break
                
            for x in range(k+1, n):
                if(nums[x]==0):
                    k=k+1
                    print('k')
                else:
                    break

            k = k+1

            if(k<j):
                continue
            else:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                temp = j
                j = k
                k= temp
                print('j= ', j)
                print('k= ', k)

            print(nums)
        
sol = Solution()
sol.moveZeroes(nums)