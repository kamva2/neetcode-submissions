class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numbers = {}

        for num in nums:

            numbers[num] = numbers.get(num,0)+1
        
        top_k = sorted(numbers.values(),reverse=True)[:k]

        results = []

        for i,v in numbers.items():
            if v in top_k:
                results.append(i)
        return results