def binary_search(x, nums, start, end):
    if end >= start:
        mid_idx = int(start + (end - start) / 2)
        if x == nums[mid_idx]:
            return mid_idx
        elif x < nums[mid_idx]:
            return binary_search(x, nums, start, mid_idx)
        else:
            return binary_search(x, nums, mid_idx + 1, end)
    else:
        return -1


def search(nums, x):
    if nums is None or len(nums) == 0:
        return -1

    return binary_search(x, nums, 0, len(nums) - 1)


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    print(search(arr, x))
