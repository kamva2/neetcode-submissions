class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        integers = {}

        for i in nums:
            if i not in integers:
                integers[i] = 1
            else:
                integers[i] = integers.get(i)+1
        for k in integers:
            if integers.get(k) > 1:
                return True
        return False