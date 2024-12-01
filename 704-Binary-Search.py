class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        found = False
        
        while (left <= right and not found):
            mid = (left + right)// 2
            if nums[mid] == target:
                found = True
                return mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1        
        
            
        