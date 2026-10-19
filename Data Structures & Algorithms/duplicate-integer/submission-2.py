class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        if len(nums) != len(seen):
            return True
        else: 
            return False