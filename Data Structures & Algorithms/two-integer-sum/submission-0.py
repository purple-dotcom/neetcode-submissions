class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        N = len(nums)
        for i in range(N):
            if nums[i] < target:
                l.append(nums[i])
        
        for i in range(N):
            for j in range(1+i,N):
                if nums[i]+nums[j] == target:
                    if i > j:
                        return [j,i]
                    else:
                        return [i,j]