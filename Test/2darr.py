def twoSum(self, nums: List[int], target: int) -> List[int]:
    viewedNumsMap = {}

    for i, c in enumerate(nums):
        if viewedNumsMap.get(target - c) is not None:
            return [viewedNumsMap[target-c], i]
        else:
            viewedNumsMap[c] = i
