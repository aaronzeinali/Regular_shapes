from turtle import *

x = int(input('Enter a number: '))
y = 180 - (((x - 2) * 180) / x)
bob = Turtle()

for i in range(x):
    bob.forward(100)
    bob.left(y)

mainloop()