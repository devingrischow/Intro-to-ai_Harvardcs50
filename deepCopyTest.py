import copy 
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = copy.deepcopy(xs)

xs.append(['new sublist'])
print(xs)
print(ys)
xs[1][0] = 'X'
print(xs)
print(ys)
