class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if target > i :
                    return nums.index(i)+1



if __name__ == '__main__':
    ss = Solution()
    nums = [1,2,3,4,5]
    target = 6
    res = ss.searchInsert(nums,target)
    print(res)