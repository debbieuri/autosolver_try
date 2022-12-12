import pygame
pygame.init()

size=[10,10]
bgc=(100,100,100)

zz=pygame.image.load('d.png')

ss=zz.get_width()/size[0]/3
zz.set_colorkey(bgc)
z=pygame.mask.from_surface(zz)
ways=[[0,-1],[1,0],[0,1],[-1,0]]#<3
g=[[[False,False,False,False] for ii in range(size[1])] for i in range(size[0])]
for x in range(size[0]):
    for y in range(size[1]):
        if z.get_at((int((x*ss*3)+ss/2),int((y*ss*3)+ss+ss/2))):
            g[x][y][3]=True
        if z.get_at((int((x*ss*3)+ss+ss+ss/2),int((y*ss*3)+ss+ss/2))):
            g[x][y][1]=True
        if z.get_at((int((x*ss*3)+ss+ss/2),int((y*ss*3)+ss/2))):
            g[x][y][0]=True
        if z.get_at((int((x*ss*3)+ss+ss/2),int((y*ss*3)+ss+ss+ss/2))):
            g[x][y][2]=True

h=[[i.copy() for i in ii] for ii in g]
t=[[False for ii in range(size[1])] for i in range(size[0])]
a=[[[0,0,0,0] for ii in range(size[1])] for i in range(size[0])]

d=pygame.display.set_mode((zz.get_width(),zz.get_height()))
def show():
    d.fill((0,0,0))
    for x in range(size[0]):
        for y in range(size[1]):
            pygame.draw.rect(d,(255,0,0),(int((x*ss*3)+ss),int((y*ss*3)+ss),ss,ss))
            if h[x][y][3]:
                pygame.draw.rect(d,(255,0,0),(int((x*ss*3)),int((y*ss*3)+ss),ss,ss))
            if h[x][y][1]:
                pygame.draw.rect(d,(255,0,0),(int((x*ss*3)+ss+ss),int((y*ss*3)+ss),ss,ss))
            if h[x][y][0]:
                pygame.draw.rect(d,(255,0,0),(int((x*ss*3)+ss),int((y*ss*3)),ss,ss))
            if h[x][y][2]:
                pygame.draw.rect(d,(255,0,0),((int((x*ss*3)+ss),int((y*ss*3)+ss+ss),ss,ss)))
    pygame.display.update()
    
def show2():
    cc=[(0,0,0),(0,255,0),(0,0,255)]
    for x in range(size[0]):
        for y in range(size[1]):
            #pygame.draw.rect(d,(255,0,0),(int((x*ss*3)+ss),int((y*ss*3)+ss),ss,ss))
            #print(a[x][y])
            if a[x][y][3]!=0:
                pygame.draw.rect(d,cc[a[x][y][3]],(int((x*ss*3)),int((y*ss*3)+ss),ss,ss),4)
            if a[x][y][1]!=0:
                pygame.draw.rect(d,cc[a[x][y][1]],(int((x*ss*3)+ss+ss),int((y*ss*3)+ss),ss,ss),4)
            if a[x][y][0]!=0:
                pygame.draw.rect(d,cc[a[x][y][0]],(int((x*ss*3)+ss),int((y*ss*3)),ss,ss),4)
            if a[x][y][2]!=0:
                pygame.draw.rect(d,cc[a[x][y][2]],(int((x*ss*3)+ss),int((y*ss*3)+ss+ss),ss,ss),4)
    pygame.display.update()

show()


rr=[[[False,False,False,False]for _ in range(size[1])]for _ in range(size[0])]
for x in range(size[0]):
    for y in range(size[1]):
        rrrr=[]
        for r in range(4):
            rrr=[0,0,0,0]
            for v in range(4):
                if g[x][y][(r+v)%4]:
                    rrr[v]=1
            if rrr not in rrrr:
                rrrr.append(rrr)
                rr[x][y][r]=True

tt=True
while tt:
    print('SOLVING!!')
    for x in range(size[0]):
        for y in range(size[1]):
            if not t[x][y]:
                for i in range(4):
                    if a[x][y][i]==0:
                        if x+ways[i][0]<0:
                            a[x][y][i]=-1
                        elif y+ways[i][1]<0:
                            a[x][y][i]=-1
                        elif x+ways[i][0]>=size[0]:
                            a[x][y][i]=-1
                        elif y+ways[i][1]>=size[1]:
                            a[x][y][i]=-1
                        else:
                            if a[x+ways[i][0]][y+ways[i][1]][i-2]==1:
                                a[x][y][i]=1
                            elif a[x+ways[i][0]][y+ways[i][1]][i-2]==-1:
                                a[x][y][i]=-1

                rrr=rr[x][y].copy()
                for r in range(4):
                    for v in range(4):
                        if g[x][y][(r+v)%4]:
                            if a[x][y][v]==-1:
                                rrr[r]=0
                                break
                        else:
                            if a[x][y][v]==1:
                                rrr[r]=0
                                break

                if sum(rrr)==1:
                    for v in range(4):
                        if g[x][y][(rrr.index(1)+v)%4]:
                            a[x][y][v]=1
                            h[x][y][v]=True
                        else:
                            a[x][y][v]=-1
                            h[x][y][v]=False
                    t[x][y]=True

                                
    show()             
    show2()
    pygame.event.get()
    tt=False
    for x in range(size[0]):
        for y in range(size[1]):
            if not t[x][y]:
                tt=True
                break
show()
print('SOLVED!!')













                        
