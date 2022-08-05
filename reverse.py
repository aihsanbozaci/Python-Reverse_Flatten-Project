a = [[1, 2], [3, 4], [5, 6, 7]]
def rev():
    a[0].reverse()
    a[1].reverse()
    a[2].reverse()
    a.reverse()
    return a
rev()
print(a)
