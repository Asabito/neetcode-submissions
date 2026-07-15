class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for idx1, val1 in enumerate(nums):
            s = target-val1
            for idx2, val2 in enumerate(nums[idx1+1:]):
                if s-val2 == 0: return [idx1, 1+idx2+idx1]
                