import pygame,random
pygame.init()
disp = pygame.display.set_mode((1000,750),pygame.FULLSCREEN)
# variables
#عکس ها
zamin=pygame.image.load("zamin.jpg")
real=pygame.image.load("real madrid.jpg")
barsa=pygame.image.load("barcelona.jpg")
toop=pygame.image.load("toop.jpg")
#صدا ها
wait_sound=pygame.mixer.Sound("wait.wav")
#اندازه عکس ها
zamin=pygame.transform.scale(zamin,(1000,700))
real=pygame.transform.scale(real,(100,120))
barsa=pygame.transform.scale(barsa,(100,120))
toop=pygame.transform.scale(toop,(40,50))
#فونت ها
font=pygame.font.SysFont("Abril fatface",30)
#مختصات مهره ها
class player:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vy=vy
        self.vx=vx
players_r=[]
players_b=[]
players_r.append(player(40,340,0,0))
players_r.append(player(300,340,0,0))
players_r.append(player(190,120,0,0))
players_r.append(player(190,570,0,0))
players_b.append(player(860,340,0,0))
players_b.append(player(600,340,0,0))
players_b.append(player(710,120,0,0))
players_b.append(player(710,570,0,0))
class ball:
    def __init__(self,tx,ty,tvx,tvy):
        self.tx=tx
        self.ty=ty
        self.tvx=tvx
        self.tvy=tvy
ball1=ball(480,380,0,0)
print(ball1.tx)

# تابع برخورد به مهره
def  barkhord(players_r , players_b  ,ball1):
    for i in range(0,4):
        if (players_r[i].x < ball1.tx <players_r[i].x +100 and players_r[i].y < ball1.ty < players_r[i].y+120)  or (players_b[i].x < ball1.tx <players_b[i].x + 100 and players_b[i].y < ball1.ty < players_b[i].y +120):
            ball1.tvx=players_b[i].vx
    return(ball1.tvx,ball1.tvy)
def  barkhord2(ball1):
    if ball1.tx >= 1000 or ball1.tx <=0 or ball1.ty>=700 or ball1.ty<= 0:
        ball1.tvx=-ball1.tvx
        ball1.tvy=-ball1.tvy
    return(ball1.tvx,ball1.tvy)
def barkhord3(players_r,players_b,ax,ay,s):
    for i in range(4):
        if players_b[i].x>=800 or players_b[i].x<=100:
            players_b[i].vx=-(players_b[i].vx)
            if s==1:
                s=2
            if s==2:
                s=1
            ax=-ax
        elif players_r[i].x>=800 or players_r[i].x<=100:
            players_r[i].vx=-(players_r[i].vx)
            if s==1:
                s=2
            if s==2:
                s=1
            ax-=ax
        if players_b[i].y>=600 or players_b[i].y<=54:
            players_b[i].vy=-(players_b[i].vy)
            ay=-(ay)
        if players_r[i].y>=600 or players_r[i].y<=54:
            players_r[i].vy=-(players_r[i].vy)
            ay=-(ay)
            
#تابع حرکت
def harekat(players_r,players_b,nobat2,shomare2,ax,ay):
    if nobat2=='Barcelona':
        players_b[shomare2].x+=players_b[shomare2].vx
        players_b[shomare2].y+=players_b[shomare2].vy
        players_b[shomare2].vx+=ax
        players_b[shomare2].vy+=ay
    elif nobat2=='Real madrid':
        players_r[shomare2].x+=players_r[shomare2].vx
        players_r[shomare2].y+=players_r[shomare2].vy
        players_r[shomare2].vx+=ax
        players_r[shomare2].vy+=ay
#ورودي   ها
shomare=5
shomare2=0
turn=random.randint(1,2)
clk1=0
nobat2='hichi'
s=0
ax=0
ay=0
if turn==2:
    nobat="Real madrid"
else:
    nobat="Barcelona"
goal_real=0
goal_barsa=0
done = False
while not done:
    # events
    a=0
    for k in pygame.event.get():
        if k.type==pygame.QUIT:
            done=True
        if k.type==pygame.KEYDOWN:
            if k.key==pygame.K_END:
                done=True
        if k.type==pygame.MOUSEBUTTONDOWN:
            xm,ym=k.pos
            for i in range(0,4):
                if nobat=="Real madrid" and players_b[i].x<xm<players_b[i].x+100 and players_b[i].y<ym<players_b[i].y+120 or nobat=="Barcelona" and players_r[i].x <xm<players_r[i].x+100 and players_r[i].y<ym<players_r[i].y+120:
                    wait_sound.play()
                #پوزيشن دايره براي بارسا
                if players_r[i].x<xm<players_r[i].x+100 and players_r[i].y<ym<players_r[i].y+120 and turn%2==0:
                    shomare=i
                    turn+=1
                    nobat="Barcelona"
                    nobat2="Real madrid"
                    clk1=1
                    start_line=[xm,ym]
                #پوزيشن دايره براي مادريد 
                if players_b[i].x<xm<players_b[i].x+100 and players_b[i].y<ym<players_b[i].y+120 and turn%2==1:
                    shomare=i
                    turn+=1
                    nobat="Real madrid"
                    nobat2="Barcelona"
                    clk1=1
                    start_line=[xm,ym]
        if k.type==pygame.MOUSEMOTION and clk1==1:
            xw,yw=k.pos
            end_line=[xw,yw]
            pygame.draw.line(disp,(0,0,0),start_line,end_line,2)
            pygame.display.update()
        if k.type==pygame.MOUSEBUTTONUP:
            xup,yup=k.pos
            if nobat2=='Barcelona':
                vyn=ym-yup
                vxn=xm-xup
                if vxn<0:
                    s=1
                if vxn>0:
                    s=2
                ax=-(vxn//3)
                ay=-(vyn//3)
                players_b[shomare].vx=vxn
                players_b[shomare].vy=vyn
                shomare2=shomare
            if nobat2=='Real madrid':
                vyn=ym-yup
                vxn=xm-xup
                if vxn<0:
                    s=1
                if vxn>0:
                    s=2
                ax=-(vxn//3)
                ay=-(vyn//3)
                players_r[shomare].vx=vxn
                players_r[shomare].vy=vyn
                shomare2=shomare
            clk1=0
    # updates
    ball1.tx=ball1.tx+ball1.tvx
    ball1.ty=ball1.ty+ball1.tvy
    (ball1.tvx,ball1.tvy)=barkhord(players_r , players_b , ball1)
    (ball1.tvx,ball1.tvy)=barkhord2(ball1)
    nobat_ki=font.render("It's "+str(nobat)+" turn",True,(0,0,0))
    t_real=font.render("Real madrid : "+str(goal_real),True,(0,0,0))
    t_barsa=font.render("Barcelona : "+str(goal_barsa),True,(0,0,0))
    barkhord3(players_r,players_b,ax,ay,s)
    if nobat2=='Barcelona':
        if s==1:
            if players_b[shomare2].vx<0:
                harekat(players_r,players_b,nobat2,shomare2,ax,ay)
        if s==2:
            if players_b[shomare2].vx>0:
                harekat(players_r,players_b,nobat2,shomare2,ax,ay)
    if nobat2=='Real madrid':
        if s==1:
            if players_r[shomare2].vx<0:
                harekat(players_r,players_b,nobat2,shomare2,ax,ay)
        if s==2:
            if players_r[shomare2].vx>0:
                harekat(players_r,players_b,nobat2,shomare2,ax,ay)
    # draws
    disp.fill((255,255,255))
    disp.blit(zamin,(0,50))
    for i in range(0,4):
        #کشيدن مهره ها
        disp.blit(real,(players_r[i].x,players_r[i].y))
        disp.blit(barsa,(players_b[i].x,players_b[i].y))
        #کدام مهره
        if shomare==i and turn%2==1:
            pygame.draw.circle(disp,(0,0,0),(players_r[i].x+50,players_r[i].y+60),53,2)
        if shomare==i and turn%2==0:
            pygame.draw.circle(disp,(0,0,0),(players_b[i].x+50,players_b[i].y+60),53,2)
    #کشيدن توپ
    disp.blit(toop,(ball1.tx,ball1.ty))
    #کشيدن نوشته ها
    disp.blit(nobat_ki,(430,15))
    disp.blit(t_real,(20,15))
    disp.blit(t_barsa,(855,15))
    #کشيدن مستطيل
    pygame.draw.rect(disp,(0,0,0),(0,0,1000,50),5)
    #پايان
    pygame.display.update()
    pygame.time.Clock().tick(30)
pygame.quit()
