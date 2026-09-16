class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash_set = set()
        for num in nums:
            if num in nums_hash_set:
                return True
            nums_hash_set.add(num)
        return False