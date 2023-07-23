#! usr/bin/env python3

class solution:
    def __init__(self):
        pass
    def forawrd(self, nums: list, target: int) -> int:
        fast, slow = 0, 0
        length = len(nums)
        
        while fast < length:
            if nums[fast] != target:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == "__main__":
    nums = [1,2,2,3,2,4,5,6]
    target = 2
    func = solution()
    res = func.forawrd(nums, target)
    print(res)
