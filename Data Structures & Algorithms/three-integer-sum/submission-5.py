class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=[]

        for i,a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right = right - 1
                elif threeSum < 0:
                    left = left + 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while nums[left] == nums[left-1] and left < right:
                        left = left+1
        return res
        