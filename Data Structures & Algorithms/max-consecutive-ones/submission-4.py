class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            count = 0
            for j in range(i, len(nums)):
                if nums[j]==0:
                    break
                else:
                    count +=1
                result = max(result, count)
        return result