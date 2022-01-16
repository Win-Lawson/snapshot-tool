import re

test = 'i=1,10, do: \n turtle.down(5)_fun     dfsadfkl      '
print(test)
print(re.split('\W+', test, 1))