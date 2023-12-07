import logging
from typing import List


logging.basicConfig(level=logging.DEBUG)

"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


"""


def add_up_k(k: int, number_list: List[int]) -> bool:
    """ loop through the numbers subtracting each from k,
        and check whether the remainder is on the list
    """
    add_up_check: List[int] = list(filter(
        lambda x: (k-x) in number_list, number_list))
    logging.info(f' list of number that pass this test {add_up_check}')

    return False if add_up_check == [] else True


if __name__ == "__main__":
    print(add_up_k(15, [10, 15, 8, 7]))
