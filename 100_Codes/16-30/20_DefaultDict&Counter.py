# Write a Python program to group a sequence of key-value pairs into a dictionary of lists.
# Write a Python program to compare two unordered lists (not sets).


from collections import Counter
from collections import defaultdict


def compare_lists(x, y):
    # print(Counter(x))
    return Counter(x) == Counter(y)
n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
print(compare_lists(n1, n2))


class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
d = defaultdict(list)

print (d)
for k, v in class_roll:
    d[k].append(v)
print(sorted(d.items()))
