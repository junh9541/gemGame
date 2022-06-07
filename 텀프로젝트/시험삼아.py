import random

a=random.sample(range(1, 7), 3)
print(a)

gemPNG = {
    1:"1.png",
    2:"2.png",
    3:"3.png",
    4:"4.png",
    5:"5.png",
    6:"6.png", ##노랑 추가
    7:"7.png"
}

print(gemPNG[1])
print(range(1, 4))

class A:
    def __init__(self, a):
        self.cla=a
    def update(self):
        self.cla.x+=1
class B:
    def __init__(self, a):
        self.cla=a
    def print(self):
        print(self.cla.x)

class C:
    def __init__(self):
        self.x=0

c=C()
a=A(c)
b=B(c)
a.update()
b.print()
