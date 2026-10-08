def located_cards(cards, query):
    left = 0
    right = len(cards) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == query:
            result = mid
            right = mid - 1
        elif cards[mid] < query:
            left = mid + 1
        else:
            right = mid - 1

    return result