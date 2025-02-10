class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Easiest way- Use sets.
        return len(nums) != len(set(nums))
