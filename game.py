import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0,0,255)
BLACK= (0,0,0)

def new_ball():
    global x,y,r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    a.append(x)
    x = randint(100, 900)
    b.append(x)
    r = 30
    c.append(r)
    d.append(0)
    x=randint(-5,5)
    e.append(x)
    x=randint(-5,5)
    f.append(x)
    circle(screen, RED, (a[i], b[i]), r)
    
def ball(x,y,r):
    circle(screen, RED,(x,y),r)
    
def megaball(x,y,r):
    circle(screen,BLUE,(x,y),r)
    
def mega_ball():
    global x,y,r
    x = randint(100, 1100)
    a.append(x)
    x = randint(100, 900)
    b.append(x)
    r = 15
    c.append(r)
    d.append(0)
    x=randint(-5,5)
    e.append(x*x)
    x=randint(-5,5)
    f.append(x*x)
    circle(screen, BLUE, (a[i], b[i]), r)

def isball():
    global count, pc
    if ((event.pos[0]-a[j])**2+(event.pos[1]-b[j])**2<=r**2) and (d[j]==0) and (j%5!=0):
        count+=1
        pc=1
        d[j]=1

def ismegaball():
    global count, pc
    if ((event.pos[0]-a[j])**2+(event.pos[1]-b[j])**2<=r**2) and (d[j]==0) and (j%5==0):
        count+=5
        pc=1
        d[j]=1

def move():
    global i
    for j in range (i):
        if ((a[j]-c[j]+e[j])<0) or ((a[j]+c[j]+e[j])>1200):
            e[j]=-e[j]
        if ((b[j]-c[j]+f[j])<0) or ((b[j]+c[j]+f[j])>1200):
            f[j]=-f[j]
        a[j]+=e[j]
        b[j]+=f[j]
        if j+5<i:
            d[j]=1
        if (d[j]==0) and (j%5!=0):
            ball(a[j]+e[j],b[j]+f[j],30)
        elif (d[j]==0):
            megaball(a[j]+e[j],b[j]+f[j],15)


    
pygame.display.update()
clock = pygame.time.Clock()
finished = False
count=0
i=0
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
pc=0
k=0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for j in range (i):
                isball()
                ismegaball()
    move()
    pygame.display.update()
    screen.fill(BLACK)
    k+=1
    if (k==30) and (i%5==0):
        mega_ball()
        k=k-30
        i+=1
    elif k==30:
        new_ball()
        k=k-30
        i+=1
    if pc==1:
        print(count)
        pc=0

pygame.quit()
