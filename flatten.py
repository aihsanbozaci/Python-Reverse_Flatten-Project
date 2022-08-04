l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l_new = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            l_new.append(i)

flatten(l)
print(l_new)

