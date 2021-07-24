def missingRanges(nums, l, u):
    def getRange(lo, up):
        if lo == up:
            return "{}".format(lo)
        else:
            return "{}->{}".format(lo, up)

    missing_ranges = []
    pre = l - 1

    for i in range(len(nums) + 1):
        if i == len(nums):
            cur = u + 1
        else:
            cur = nums[i]
        if cur - pre >= 2:
            missing_ranges.append(getRange(pre + 1, cur - 1))

        pre = cur

    return missing_ranges

