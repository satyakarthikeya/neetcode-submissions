class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =[[] for i in range(len(nums)+1)]
        ans = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] +=1
        for key , value in count.items():
            freq[value].append(key)
        for i in range(len(freq)-1,0 ,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans  