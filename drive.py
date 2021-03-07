import sys
import time
import easygui as gui
import pygame
from pygame.locals import *


class CarMain():

    width=800
    height=600
    #创建一个汽车
    my_car = None
    wall = None

    #开始游戏
    def startGame(self):
        pygame.init()

        screen=pygame.display.set_mode((CarMain.width,CarMain.height),0,32)
        pygame.display.set_caption('自动驾驶演示')

        # 十字路口
        CarMain.wall1 = Wall(screen,0,200,350,50)
        CarMain.wall2 = Wall(screen, 0, 400, 350, 50)
        CarMain.wall3 = Wall(screen, 350, 0, 50, 250)
        CarMain.wall4 = Wall(screen, 600, 0, 50, 200)
        CarMain.wall5 = Wall(screen, 600, 200, 200, 50)
        CarMain.wall6 = Wall(screen, 600, 400, 200, 50)
        CarMain.wall7 = Wall(screen, 350, 400, 50, 200)
        CarMain.wall8 = Wall(screen, 600, 400, 50, 200)
        #模拟车辆
        CarMain.my_car=My_Car(screen)

        while True:
            screen.fill((220,220,220))
            CarMain.wall1.display()
            CarMain.wall1.hit_other()

            CarMain.wall2.display()
            CarMain.wall2.hit_other()

            CarMain.wall3.display()
            CarMain.wall3.hit_other()

            CarMain.wall4.display()
            CarMain.wall4.hit_other()

            CarMain.wall5.display()
            CarMain.wall5.hit_other()

            CarMain.wall6.display()
            CarMain.wall6.hit_other()

            CarMain.wall7.display()
            CarMain.wall7.hit_other()

            CarMain.wall8.display()
            CarMain.wall8.hit_other()

            #获取事件
            self.get_event(CarMain.my_car,screen)
            #显示汽车
            CarMain.my_car.display()
            CarMain.my_car.move()

            time.sleep(0.05)
            pygame.display.update()

    #事件
    def get_event(self,my_car,screen):
        for event in pygame.event.get():
            if event.type==QUIT:
                self.stopGame()
            if event.type==KEYDOWN and (not my_car)and event.key==K_n:
                CarMain.my_car=My_Car(screen)
            if event.type==KEYDOWN and my_car:
                if event.key == K_LEFT:
                    my_car.direction = "L"  # 左移
                    my_car.stop = False
                    # my_car.move()
                if event.key == K_RIGHT:
                    my_car.direction = "R"  # 右边移动
                    my_car.stop = False
                    # my_car.move()
                if event.key == K_UP:
                    my_car.direction = "U"  # 上移
                    my_car.stop = False
                    # my_car.move()
                if event.key == K_DOWN:
                    my_car.direction = "D"  # 下移
                    my_car.stop = False
                    # my_car.move()
                if event.key == K_ESCAPE:  # esc退出
                    self.stopGame()
              #  if event.key == K_SPACE:  # 设置速度


            #if event.type == KEYUP and my_car:
             #   if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_UP:
              #      my_car.stop = True

    #结束游戏
    def stopGame(self):
        sys.exit()

class BaseItem(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
    #图片显示到屏幕上
    def display(self):
        self.image=self.images[self.direction]
        self.screen.blit(self.image,self.rect)

class Car(BaseItem):
    #定义汽车
    width=100
    height=100
    def __init__(self,screen,left,top):
        super(Car,self).__init__(screen)
        #汽车默认方向朝上
        self.direction="R"
        self.speed=10
        self.stop=False
        self.images={}
        self.images["L"] = pygame.image.load("1L.png")#(r"C:\Users\new\Desktop\drive\1L.png")
        self.images["R"] = pygame.image.load("1R.png")#(r"C:\Users\new\Desktop\drive\1R.png")
        self.images["U"] = pygame.image.load("1U.png")#(r"C:\Users\new\Desktop\drive\1U.png")
        self.images["D"] = pygame.image.load("1D.png")#(r"C:\Users\new\Desktop\drive\1D.png")

        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.oldleft=self.rect.left
        self.oldtop=self.rect.top

    def stay(self):
        self.rect.left=self.oldleft
        self.rect.top=self.oldtop



    def move(self):
        #如果汽车不是停止状态
        if not self.stop:
            self.oldleft=self.rect.left
            self.oldtop=self.rect.top
            if self.direction=="L":
                if self.rect.left>0:
                    self.rect.left-=self.speed
                    if self.rect.left==600:
                        choice1 = gui.buttonbox(title="路标", images=("left.jpg","straight.jpg","right.jpg"),choices=())
                        if choice1 == "straight.jpg":
                            self.rect.left -= self.speed
                        elif choice1=="left.jpg":
                            while self.rect.left>400:
                                self.rect.left-=self.speed
                            self.direction="D"
                        elif choice1=="right.jpg":
                            while self.rect.left>500:
                                self.rect.left-=self.speed
                            self.direction="U"
                else:
                   self.rect.left=CarMain.width#0
            elif self.direction=="R":
                if self.rect.right<CarMain.width:
                    self.rect.right+=self.speed
                    if self.rect.right==400:
                        choice1 = gui.buttonbox(title="路标", images=("left.jpg","straight.jpg","right.jpg"),choices=())
                        if choice1 == "straight.jpg":
                            self.rect.right += self.speed
                        elif choice1=="left.jpg":
                            while self.rect.right<600:
                                self.rect.right+=self.speed
                            self.direction="U"
                        elif choice1=="right.jpg":
                            while self.rect.right<500:
                                self.rect.right+=self.speed
                            self.direction="D"
                else:
                    self.rect.right=0#CarMain.width #0

            elif self.direction=="D":
                if self.rect.bottom<CarMain.height:
                    self.rect.top+=self.speed
                    if self.rect.bottom==280:
                        choice1 = gui.buttonbox(title="路标", images=("left.jpg","straight.jpg","right.jpg"),choices=())
                        if choice1 == "straight.jpg":
                            self.rect.top += self.speed
                        elif choice1=="right.jpg":
                            while self.rect.bottom<350:
                                self.rect.bottom+=self.speed
                            self.direction="L"
                        elif choice1=="left.jpg":
                            while self.rect.bottom<400:
                                self.rect.bottom+=self.speed
                            self.direction="R"
                else:
                    self.rect.bottom=0#CarMain.height
            elif self.direction=="U":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                    if self.rect.top==400:
                        choice1 = gui.buttonbox(title="路标", images=("left.jpg","straight.jpg","right.jpg"),choices=())
                        if choice1 == "straight.jpg":
                            self.rect.top -= self.speed
                        elif choice1=="right.jpg":
                            while self.rect.top>300:
                                self.rect.top-=self.speed
                            self.direction="R"
                        elif choice1=="left.jpg":
                            while self.rect.top>250:
                                self.rect.top-=self.speed
                            self.direction="L"
                else:
                    self.rect.top=CarMain.height

class My_Car(Car):
    def __init__(self,screen):
        super(My_Car,self).__init__(screen,0,300)#创建我汽车，位置在屏幕左中间
        self.stop=True

class Wall(BaseItem):
    def __init__(self,screen,left,top,width,height):
        super(Wall,self).__init__(screen)
        #绘制墙
        self.rect=Rect(left,top,width,height)
        self.color=(255,142,0)
    def display(self):
        self.screen.fill(self.color,self.rect)

    #碰撞检测
    def hit_other(self):
        if CarMain.my_car:
            is_hit=pygame.sprite.collide_rect(self,CarMain.my_car)
            if is_hit:
                CarMain.my_car.stop=True
                CarMain.my_car.stay()



game=CarMain()
game.startGame()
