import pyautogui as pp

size=[10,10]
bgc=(100,100,100)

z=pp.screenshot()
ss=0
s=[]
for y in range(z.height):
    if ss==0:
        for x in range(z.width):
            if z.getpixel((x,y))==(255,0,0):#...
                while z.getpixel((x+ss,y))==(255,0,0):
                    ss+=1
                ss-=1
                if ss>10:#don't shrink it too much...
                    for i in range(ss-1):#keep it square..
                        if not z.getpixel((x+ss,y))==(255,0,0):
                            ss=0
                    else:
                        s=[x+ss/2,y+ss/2]
                        ss=(ss+1)/2*5
                        print(x,y,ss)
                        while True:
                            if s[0]-ss<0:
                                break
                            a=z.getpixel((s[0]-ss,s[1]))
                            pp.moveTo(s[0]-ss,s[1])
                            if a!=(255,0,0) and a!=(128, 128, 128) and a!=(0,0,255) and a!=(173, 216, 230):#?
                                break
                            s[0]-=ss
                        while True:
                            if s[1]-ss<0:
                                break
                            a=z.getpixel((s[0],s[1]-ss))
                            if a!=(255,0,0) and a!=(128, 128, 128) and a!=(0,0,255) and a!=(173, 216, 230):#?
                                break
                            s[1]-=ss
                        ss=ss/3
                        pp.moveTo(s[0],s[1])
                        break
if s==[]:
    print('epic fail!!!')
    dfjghygf
    
ways=[[0,-1],[1,0],[0,1],[-1,0]]
g=[[[False,False,False,False] for ii in range(size[1])] for i in range(size[0])]
for x in range(size[0]):
    xx=int(s[0]+x*ss*3)
    for y in range(size[1]):
        yy=int(s[1]+y*ss*3)
        if z.getpixel((xx+ss,yy))!=bgc:
            g[x][y][1]=True
        if z.getpixel((xx-ss,yy))!=bgc:
            g[x][y][3]=True
        if z.getpixel((xx,yy+ss))!=bgc:
            g[x][y][2]=True
        if z.getpixel((xx,yy-ss))!=bgc:
            g[x][y][0]=True
h=[[i.copy() for i in ii] for ii in g]
t=[[False for ii in range(size[1])] for i in range(size[0])]
a=[[[0,0,0,0] for ii in range(size[1])] for i in range(size[0])]
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
                    pp.moveTo(s[0]+x*ss*3,s[1]+y*ss*3)
                    q=rrr.index(1)
                    if q&1:#WHY THIS ?????????????????????????????????????why dos it happen? :((( ?????????????????????????
                        q=(q+2)%4#:(
                    for _ in range(q):
                        pp.click()

    tt=False
    for x in range(size[0]):
        for y in range(size[1]):
            if not t[x][y]:
                tt=True
                break
        
