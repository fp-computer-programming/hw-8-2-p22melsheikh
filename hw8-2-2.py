# MEE 12/09/21


def sum_odds(lst):

    sum_of_odds = 0

    for x in lst:
        if x % 2 != 0:
            sum_of_odds += x
    return sum_of_odds

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)