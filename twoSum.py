class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            if nums[i] in store:
                diffIndex = store[nums[i]]
                return [diffIndex,i]
            else:
                diffIndex2 = target - nums[i]
                store[diffIndex2] = i
