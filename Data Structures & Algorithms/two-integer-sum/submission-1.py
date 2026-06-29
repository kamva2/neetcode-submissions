class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        results = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                j = nums.index(diff)
                if i != j:
                    results.append(j)
                    results.append(i)
                    return sorted(results)