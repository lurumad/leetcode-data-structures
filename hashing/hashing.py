from collections import defaultdict
from typing import List


# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
# If there are duplicates in arr, count them separately.
# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
def count_elements(arr: List[int]) -> int:
    unique_numbers = set(arr)
    total = 0
    for number in arr:
        if number + 1 in unique_numbers:
            total += 1
    return total


# Given an array of strings strs, group the anagrams together.
#
# For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
def group_anagrams(strs: List[str]) -> List[List[str]]:
    seen = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        seen[key].append(word)
    return list(seen.values())


# Example 2: 2260. Minimum Consecutive Cards to Pick Up
#
# Given an integer array cards, find
# the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.
def minimum_card_pickup(cards: List[int]) -> int:
    answer = len(cards)
    seen = defaultdict(int)
    for right in range(len(cards)):
        if cards[right] in seen:
            index = seen[cards[right]]
            answer = min(answer, right - index + 1)
        seen[cards[right]] = right
    return answer if answer <= len(cards) else -1


# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
def length_of_longest_substring(s: str) -> int:
    left = answer = 0
    for right in range(len(s)):
        if s[right] in s[left:right]:
            left = s.index(s[right], left) + 1
        answer = max(answer, right - left + 1)
    return answer


if __name__ == '__main__':
    print(count_elements([1, 1, 2]))
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(minimum_card_pickup([0, 0]))
    print(minimum_card_pickup([1, 0, 5, 3]))
    print(length_of_longest_substring("abcabcbb"))
