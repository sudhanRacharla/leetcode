class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hashmap and hashmap[rem]!=i:
                return [i,hashmap[rem]]
        