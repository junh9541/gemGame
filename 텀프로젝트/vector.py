import math

class MyVector:
  def __init__(self, x, y):
    self.x=x
    self.y=y

  def __add__(self, Vector):
    return MyVector(self.x+Vector.x, self.y+Vector.y)
  
  def __sub__(self, Vector):
    return MyVector(self.x-Vector.x, self.y-Vector.y)
  
  def __mul__(self, scalar):
    return MyVector(scalar*self.x, scalar*self.y)
  
  def setPos(self, x, y):
    self.x=x
    self.y=y

  def normalize(self):
    mag=self.getMagnitude()
    self.x/=mag
    self.y/=mag

  def getMagnitude(self):
    mag=math.sqrt(math.pow(self.x,2)
    +math.pow(self.y,2))
    return mag

  def getState(self):
    return self.x, self.y

  def vec(self):
    return [self.x, self.y]


# class MyVector:
#   def __init__(self, dim, x, y, z):
#     self.x=x
#     self.y=y
#     self.z=z
#     self.dim = -1

#   def nomalize(self):
#     mag=self.getMagnitude()
#     self.x/=mag
#     self.y/=mag
#     self.z/=mag

#   def getMagnitude(self):
#     mag=math.sqrt(math.pow(self.x,2)
#     +math.pow(self.y,2)
#     +math.pow(self.z,2))
#     return mag

#   def getState(self):
#     return self.x, self.y, self.z

#   def scalarMulti(self, scalar): #과제
#     self.x*=scalar
#     self.y*=scalar
#     self.z*=scalar
#     return self

#   def __sub__(self, MyVector):  #과제
#     self.x-=MyVector.x
#     self.y-=MyVector.x
#     self.z-=MyVector.z
#     return self

#   def __add__(self, MyVector): #과제
#     self.x+=MyVector.x
#     self.y+=MyVector.x
#     self.z+=MyVector.z
#     return self

#   def minus(self, MyVector):#질문. 두 함수 모두 반환형이 
#     myvector인데 호출한 객체의 인자값을 바꾸는게 아니라 
#     곱, 차, 합의 결과값을 지닌 또다른 객체를 반환해야 하는 부분?






# # myVector까지만 만들고
# vec=MyVector(3, 2)
# print(vec.getState())
# b=vec.scalarMulti(3)
# print(vec.getState())

# # 이렇게 객체를 생성할 수도 있고 지금까지도 많이 해왔을 것.
# #세련되게 표현하는 방법이라고 생각하며 될듯

# class VectorBuilder:
#   def __init__(self):
#     self.x=None
#     self.y=None
#     self.z=None
#     self.dim =None

#   def setDim(self, dim):
#     self.dim=dim
#     return self

#   def setX(self, x):
#     self.x=x
#     return self

#   def setY(self, y):
#     self.y=y
#     return self

#   def setZ(self, z):
#     self.z=z
#     return self

#   def build(self):
#     vector=MyVector(self.dim, self.x, self.y, self.z)
#     return vector

# vec=VectorBuilder().setDim(3).setX(50).setY(100).setZ(15).build()
# print(vec.getState())

# #create 2d vector or 3dvector using preset

# class VectorBuilder2D(VectorBuilder):
#   def __init__(self):
#     super().__init__()
#     self.setZ(0)
#     self.setDim(2)

# class VectorBuilder3D(VectorBuilder):
#   def __init__(self):
#     super().__init__()
#     self.setDim(3)

# vector2D=VectorBuilder2D().setX(1).setY(50).build()
# print(vector2D.getState())
# vector2D.nomalise()
# print(vector2D.getState())
# print(vector2D.getMagnitude)

# vector3D=VectorBuilder2D().setX(1).setY(50).setZ(150).build()
# print(vector3D.getState())
# vector3D.nomalise()
# print(vector3D.getState())
# print(vector3D.getMagnitude)

# #디렉터-프리셋역할 0, 1로 채워진 데이터 생성 넘파이??np.제로스?
# class Director:
#   def vectorZeros(builder:VectorBuilder):
#     builder.setX(0)
#     builder.setY(0)
#     builder.setZ(0)

#   def vectorOnes(builder:VectorBuilder):
#     builder.setX(1)
#     builder.setY(1)
#     builder.setZ(1)

# builder3D=VectorBuilder3D()
# Director.vectorOnes(builder3D)
# vec3D=builder3D.build()
# print(vec3D.getState())