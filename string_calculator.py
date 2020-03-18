# string calculator field
# James Rine
from re import match


def add(comma_delimited_numbers):
    if not comma_delimited_numbers:
        return 0
    num_list_match = match(r'(?P<first_num>\d+)(,(?P<second_num>\d+))?', comma_delimited_numbers)
    if not num_list_match.group('second_num'):
        return int(num_list_match.group('first_num'))
    return int(num_list_match.group('first_num')) + int(num_list_match.group('second_num'))
