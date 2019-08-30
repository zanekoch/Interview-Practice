class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        solution = None
        nums = sorted(nums)
        for i in range(0, n-2):
            a = nums[i]
            front = i + 1
            back = n - 1
            while front < back:
                b = nums[front]
                c = nums[back]
                if solution == None:
                    solution = a+b+c
                if abs(a+b+c-target) < abs(solution-target):
                    solution = a+b+c
                if a+b+c > target:
                    back -= 1
                else:
                    front += 1
        return solution
