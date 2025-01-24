from typing import List


def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False


def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


def is_subsequence(s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


def sorted_squares(nums: List[int]) -> List[int]:
    count = len(nums)
    result = [0] * count
    left = 0
    right = len(nums) - 1
    for index in range(len(result) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[index] = pow(nums[left], 2)
            left += 1
        else:
            result[index] = pow(nums[right], 2)
            right -= 1
    return result


def reverse_words(s: str) -> str:
    chars = list(s)
    last_space_index = -1
    for str_index in range(0, len(s) + 1):
        if str_index != len(s) and s[str_index] != ' ':
            continue
        left = last_space_index + 1
        right = str_index - 1
        while left <= right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        last_space_index = str_index
    return ''.join(chars)


if __name__ == '__main__':
    print(check_if_palindrome("racecar"))
    print(check_for_target([1, 2, 3, 4, 5], 9))
    print(combine([1, 3, 5], [2, 4, 6]))
    print(is_subsequence("ace", "abcde"))
    print(reverse_words("Let's take LeetCode contest"))
