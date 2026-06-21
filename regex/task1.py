# You are to retrieve all of the numbers in the file and compute the sum of the numbers.

import re

# handler = open('regex_sum_2433909.txt')
# total = 0
# for line in handler:
#     line = line.rstrip()
#     numbers = re.findall('[0-9]+', line)
#     if len(numbers) > 0:
#         total += sum(map(int, numbers))
# print(total)


print(sum(map(int, re.findall('[0-9]+', open('regex_sum_2433909.txt').read()))))