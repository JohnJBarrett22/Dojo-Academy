def min(l):
    # Should find and return minimum value in a given list
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100
### For this exercise, work within this class. This is something you will come up with on your own soon ###
class MainTest(unittest.TestCase):
    # tests go here!
