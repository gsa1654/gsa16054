# -*- coding: cp949 -*-
import pygame#임포트
import time
import Queue
import Image

move_count=0#이동카운트 초기화
can_ps=True#입력여부 초기화
movecount=0

game=[1,2,3,4,16,5,7,8,9,6,11,12,13,10,14,15]#게임판. 셋다 동일하게
Cpu_game=game[:]
puzzle=game[:]#16을 0으로

def cutimg(ig):#이미지 자르는 함수
    img=ig.resize((600,600))
    filename=["img\c1.jpg","img\c2.jpg","img\c3.jpg","img\c4.jpg","img\c5.jpg","img\c6.jpg","img\c7.jpg","img\c8.jpg","img\c9.jpg","img\c10.jpg","img\c11.jpg","img\c12.jpg","img\c13.jpg","img\c14.jpg","img\c15.jpg","img\c16.jpg"]
    for i in range(0,4):
        for j in range(0,4):    
            img.box=(150*j,150*i,150*j+150,150*i+150)
            tep=img.crop(img.box)
            tep.paste("Black",(0,0,150,1))
            tep.paste("Black",(0,149,150,150))
            tep.paste("Black",(0,0,1,150))
            tep.paste("Black",(149,0,150,150))
            tep.save(filename[4*i+j])

#BFS 알고리즘 S
def move(puzzle, index):
    newpuzzle = puzzle[:]
    newpuzzle[newpuzzle.index(16)] = newpuzzle[index]
    newpuzzle[index] = 16
    global movecount
    movecount += 1
    return newpuzzle

def printpuzzle(puzzle):
    print('*******')
    for i in range(4):
        for j in range(4):
            print(' '),
            if puzzle[i*4+j]!= 0:
                print "%2d" % (puzzle[i*4+j]),
            else:
                print "%2d" % (16),
        print('\n')

def printsolution(puzzle, solution):
    printpuzzle(puzzle)
    for i in solution:
        puzzle = move(puzzle,i)
        printpuzzle(puzzle)
        
def BFS2(puzzle):
    Q1 = Queue.Queue()
    Q2 = Queue.Queue()
    Q1.put(puzzle[:])
    Q2.put([])
    while True:
        temp=Q1.get()
        temp2=Q2.get()
        if(manhattan(temp)==0):
            return temp2
            break
        else:
            zeroindex = temp.index(16)

            if(zeroindex>3): #d
                d=manhattan(move(temp,zeroindex-4))
            else:
                d=100000
                
            if(zeroindex<12): #u
                u=manhattan(move(temp,zeroindex+4))
            else:
                u=100000
                
            if((zeroindex%4)!=3): #r
                r=manhattan(move(temp,zeroindex+1))
            else:
                r=100000
                
            if((zeroindex%4)!=0): #l
                l=manhattan(move(temp,zeroindex-1))
            else:
                l=100000

                
            if(d<=u and d<=r and d<=l):
                Q1.put(move(temp,zeroindex-4))
                Q2.put(temp2+[zeroindex-4])

            if(u<=d and u<=r and u<=l):
                Q1.put(move(temp,zeroindex+4))
                Q2.put(temp2+[zeroindex+4])

            if(r<=d and r<=u and r<=l):
                Q1.put(move(temp,zeroindex+1))
                Q2.put(temp2+[zeroindex+1])

            if(l<=d and l<=u and l<=r):
                Q1.put(move(temp,zeroindex-1))
                Q2.put(temp2+[zeroindex-1])


def manhattan(puzzle):
    md = 0
    for i in range(16):
        row1 = i // 4
        col1 = i % 4
        if puzzle[i] != 0:
            row2 = (puzzle[i]-1) // 4
            col2 = (puzzle[i]-1) % 4
        else:
            row2 = 3
            col2 = 3
        md += (abs(row1-row2) + abs(col1-col2))
    return md


class node:
    def __init__(self,puzzle,parent,depth):
        self.puzzle = puzzle
        self.parent = parent
        self.depth = depth
        self.md = manhattan(puzzle)
#BFS 알고리즘 E
def computer():#퍼즐 푸는 함수
    screen.fill((255,255,255))
    for i in range(0,16):
        a=Cpu_game[i]-1
        screen.blit(imgs[a],xys[i])
    pygame.display.flip()
    move=(BFS2(puzzle))
    g=Cpu_game
    for i in move:
        time.sleep(0.8)
        g=nto(i,g)

def nto(n,g):#숫자를 방향으로 전환
    a=n
    if a<15:
        if g[a+1]==16:
            g=do_right(g)
    if a>0:
        if g[a-1]==16:
            g=do_left(g)
    if a<11:
        if g[a+4]==16:
            g=do_down(g)
    if a>4:
        if g[a-4]==16:
            g=do_up(g)
    return g


def flip(game):#화면 초기화(더미)
    for i in range(0,16):
        screen.blit(imgs[game[i]-1],xys[game[i]-1])
    pygame.display.flip()


def do_right(gamp):#방향이동함수 (do_방향)
    game=gamp
    a=0
    n=0
    for i in range(0,16):
        if game[i]==16:
            a=i
    if xys[a][0]==100:
            return game
    else:
        n=a-1 
        tx=xys[n][0]
        ty=xys[n][1]
        m1x=xys[n][0]
        m1y=xys[n][1]
        m2x=xys[a][0]
        m2y=xys[a][1]
        for j in range(0,150):
            tx+=1
            screen.blit(imgs[15],(m1x,m1y))
            screen.blit(imgs[15],(m2x,m2y))
            screen.blit(imgs[game[n]-1],(tx,ty))
            pygame.display.flip()
            time.sleep(0.002)
        t=game[a]
        game[a]=game[a-1]
        game[a-1]=t
    return game

def do_left(gamp):
    game=gamp
    a=0
    n=0
    for i in range(0,16):
        if game[i]==16:
            a=i
    if xys[a][0]==550:
            return game
    else:
        n=a+1
        tx=xys[n][0]
        ty=xys[n][1]
        m1x=xys[n][0]
        m1y=xys[n][1]
        m2x=xys[a][0]
        m2y=xys[a][1]
        for j in range(0,150):
            tx-=1
            screen.blit(imgs[15],(m1x,m1y))
            screen.blit(imgs[15],(m2x,m2y))
            screen.blit(imgs[game[n]-1],(tx,ty))
            pygame.display.flip()
            time.sleep(0.002)
        t=game[a]
        game[a]=game[a+1]
        game[a+1]=t
    return game


def do_down(gamp):
    game=gamp
    a=0
    n=0
    for i in range(0,16):
        if game[i]==16:
            a=i
    if xys[a][1]==20:
            return game
    else:
        n=a-4 
        tx=xys[n][0]
        ty=xys[n][1]
        m1x=xys[n][0]
        m1y=xys[n][1]
        m2x=xys[a][0]
        m2y=xys[a][1]
        for j in range(0,150):
            ty+=1
            screen.blit(imgs[15],(m1x,m1y))
            screen.blit(imgs[15],(m2x,m2y))
            screen.blit(imgs[game[n]-1],(tx,ty))
            pygame.display.flip()
            time.sleep(0.002)
        t=game[a]
        game[a]=game[a-4]
        game[a-4]=t
    return game

def do_up(gamp):
    game=gamp
    a=0
    n=0
    for i in range(0,16):
        if game[i]==16:
            a=i
    if xys[a][1]==470:
            return game
    else:
        n=a+4
        tx=xys[n][0]
        ty=xys[n][1]
        m1x=xys[n][0]
        m1y=xys[n][1]
        m2x=xys[a][0]
        m2y=xys[a][1]
        for j in range(0,150):
            ty-=1
            screen.blit(imgs[15],(m1x,m1y))
            screen.blit(imgs[15],(m2x,m2y))
            screen.blit(imgs[game[n]-1],(tx,ty))
            pygame.display.flip()
            time.sleep(0.002)
        t=game[a]
        game[a]=game[a+4]
        game[a+4]=t
    return game




pygame.init()#파이게임 초기화
im=Image.open("image.jpg")#변환할 이미지 인풋
screen=pygame.display.set_mode((1000,700))#파이게임 스크린 셋
pygame.display.set_caption("15-puzle game")
screen.fill((255,255,255))
pygame.display.flip()

imgf="img"
imgs=[pygame.image.load(imgf+"\c1.jpg"),pygame.image.load(imgf+"\c2.jpg"),
      pygame.image.load(imgf+"\c3.jpg"),pygame.image.load(imgf+"\c4.jpg"),pygame.image.load(imgf+"\c5.jpg"),pygame.image.load(imgf+"\c6.jpg"),pygame.image.load(imgf+"\c7.jpg"),pygame.image.load(imgf+"\c8.jpg"),pygame.image.load(imgf+"\c9.jpg"),pygame.image.load(imgf+"\c10.jpg"),pygame.image.load(imgf+"\c11.jpg"),pygame.image.load(imgf+"\c12.jpg"),pygame.image.load(imgf+"\c13.jpg"),pygame.image.load(imgf+"\c14.jpg"),pygame.image.load(imgf+"\c15.jpg"),pygame.image.load("void.jpg")]
xys=[[100,20],[250,20],[400,20],[550,20],[100,170],[250,170],[400,170],[550,170],[100,320],[250,320],[400,320],[550,320],[100,470],[250,470],[400,470],[550,470]]
CountFont=pygame.font.Font("ng.ttf",20)

for i in range(0,16):
    a=game[i]-1
    screen.blit(imgs[a],xys[i])


COUNT=CountFont.render(str(move_count) + " moved",True,(0,0,0),(255,255,255))
screen.blit(COUNT,(750,50))
pygame.display.flip()

while True:#방향키 입력
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
    elif event.type==pygame.KEYDOWN :
        if event.key == pygame.K_RIGHT:
            if can_ps:
                can_ps=False
                game=do_right(game)
                move_count+=1
                #print move_count
                COUNT=CountFont.render(str(move_count) + " moved",True,(0,0,0),(255,255,255))
                screen.blit(COUNT,(750,50))
                pygame.display.flip()
                can_ps=True
        elif event.key == pygame.K_LEFT:
            if can_ps:
                can_ps=False
                game=do_left(game)
                move_count+=1
                #print move_count
                COUNT=CountFont.render(str(move_count) + " moved",True,(0,0,0),(255,255,255))
                screen.blit(COUNT,(750,50))
                pygame.display.flip()
                can_ps=True
        elif event.key == pygame.K_UP:
            if can_ps:
                can_ps=False
                game=do_up(game)
                move_count+=1
                #print move_count
                COUNT=CountFont.render(str(move_count) + " moved",True,(0,0,0),(255,255,255))
                screen.blit(COUNT,(750,50))
                pygame.display.flip()
                can_ps=True
        elif event.key == pygame.K_DOWN:
            if can_ps:
                can_ps=False
                game=do_down(game)
                move_count+=1
                #print move_count
                COUNT=CountFont.render(str(move_count) + " moved",True,(0,0,0),(255,255,255))
                screen.blit(COUNT,(750,50))
                pygame.display.flip()
                can_ps=True
        elif event.key == 13:
            computer()
        elif event.key == 96:
            cutimg(im)
            
pygame.quit()

movecount = 0
print(BFS2(puzzle))
print(movecount)
printsolution(puzzle, BFS2(puzzle))
