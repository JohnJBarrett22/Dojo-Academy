import unittest

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
    
    def test_min(self):
        self.assertEqual(min([10,9,8,7,6,5,4,3,2,1]),1)
        self.assertEqual(min([5,-10,15,-20,25,-30]),-30)
        self.assertEqual(min([-1,-2,3,-4,5,-6,-7,-99.3, 0.01, 4.52]), -99.3)

    def test_sum_list(self):
        self.assertEqual(sum_list([0,2,4,6,8,10,12,14,16,18,20]),110)
        self.assertEqual(sum_list([-15,-10,-5,0,5,10,15]),0)
        self.assertEqual(sum_list([.25,.75,3,6,9,-3,0,-1,20]),35)

    def test_less_than(self):
        self.assertTrue(less_than(3), True)
        self.assertFalse(less_than(103), True)
        self.assertTrue(less_than(-55), True)