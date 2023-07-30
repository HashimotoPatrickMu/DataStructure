import random

class solution:
    def ___init__(self):
        pass
    def forward(self, nums: list[int], target: int) -> list[int]:
        nums_sorted = sorted(nums)
        
        left = 0
        right = len(nums_sorted) - 1
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right])
                if left_index == right_index:
                    right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
                return [left_index, right_index]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
if __name__ == "__main__":
    random.seed(0)
    nums = [random.randint(0,100) for _ in range(10)]
    print(f'nums: {nums}')
    target = 38
    print(f"target: {target}")
    func = solution()
    output = func.forward(nums, target)
    print(f'first index: {output[0]}')
    print(f'second index: {output[1]}')
