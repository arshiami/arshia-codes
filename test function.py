def test_function(y):
    y[1] = -2



x = [0, 1, 2]
y = x.copy()
test_function(y)
print(x)
