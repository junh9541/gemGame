import pygame
import os
import vector as mv
import random

gemPNG = {
    1:"1.png",
    2:"2.png",
    3:"3.png",
    4:"4.png",
    5:"5.png",
    6:"6.png", 
    7:"7.png",
    8: "8.png",
    9: "9.png",
    10: "10.png",
    11: "11.png",
    12: "12.png",
    "loading": "loading.png"
}

class itemBase:
  def __init__(self):
    # self.size=100
    # self.speed=0
    self.pos=mv.MyVector(random.randint(50, 650), random.randint(150, 500))
  def updatePos(self):
    self.pos.setPos(random.randint(50, 650), random.randint(150, 500))



class Gem(itemBase):#
  def __init__(self, imageNumber):
    super().__init__()
    self.number=imageNumber
    self.image=pygame.transform.scale(
      pygame.image.load(gemPNG[imageNumber]), (45, 45))#이미지 스케일링은 팩토리로 옮긴다.
    self.loadImage=image=pygame.transform.scale(
      pygame.image.load(gemPNG["loading"]), (45, 45))#팩토리로 옯기기
    self.count=random.randint(1, 20)#팩토리로 옯기기. 함수로 생성
    self.state='B'

  def updateCount(self, a, b):
    self.count=random.randint(a,b)

  def checkState(self):
    if self.state=='A':#표시중
      return 'A'
    elif self.state=='B':#사라짐
      return 'B'
    else:
      return 'C'#대기중

  def changeState(self):
    if self.state=='A':#표시>사라짐
      self.state='B'
      self.updateCount(5, 10)
      self.updatePos()
    elif self.state=='B':#사라짐>대기
      self.state='C'
      self.updateCount(3, 3)
    elif self.state=='C':#대기>표시
      self.state='A'
      self.updateCount(10, 30)




    
#class SuperPower(itemBase):#젬말고 아이템을 만들어봄

class GemFactory: #넘버=화면에 나타날 보석 수(난이도와 관련)

  def createGem(self, imageNum):
    gem=Gem(imageNum)
    return gem
  
  def createGems(self, num):
    gemList=[]
    imageTuple=range(1, num+1)
    for a in imageTuple:
      gem=self.createGem(a)
      gemList.append(gem)
    return gemList


class Player:# 아이템 상속받아서 생성하기, 속도 추가
  def __init__(self):
    self.life=3#난이도 따라 설정
    self.pos=mv.MyVector(0, 0)
    self.image=pygame.image.load("1.png")
    self.record=0
  def setPos(self, x, y):
    self.pos.x=x
    self.pos.y=y
  def setLife(self, num):
    self.life=num
  def move(self, delta):
    self.pos=self.pos+delta
    


class Game:
  def __init__(self):
    self.pygame=pygame
    self.screen=0
    self.nY=600
    self.nX=750
  
  # def pickRandom(self, optionList:tuple, ch
  # oiceNum:int):
  #   result=tuple(random.sample(optionList, choiceNum))
  #   return result

  def setLevel(self, level):
    if level == 1:
      self.level = {"gem": 4, "answer": 1, "score": 10}
    elif level == 2:
      self.level = {"gem": 7, "answer": 2, "score": 5}
    elif level == 2:
      self.level = {"gem": 10, "answer": 3, "score": 3}

  def setGems(self, gemFactory:GemFactory):
    self.gemList=gemFactory.createGems(10)#여기 넣을 난이도가 필요함
    #random.shuffle(self.gemList)#출력될 순서 섞음
    #컬러 박스 함수 이용해 객체 리스트에 저장
    self.gemRectList=[]

    for gem in self.gemList:
      self.gemRectList.append(self.makeRect(gem.image, gem.pos.vec()))

    self.loadingRect=[]
    for gem in self.gemList:
      self.loadingRect.append(self.makeRect(gem.loadImage, gem.pos.vec()))
    print(len(self.loadingRect), "길이")

  def setPlayer(self, player:Player):# makeRect쓰는 거로 수정하기!
    player.image=pygame.transform.scale(player.image, (50, 50))
    playerRect=pygame.Rect(player.image.get_rect())
    playerRect.topleft=player.pos.vec()
    self.playerRect=playerRect

    self.player=player

  def setDisplay(self): #게임화면의 크기를 결정
    self.screen = self.pygame.display.set_mode([self.nX, self.nY])
    self.pygame.display.set_caption("Prince")

  def ready(self): 
    self.pygame.init()

  def makeRect(self, image, pos):
    characterRect=pygame.Rect(image.get_rect())
    characterRect.topleft=pos
    return characterRect

  def makeAnswer(self):
    a=3#뽑을 개수 임의 설정함. 후에 정답을...
    self.answer=random.sample(range(1, 8), a)

  def printInfo(self):
    x=30
    y=30
    for i in self.answer:
      self.screen.blit(self.gemList[i-1].image, (x, y))
      x+=65
    font= self.pygame.font.SysFont("consolas",35)
    lifeText = font.render("Life: "+str(self.player.life), True, (
      255, 255, 255), None) #self.pygame.Color(color)
    recordText = font.render("Score: "+str(self.player.record), True, (
      255, 255, 255), None) #self.pygame.Color(color)
    self.screen.blit(lifeText, (500, y))
    self.screen.blit(recordText, (500, y+40))

  def printText(self, msg, size, x, y):
    font= self.pygame.font.SysFont("consolas",size)
    Text = font.render(msg, True, (255, 255, 255), None)
    self.screen.blit(Text, (x, y))

  def moveGem(self):
    for i, v in enumerate(self.gemList):
      # print(v.state)
      if v.state=='A':
        self.gemRectList[i].topleft= v.pos.vec()
        self.screen.blit(v.image, self.gemRectList[i])
      elif v.state=='C':
        self.loadingRect[i].topleft= v.pos.vec()
        self.screen.blit(v.loadImage, self.loadingRect[i])

  def checkCollision(self):
    for i, v in enumerate(self.gemRectList):
      if v.colliderect(self.playerRect) and self.gemList[i].checkState()=='A':
        self.gemList[i].changeState()
        print(self.answer)
        if self.gemList[i].number in self.answer:
          self.answer.remove(self.gemList[i].number)
          if len(self.answer)==0:
            self.player.record+=5
            return True
        else: 
          self.player.life-=1
          print(self.player.life)
          if self.player.life<=-1: 
            print("종료!")
            return 'quit'


  def printRect(self, playerRect, image, pos):
    playerRect.topleft=pos
    self.screen.blit(image, playerRect)


  def launch(self):
    print("launch")
    clock = self.pygame.time.Clock()
    self.pygame.time.set_timer(pygame.USEREVENT, 300)
    delta = mv.MyVector(0, 0) #위치의 변화 저장
    my_event = self.pygame.USEREVENT + 1
    self.makeAnswer()
    keyFlag = None
    done = False 
    ending=False
    self.pygame.event.post(pygame.event.Event(pygame.USEREVENT+1))

    while not done: #계속해서 실행##수정!! 
      clock.tick(50) #정한 프레임마다 위치 업데이트

      for event in self.pygame.event.get():
        #event확인 후 QUIT라면 게임 종료
        if event.type == self.pygame.QUIT:
          done = True
        elif event.type ==self.pygame.USEREVENT + 1:
          ending=True
          
        #종류에 관계없이 키가 눌리면 "key down" 출력
        elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
          # print("key down")
          if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가? 눌린 키에 따라 delta를 변경한다.
              # print("K_LEFT")
              delta.x = -10
          elif event.key == self.pygame.K_RIGHT:
              # print("K_RIGHT")
              delta.x = 10
          elif event.key == self.pygame.K_DOWN:
              # print("K_DOWN")
              delta.y = 10
          elif event.key == self.pygame.K_UP:
              # print("K_UP")
              delta.y = -10
          

          # keyFlag = True
        elif event.type == self.pygame.KEYUP:
          delta.setPos(0, 0)
          # print("key up")
          keyFlag = False

        if event.type == self.pygame.USEREVENT:
          for i in range(len(self.gemList)):
            gemObj=self.gemList[i]
            gemObj.count-=1
            if gemObj.count==0:
              # print(gemObj.state)
              gemObj.changeState()
              # print(gemObj.state)

      # if keyFlag == True:
      self.player.move(delta) #주인공의 위치가 업데이트가 됨

      # print("pressed", self.player.pos.getState()) #in console
      self.screen.fill((0, 0, 0)) #Refined Abstraction의 특성을 살린 부분
      self.printRect(self.playerRect, self.player.image, self.player.pos.vec())  #캐릭터의 이름, 색, 위치제공하여 출력
      self.printInfo()
      self.moveGem()

      answerflag=self.checkCollision()
      if answerflag==True: self.makeAnswer()
      elif answerflag=='quit': ending=True

      if ending==True:
        pygame.time.delay(500)
        self.screen.fill((0, 0, 0))
        pygame.time.delay(1000)
        self.printText("Your Final Score is", 25, 250, 240)
        pygame.display.flip()
        pygame.time.delay(1000)
        self.printText(str(self.player.record), 35, 370, 280)
        pygame.display.flip()
        pygame.time.delay(5000)
        done=True


      self.pygame.display.flip()

    self.pygame.quit()

addr=os.path.abspath(__file__)
os.chdir(os.path.dirname(addr))
game=Game()
game.ready()

game.setDisplay()
game.setPlayer(Player())
game.setGems(GemFactory())

game.launch()
