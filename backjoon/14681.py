x = int(input())
y = int(input())

x_positive, y_positive = True, True
if x < 0 : x_positive = False
if y < 0 : y_positive = False

if x_positive and y_positive : print(1)
elif not x_positive and y_positive : print(2)
elif not x_positive and not y_positive : print(3)
elif x_positive and not y_positive : print(4)
