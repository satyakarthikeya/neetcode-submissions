class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        windowSum = 0
        l = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            while windowSum >= target:
                res = min(res , r -l +1)
                windowSum -= nums[l]
                l +=1
            
            
        return 0 if res == float('inf') else res