class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            product = 1
            for k in range(len(nums)):
                
                if i == k:
                    continue
                product *= nums[k]
            output.append(product)
        
        return output