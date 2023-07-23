#! usr/bin/env python3

class solution:
    def __init__(self):
        pass
    def forawrd(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            middle = left + (right - left) // 2
            
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

if __name__ == "__main__":
    nums = [1,2,3,4,6,8,10,13,15]
    target = 7
    func = solution()
    res = func.forawrd(nums, target)
    print(res)
    print(nums[res])
