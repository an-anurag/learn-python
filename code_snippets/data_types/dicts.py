
l1 = ['a', 'b', 'c', 'd', 'e']

l2 = [1, 2, 3]

d = {}

for i in zip(l1, l2):
    pass

d2 = {x[0]: x[1] for x in zip(l1, l2)}

# print(d2)