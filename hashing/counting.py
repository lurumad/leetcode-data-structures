from collections import defaultdict, Counter
from typing import List


# Given a 2D array nums that contains n arrays of distinct integers,
# return a sorted array containing all the numbers that appear in all n arrays.
#
# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3
# and 4 are the only numbers that are in all arrays.
def intersection(nums: List[List[int]]) -> List[int]:
    counts = defaultdict(int)
    for arr in nums:
        for number in arr:
            counts[number] += 1
    answer = []
    length = len(nums)
    for key in counts:
        if counts[key] == length:
            answer.append(key)
    return answer


# Given a string s, determine if all characters have the same frequency.
#
# For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb",
# return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
def are_all_occurrences_equal(s: str) -> bool:
    # one liner
    # return len(set(Counter(s).values())) == 1

    counts = defaultdict(int)
    for character in s:
        counts[character] += 1
    frequencies = counts.values()
    return len(set(frequencies)) == 1


# Example 4: 560. Subarray Sum Equals K
#
# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
def subarray_sum(numbers: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    answer = current = 0
    for number in numbers:
        current += number
        answer += counts[current - k]
        counts[current] += 1
    return answer


# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri
# defeated player loseri in a match.
#
# Return a list answer of size 2 where:
#
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
#
# Note:
#
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.
def find_winners(matches: List[List[int]]) -> List[List[int]]:
    counts = defaultdict(int)
    players = set()
    for match in matches:
        winner = match[0]
        losser = match[1]
        players.add(winner)
        players.add(losser)
        counts[losser] += 1
    no_matches_lost = []
    one_match_lost = []
    for player in players:
        if player not in counts:
            no_matches_lost.append(player)
        elif counts[player] == 1:
            one_match_lost.append(player)
    return [sorted(no_matches_lost), sorted(one_match_lost)]


# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
def largest_unique_number(nums: List[int]) -> int:
    counter = Counter(nums)
    answer = -1
    for number in nums:
        if counter[number] == 1:
            answer = max(answer, number)
    return answer


# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as
# possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
def max_number_of_balloons(text: str) -> int:
    counts = Counter(text)
    return min(counts["b"], min(counts["a"], min(counts["l"] // 2, min(counts["o"] // 2, counts["n"]))))


def find_max_length(nums: List[int]) -> int:
    counts = defaultdict(int)
    count = 0
    answer = 0
    counts[0] = -1
    for index, number in enumerate(nums):
        count = count + (-1 if number == 0 else 1)
        if count in counts:
            answer = max(answer, index - counts[count])
        else:
            counts[count] = index
    return answer


# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at
# most k distinct characters.
#
# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = answer = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        answer = max(answer, right - left + 1)
    return answer


def string_anagram(dictionary, query):
    result = []
    counts = dict()

    for d in dictionary:
        s = str(''.join(sorted(d)))
        if s in counts:
            counts[s] = + 1
        else:
            counts[s] = 1

    for q in query:
        s = ''.join(sorted(q))
        if s in counts:
            result.append(counts[s])
        else:
            result.append(0)
    return result


def longest_subarray(arr):
    k = 1
    left = ans = start = 0
    freq = Counter()
    for right in range(len(arr)):
        freq[arr[right]] += 1
        while len(freq) > 2 or max(freq) - min(freq) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        if right - left + 1 > ans:
            ans = right - left + 1
            start = left
    return arr[start:start + ans]


if __name__ == '__main__':
    print(intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
    print(are_all_occurrences_equal("abcabc"))
    print(subarray_sum([1, 2, 1, 2, 1], 3))
    print(find_winners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    print(largest_unique_number([5, 7, 3, 9, 4, 9, 8, 3, 1]))
    print(max_number_of_balloons("loonbalxballpoon"))
    print(find_max_length([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))
    print(string_anagram(["heater", "cold", "clod", "reheat", "docl"], ["codl", "heater", "abcd"]))
    print(longest_subarray([0, 1, 2, 1, 2, 3]))
    print(longest_subarray([0, 1, 2, 1, 2, 3, 2, 3, 2, 3]))