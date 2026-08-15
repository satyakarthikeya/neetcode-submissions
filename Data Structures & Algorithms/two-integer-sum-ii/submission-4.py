class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        import bisect
        i,j = 0,len(numbers)-1
        s = numbers[i]+numbers[j]
        while s!=target:
            if s<target:
                i1 = bisect.bisect_left(numbers,target-numbers[j])
                s+=numbers[i1]-numbers[i]
                i = i1
            else:
                j1 = bisect.bisect_right(numbers,target-numbers[i])-1
                s+=numbers[j1]-numbers[j]
                j = j1
        return [i+1,j+1]