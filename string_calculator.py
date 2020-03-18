# string calculator field
# James Rine
from re import finditer


def get_nums(comma_delimited_numbers):
    match_iter = finditer(r'(?P<num>\d+),?', comma_delimited_numbers)
    nums = []
    while True:
        try:
            num_match = next(match_iter)
            nums.append(int(num_match.group('num')))
        except StopIteration:
            break
    return nums

def add(comma_delimited_numbers):
    if not comma_delimited_numbers:
        return 0
    nums = get_nums(comma_delimited_numbers)
    return sum(nums)