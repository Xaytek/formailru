"""TEST"""


def test_turpe_not_exist_string():
    tup = ('Hello', 10, "22", 1, 150)
    for item in tup:
        if not isinstance(item, int):
            return False
    return True


assert not test_turpe_not_exist_string()


"""TEST"""


def test_try_except():
    try:
        10 + 'string'
        return False
    except TypeError:
        return True


assert test_try_except()


"""TEST"""


lst = [1, 1, 1, 1, 9, 10, 9, 1, 2, 0, 1, 98, 67]
lst1 = [0, 1, 1, 1, 1, 1, 1, 2, 9, 9, 10, 67, 98]
def test_bubble_sort ():
    n= 1
    while n <len (lst):
         for i in range (len (lst) -n):
              if lst [i]>lst [i + 1]:
                   lst [i], lst [i + 1]= lst [i + 1], lst [i]
         n += 1
    return (lst)

assert test_bubble_sort() == lst1
