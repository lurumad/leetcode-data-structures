import math
from typing import List


def ways_to_split_array(nums: List[int]) -> int:
    n = len(nums)
    prefix = [nums[0]]
    for index in range(1, n):
        prefix.append(nums[index] + prefix[-1])
    answer = 0
    for index in range(n - 1):
        left_section_sum = prefix[index]
        right_section_sum = prefix[-1] - prefix[index]
        if left_section_sum >= right_section_sum:
            answer += 1
    return answer


def running_sum(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [nums[0]]
    for index in range(1, n):
        prefix.append(nums[index] + prefix[-1])
    return prefix


def min_start_value(nums: List[int]) -> int:
    n = len(nums)
    prefix = [nums[0]]
    answer = 0
    found = False
    for index in range(1, n):
        prefix.append(nums[index] + prefix[-1])

    print(f"prefix: {prefix}")

    while not found:
        answer += 1
        for i in range(n):
            if answer + prefix[i] < 1:
                found = False
                break
            found = True
    return answer


def get_averages(nums: List[int], k: int) -> List[int]:
    if k == 0:
        return nums
    length = len(nums)
    prefix = [nums[0]]
    result = []
    for index in range(1, length):
        prefix.append(nums[index] + prefix[-1])
    for index in range(length):
        if index - k < 0 or index + k >= length:
            result.append(-1)
            continue
        diff = 0 if (index - k - 1) < 0 else prefix[index - k - 1]
        avg = math.floor((prefix[index + k] - diff) / (k * 2 + 1))
        result.append(avg)
    return result


if __name__ == '__main__':
    print(get_averages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
