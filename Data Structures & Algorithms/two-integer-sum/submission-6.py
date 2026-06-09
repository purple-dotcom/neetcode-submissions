class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])
        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            s = A[i][0] + A[j][0]
            if s == target:
                    return [min(A[i][1], A[j][1]),
                            max(A[i][1], A[j][1])]
            elif s > target:
                j -= 1
            else:
                i += 1