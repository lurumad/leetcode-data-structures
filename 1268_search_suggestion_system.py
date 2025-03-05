from typing import List


def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
    products.sort()
    result = []
    left = 0
    right = len(products) - 1
    for i in range(len(search_word)):
        search = search_word[i]

        while left <= right and len(products[left]) <= i or products[left][i] != search:
            left += 1
        while left <= right and len(products[right]) <= i or products[right][i] != search:
            right -= 1

        words_left = right - left + 1

        if words_left >= 3:
            result.append([products[left], products[left+1], products[left+2]])
        elif words_left == 2:
            result.append([products[left], products[left+1]])
        elif words_left == 1:
            result.append([products[left]])
        else:
            result.append([])

    return result


if __name__ == "__main__":
    print(suggested_products(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        "monitor"
        )
    )
