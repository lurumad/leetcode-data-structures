from collections import defaultdict


# Example 1: 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct
# order, and each closing bracket closes exactly one open bracket.
#
# For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.


def valid_parentheses(text: str) -> bool:
    stack = []
    for character in text:
        if character in "({[":
            stack.append(character)
            continue
        if not stack:
            return False
        previous_opening = stack.pop()
        if previous_opening == "(" and character != ")":
            return False
        if previous_opening == "{" and character != "}":
            return False
        if previous_opening == "[" and character != "]":
            return False
    return not stack


# Example 2: 1047. Remove All Adjacent Duplicates In String
#
# You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you
# can't anymore. Return the final string after this.
#
# For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get
# "ca". This is the final answer.

def remove_all_adjacent_duplicates(text: str) -> str:
    stack = []
    for character in text:
        if stack and character == stack[-1]:
            stack.pop()
            continue
        stack.append(character)
    return ''.join(stack)


# Example 3: 844. Backspace String Compare
#
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
# backspace character.
#
# For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to
# "ac".

def backspace_string_compare(s: str, t: str) -> bool:
    def check(text: str) -> str:
        stack = []
        for char in text:
            if char != '#':
                stack.append(char)
                continue
            if stack:
                stack.pop()
        return "".join(stack)

    return check(s) == check(t)


def simplify_path(path: str) -> str:
    stack = []
    path_splitting = path.split('/')
    for item in path_splitting:
        if item == '' or item == '.':
            continue
        if item == '..':
            if stack:
                stack.pop()
            continue
        stack.append(item)
    return f'/{"/".join(stack)}'


def two_adjacent_characters(s: str) -> str:
    stack = []
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
            continue
        stack.append(char)
    return "".join(stack)


if __name__ == "__main__":
    print(valid_parentheses("()[]"))
    print(remove_all_adjacent_duplicates("abccba"))
    print(backspace_string_compare("y#fo##f", "y#f#o##f"))
    print(simplify_path("/."))
    print(simplify_path("/home/"))
    print(simplify_path("/home////foo/"))
    print(simplify_path("/home/user/Documents/../Pictures"))
    print(simplify_path("/../"))
    print(simplify_path("/.../a/../b/c/../d/./"))
    print(simplify_path("/a//b////c/d//././/.."))
    print(simplify_path("/hello../world"))
    print(simplify_path("/..hidden"))
    print(simplify_path("/hello./world"))
    print(two_adjacent_characters("Aa"))
