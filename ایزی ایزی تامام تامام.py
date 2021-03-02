import pygame,random,sys
pygame.init()
disp = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
# variables
#عکس ها
zamin=pygame.image.load("zamin.jpg")
ggg=pygame.image.load("ggg.png")
zamin1=pygame.image.load("zamin1.png")
zamin2=pygame.image.load("zamin2.png")
zamin3=pygame.image.load("zamin3.png")
real=pygame.image.load("real madrid.png")
barsa=pygame.image.load("barcelona.png")
up=pygame.image.load("up.png")
down=pygame.image.load("down.png")
logo=pygame.image.load("LOGO.png")
toop=pygame.image.load("toop.jpg")
juventus=pygame.image.load("Juventus.png")
bayern=pygame.image.load("Bayern.png")
perspolis=pygame.image.load("Perspolis.png")
esteghlal=pygame.image.load("Esteghlal.png")
font=pygame.font.SysFont("Abril fatface",30)
font2=pygame.font.SysFont("Abril fatface",40)
font1=pygame.font.SysFont("Abril fatface",25)
photo=pygame.image.load("photo.jpg")
#صدا ها
wait_sound=pygame.mixer.Sound("wait.wav")
goal_sound=pygame.mixer.Sound("Goal.wav")
#اندازه عکس ها
zamin=pygame.transform.scale(zamin,(300,200))
zamin1=pygame.transform.scale(zamin1,(300,200))
zamin2=pygame.transform.scale(zamin2,(300,200))
zamin3=pygame.transform.scale(zamin3,(300,200))
photo=pygame.transform.scale(photo,(1280,750))
logo=pygame.transform.scale(logo,(640,375))
up=pygame.transform.scale(up,(50,50))
down=pygame.transform.scale(down,(50,50))
ggg=pygame.transform.scale(ggg,(1280,750))
real=pygame.transform.scale(real,(100,100))
barsa=pygame.transform.scale(barsa,(100,100))
juventus=pygame.transform.scale(juventus,(100,100))
bayern=pygame.transform.scale(bayern,(100,100))
perspolis=pygame.transform.scale(perspolis,(100,100))
esteghlal=pygame.transform.scale(esteghlal,(100,100))
toop=pygame.transform.scale(toop,(50,50))
#ورودي ها
flag_player1=False
flag_player2=False
flag_player3=False
flag_play=False
flag_start=False
flag_from=0
play=0
start=0
p1=0
p2=0
p3=0
t_goal=1
g_goal=0
gh=0
nfont=0
x_box=1300
y_box=600
time=0
rang=(255,255,255)
#کلاس ها
class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
players_r=[]
players_b=[]
players_r.append(player(100,320))
players_r.append(player(400,320))
players_r.append(player(290,90))
players_r.append(player(290,570))
players_b.append(player(1085,320))
players_b.append(player(775,320))
players_b.append(player(890,90))
players_b.append(player(890,560))
class playerv:
    def __init__(self,vx,vy):
        self.vx=vx
        self.vy=vy
players_rv=[]
players_bv=[]
players_rv.append(playerv(2,2))
players_rv.append(playerv(2,2))
players_rv.append(playerv(2,2))
players_rv.append(playerv(2,2))
players_bv.append(playerv(2,2))
players_bv.append(playerv(2,2))
players_bv.append(playerv(2,2))
players_bv.append(playerv(2,2))
to=0
lo=0
flag1=0
flag2=0
goal=0
class ball:
    def __init__(self,tx,ty):
        self.tx=tx
        self.ty=ty
ball1=ball(620,360)
tvx=0
tvy=0
toopx=0
toopy=0
winner=0
player_r_v=[0,0,0,0]
player_b_v=[0,0,0,0]
#مهره ها تابع برخورد
def barkhord(players_r , players_b,turn,shomare,vx,vy,k2,h2,player_r_v,player_b_v):
    if turn=="Player2":
        if players_r[shomare].x+100>=1280 or players_r[shomare].x<=0:
            vx=-vx
    if turn=="Player1":
        if players_b[shomare].x+100>=1280 or players_b[shomare].x<=0:
            vx=-vx
    if turn=="Player2":
        if players_r[shomare].y<=50 or players_r[shomare].y+100>=720:
            vy=-vy
    if turn=="Player1":
        if players_b[shomare].y<=50 or players_b[shomare].y+100>=720:
            vy=-vy
    if turn=="Player1":
        for i in range(0,4):
            if shomare!=i:
                dis=( (players_b[i].y-players_b[shomare].y)**2 + (players_b[i].x-players_b[shomare].x)**2 )**0.5
                col=dis<=100
                if col==True and players_b[shomare].x+50>=players_b[i].x:
                    vx=-vx
                if col==True and players_b[shomare].x<=players_b[i].x+50:
                    vx=-vx
                if col==True and players_b[shomare].y<=players_b[i].y+50:
                    vy=-vy
                if col==True and players_b[shomare].y+50>=players_b[i].y:
                    vy=-vy
        for i in range(0,4):
            dis1=( (players_r[i].y-players_b[shomare].y)**2 + (players_r[i].x-players_b[shomare].x)**2 )**0.5
            col1=dis1<=100
            if col1==True and players_b[shomare].x+50>=players_r[i].x:
                vx=-vx
            if col1==True and players_b[shomare].x<=players_r[i].x+50:
                vx=-vx
            if col1==True and players_b[shomare].y<=players_r[i].y+50:
                vy=-vy
            if col1==True and players_b[shomare].y+50>=players_r[i].y:
                vy=-vy
    if turn=="Player2":
        for i in range(0,4):
            if shomare!=i:
                dis=( (players_r[i].y-players_r[shomare].y)**2 + (players_r[i].x-players_r[shomare].x)**2 )**0.5
                col=dis<=100
                if col==True and players_r[shomare].x+50>=players_r[i].x:
                    vx=-vx
                if col==True and players_r[shomare].x<=players_r[i].x+50:
                    vx=-vx
                if col==True and players_r[shomare].y<=players_r[i].y+50:
                    vy=-vy
                if col==True and players_r[shomare].y+50>=players_r[i].y:
                    vy=-vy
        for i in range(0,4):
            dis1=( (players_b[i].y-players_r[shomare].y)**2 + (players_b[i].x-players_r[shomare].x)**2 )**0.5
            col1=dis1<=100
            if col1==True and players_r[shomare].x+50>=players_b[i].x:
                vx=-vx
            if col1==True and players_r[shomare].x<=players_b[i].x+50:
                vx=-vx
            if col1==True and players_r[shomare].y<=players_b[i].y+50:
                vy=-vy
            if col1==True and players_r[shomare].y+50>=players_b[i].y:
                vy=-vy
    return(vx,vy,k2,h2)
#تابع برخورد توپ
def barkhord_ball(ball1,tvx,tvy,turn):
    if ball1.tx+50>=1280 or ball1.tx<=0:
        tvx=-tvx
    if ball1.ty<=50 or ball1.ty+50>=720:
        tvy=-tvy
    for i in range(0,4):
        dis=( (players_b[i].y-ball1.ty+25)**2 + (players_b[i].x-ball1.tx+25)**2 )**0.5
        col=dis<=75
        if col==True and players_b[i].x+50>=ball1.tx:
            tvx=-tvx
        if col==True and players_b[i].x<=ball1.tx+25:
            tvx=-tvx
        if col==True and players_b[i].y<=ball1.ty+25:
            tvy=-tvy
        if col==True and players_b[i].y+50>=ball1.ty:
            tvy=-tvy
        dis=( (players_r[i].y-ball1.ty+25)**2 + (players_r[i].x-ball1.tx+25)**2 )**0.5
        col=dis<=75
        if col==True and players_r[i].x+50>=ball1.tx:
            tvx=-tvx
        if col==True and players_r[i].x<=ball1.tx+25:
            tvx=-tvx
        if col==True and players_r[i].y<=ball1.ty+25:
            tvy=-tvy
        if col==True and players_r[i].y+50>=ball1.ty:
            tvy=-tvy
    return(tvx,tvy)
#تابع برخورد توپ و مهره ها
def barkhord_t_m(players_r,players_b,ball1,turn,shomare):
    ad="false"
    if turn=="Player1":
        dis=( (players_b[shomare].y-ball1.ty+25)**2 + (players_b[shomare].x-ball1.tx+25)**2 )**0.5
        col=dis<=75
        if col==True and players_b[shomare].x+50>=ball1.tx:
            ad="true"
        if col==True and players_b[shomare].x<=ball1.tx+25:
            ad="true"
        if col==True and players_b[shomare].y<=ball1.ty+25:
            ad="true"
        if col==True and players_b[shomare].y+50>=ball1.ty:
            ad="true"
    if turn=="Player2":
        dis=( (players_r[shomare].y-ball1.ty+25)**2 + (players_r[shomare].x-ball1.tx+25)**2 )**0.5
        col=dis<=75
        if col==True and players_r[shomare].x+50>=ball1.tx:
            ad="true"
        if col==True and players_r[shomare].x<=ball1.tx+25:
            ad="true"
        if col==True and players_r[shomare].y<=ball1.ty+25:
            ad="true"
        if col==True and players_r[shomare].y+50>=ball1.ty:
            ad="true"
    return(ad)
#تابع گل
def barkhord_g(ball1,goal):
    if ball1.tx<=0 and 290<=ball1.ty<=515:
        goal=1
    if ball1.tx>=1230 and 290<=ball1.ty<=515:
        goal=2
    return goal
#ورودي ها
s=0
flag=0
flag_t=0
flag1_t=0
flag2_t=0
shomare=5
tt=0
lt=0
turn=random.randint(1,2)
clk1=0
jahat=0
if turn==2:
    nobat="Player1"
else:
    nobat="Player2"
goal_real=0
goal_barsa=0
done = False
EZS=0
op=1
logo1=0
tlogo=5
t2=0
lg=0
ttt=0
#وايل اصلي
while EZS==0:
    #لدينگ اسکرين
    while logo1==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
        tlogo=tlogo+1
        disp.fill((0,0,0))
        disp.blit(logo,(240,180))
        if 5<=tlogo<=100 and lg==0:
            pygame.draw.circle(disp,(255,255,255),(677,443),3,0)
            pygame.draw.circle(disp,(255,255,255),(686,443),3,0)
            pygame.draw.circle(disp,(255,255,255),(695,443),3,0)
            logo_font=font.render("Loading",True,(255,255,255))
            disp.blit(logo_font,(590,430))
        if tlogo>50:
            t2=t2+1
            tlogo=0
        if t2>=6:
            lg=1
            logo_font=font.render("Complete",True,(255,255,255))
            disp.blit(logo_font,(590,430))
        if t2>=8:
            logo1=1
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #صفحه اصلي
    while play==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if flag_play==False and 590<=xm<=690 and 335<=ym<=405:
                    play=1
                    flag_play==True
                elif flag_play==False and 600<=xm<=680 and 425<=ym<=475:
                    play=1
                    flag_from=1
                    flag_play==True
        disp.fill((0,0,0))
        disp.blit(ggg,(0,0))
        pygame.draw.rect(disp,(255, 255, 255),(590,335,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(590,335,100,70),5)
        pygame.draw.rect(disp,(255, 255, 255),(600,425,80,50),0)
        pygame.draw.rect(disp,(0, 0, 0),(600,425,80,50),5)
        play_font=font.render("Play",True,(0,0,0))
        from_font=font.render("From",True,(0,0,0))
        disp.blit(from_font,(615,440))
        disp.blit(play_font,(617,360))
        logo_font=font.render("Soccer Iran",True,(255,255,255))
        disp.blit(logo_font,(590,30))
        pygame.display.update()
        pygame.time.Clock().tick(60)
    #صفحه فرام
    while flag_from==1:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if 590<=xm<=690 and 535<=ym<=585:
                    flag_from=2
        disp.fill((39, 41, 43))
        pygame.draw.rect(disp,(255, 255, 255),(590,535,100,50),0)
        pygame.draw.rect(disp,(0, 0, 0),(590,535,100,50),5)
        exit_font=font.render("Exit",True,(0,0,0))
        disp.blit(exit_font,(620,550))
        p_font=font.render("Programmer",True,(156, 149, 149))
        disp.blit(p_font,(580,50))
        a_font=font1.render("Arya Alimadadian",True,(255,255,255))
        disp.blit(a_font,(565,80))
        p_font=font.render("Designer",True,(156, 149, 149))
        disp.blit(p_font,(595,120))
        ar_font=font1.render("Armin Vahabpour",True,(255,255,255))
        disp.blit(ar_font,(565,150))
        c_font=font.render("Calculations",True,(156, 149, 149))
        disp.blit(c_font,(572.5,190))
        art_font=font1.render("Arta Motevalian",True,(255,255,255))
        disp.blit(art_font,(570,220))
        w_font=font.render("With the help of",True,(156, 149, 149))
        disp.blit(w_font,(565,360))
        ary_font=font1.render("Arya Mohammadi",True,(255,255,255))
        disp.blit(ary_font,(570,390))
        w_font=font.render("Allameh Helli3",True,(156, 149, 149))
        disp.blit(w_font,(565,470))
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #صفحه بازي بعد از فرام
    while flag_from==2:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if 590<=xm<=690 and 335<=ym<=405:
                    flag_from=0
        disp.fill((0,0,0))
        disp.blit(ggg,(0,0))
        pygame.draw.rect(disp,(255, 255, 255),(590,335,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(590,335,100,70),5)
        play_font=font.render("Play",True,(0,0,0))
        disp.blit(play_font,(617,360))
        logo_font=font.render("Soccer Iran",True,(255,255,255))
        disp.blit(logo_font,(590,30))
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #صفحه انتخاب زمين
    while p3==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if flag_player3==False and 300<=xm<=600 and 140<=ym<=340:
                    zamin=pygame.image.load("zamin.jpg")
                    zamin=pygame.transform.scale(zamin,(1280,670))
                    p3=zamin
                    flag_player3==True
                elif flag_player3==False and 620<=xm<=920 and 140<=ym<=340:
                    zamin1=pygame.image.load("zamin1.png")
                    zamin1=pygame.transform.scale(zamin1,(1280,670))
                    p3=zamin1
                    flag_player3==True
                elif flag_player3==False and 620<=xm<=920 and 360<=ym<=560:
                    zamin2=pygame.image.load("zamin2.png")
                    zamin2=pygame.transform.scale(zamin2,(1280,670))
                    p3=zamin2
                    flag_player3==True
                elif flag_player3==False and 300<=xm<=600 and 360<=ym<=560:
                    zamin3=pygame.image.load("zamin3.png")
                    zamin3=pygame.transform.scale(zamin3,(1280,670))
                    p3=zamin3
                    flag_player3==True
        disp.fill((255, 255, 255))
        ground_font=font.render("Ground",True,(0,0,0))
        disp.blit(ground_font,(575,15))
        disp.blit(zamin,(300,140))
        disp.blit(zamin1,(620,140))
        disp.blit(zamin2,(620,360))
        disp.blit(zamin3,(300,360))
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #صفحه انتخاب مهره تيم اول
    while p1==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if flag_player1==False and 100<=xm<=200 and 150<=ym<=270:
                    p1=real
                    flag_player1==True
                elif flag_player1==False and 220<=xm<=320 and 150<=ym<=270:
                    p1=barsa
                    flag_player1==True
                elif flag_player1==False and 340<=xm<=440 and 150<=ym<=270:
                    p1=juventus
                    flag_player1==True
                elif flag_player1==False and 100<=xm<=200 and 350<=ym<=470:
                    p1=perspolis
                    flag_player1==True
                elif flag_player1==False and 220<=xm<=320 and 350<=ym<=470:
                    p1=esteghlal
                    flag_player1==True
                elif flag_player1==False and 340<=xm<=440 and 350<=ym<=470:
                    p1=bayern
                    flag_player1==True
        disp.fill((255, 255, 255))
        player1_font=font.render("Player1",True,(0,0,0))
        disp.blit(player1_font,(20,15))
        disp.blit(real,(100,150))
        disp.blit(barsa,(220,150))
        disp.blit(juventus,(340,150))
        disp.blit(perspolis,(100,350))
        disp.blit(esteghlal,(220,350))
        disp.blit(bayern,(340,350))
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #صفحه انتخاب مهره تيم دوم
    while p2==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if flag_player2==False and 860<=xm<=960 and 150<=ym<=270 and p1!=real:
                    p2=real
                    flag_player2==True
                elif flag_player2==False and 980<=xm<=1080 and 150<=ym<=270 and p1!=barsa:
                    p2=barsa
                    flag_player2==True
                elif flag_player2==False and 1100<=xm<=1200 and 150<=ym<=270 and p1!=juventus:
                    p2=juventus
                    flag_player2==True
                elif flag_player2==False and 860<=xm<=960 and 350<=ym<=470 and p1!=perspolis:
                    p2=perspolis
                    flag_player2==True
                elif flag_player2==False and 980<=xm<=1080 and 350<=ym<=470 and p1!=esteghlal:
                    p2=esteghlal
                    flag_player2==True
                elif flag_player2==False and 1100<=xm<=1200 and 350<=ym<=470 and p1!=bayern:
                    p2=bayern
                    flag_player2==True   
        disp.fill((255, 255, 255))
        player2_font=font.render("Player2",True,(0,0,0))
        disp.blit(player2_font,(1180,15))
        if p1!=real:
            disp.blit(real,(860,150))
        if p1!=barsa:
            disp.blit(barsa,(980,150))
        if p1!=juventus:
            disp.blit(juventus,(1100,150))
        if p1!=perspolis:
            disp.blit(perspolis,(860,350))
        if p1!=esteghlal:
            disp.blit(esteghlal,(980,350))
        if p1!=bayern:
            disp.blit(bayern,(1100,350))
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #صفحه انتخاب تعداد گل
    while g_goal==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
                if i.key==pygame.K_UP and t_goal<9:
                    t_goal=t_goal+1
                    rang=(0,255,0)
                if i.key==pygame.K_DOWN and t_goal>1:
                    t_goal=t_goal-1
                    rang=(255,0,0)
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if 600<=xm<=700 and 400<=ym<=470:
                    g_goal=1
        time=time+1
        if time>=500 and gh!=1:
            x_box=x_box-1
        if x_box==860:
            gh=1
            nfont=1
        disp.fill((255, 255, 255))
        disp.blit(up,(625,140))
        disp.blit(down,(625,280))
        pygame.draw.rect(disp,rang,(625,200,50,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(625,200,50,70),5)
        pygame.draw.rect(disp,(148,0,211),(600,400,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(600,400,100,70),5)
        pygame.draw.rect(disp,(218,165,32),(x_box,y_box,400,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(x_box,y_box,400,70),5)
        tgoal_font=font2.render(str(t_goal),True,(0,0,0))
        disp.blit(tgoal_font,(642,224))
        conf_font=font.render("confirm",True,(0,0,0))
        disp.blit(conf_font,(612,425))
        if nfont==1:
            up_font=font.render("press up arrow to increase.",True,(0,0,0))
            disp.blit(up_font,(920,610))
            down_font=font.render("press down arrow to decrease.",True,(0,0,0))
            disp.blit(down_font,(920,640))
        ground_font=font.render("Goal point",True,(0,0,0))
        disp.blit(ground_font,(600,15))
        pygame.display.update()
        pygame.time.Clock().tick(1000)
    #صفحه استارت
    while start==0:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if flag_start==False and 600<=xm<=700 and 400<=ym<=470:
                    start=1
                    flag_start==True
        disp.fill((255,255,255))
        disp.blit(photo,(0,0))
        pygame.draw.rect(disp,(184, 17, 17),(600,400,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(600,400,100,70),5)
        start_font=font.render("Start",True,(0,0,0))
        vs_font=font.render("VS",True,(255,255,255))
        disp.blit(p1,(500,150))
        disp.blit(p2,(700,150))
        point_font=font.render("Goal Point:"+str(t_goal),True,(255,255,255))
        disp.blit(point_font,(592,275))
        disp.blit(start_font,(627,425))
        disp.blit(vs_font,(642,210))
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #وايل بازي اصلي
    while not done:   
        # events
        for k in pygame.event.get():
            if k.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if k.type==pygame.KEYDOWN:
                if k.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if k.type==pygame.MOUSEBUTTONDOWN and flag==0:
                xm,ym=k.pos
                for i in range(0,4):
                    if nobat=="Player1" and players_b[i].x<xm<players_b[i].x+100 and players_b[i].y<ym<players_b[i].y+120 or nobat=="Player2" and players_r[i].x <xm<players_r[i].x+100 and players_r[i].y<ym<players_r[i].y+120:
                        wait_sound.play()
                        s=0
                    #پوزيشن دايره براي بارسا
                    if players_r[i].x<xm<players_r[i].x+100 and players_r[i].y<ym<players_r[i].y+100 and turn%2==0:
                        shomare=i
                        turn+=1
                        nobat="Player2"
                        clk1=1
                        xd=players_r[i].x+50
                        yd=players_r[i].y+50
                        start_line=[xd,yd]
                        s=1
                    #پوزيشن دايره براي مادريد 
                    if players_b[i].x<xm<players_b[i].x+100 and players_b[i].y<ym<players_b[i].y+100 and turn%2==1:
                        shomare=i
                        turn+=1
                        nobat="Player1"
                        clk1=1
                        xd=players_b[i].x+50
                        yd=players_b[i].y+50
                        start_line=[xd,yd]
                        s=1
            if k.type==pygame.MOUSEMOTION and clk1==1:
                xw,yw=k.pos
                if xw-xd<-200:
                    xw=xd-200
                if xw-xd>200:
                    xw=xd+200
                if yw-yd<-200:
                    yw=yd-200
                if yw-yd>200:
                    yw=yd+200
                if yw<=50:
                    yw=50
                end_line=[xw,yw]
                pygame.draw.line(disp,(0,0,0),start_line,end_line,5)
                pygame.display.update()
            if k.type==pygame.MOUSEBUTTONUP and clk1==1:
                xup,yup=k.pos
                flag=1
                if xup>xd:
                    xp=(xd-xup)+xd-50
                if xd>xup:
                    xp=xd-(xup-xd)-50
                if yup<yd:
                    yp=(yd-yup)+yd-50
                if yd<yup:
                    yp=yd-(yup-yd)-50
                clk1=0
                k2=xp-xd
                h2=yp-yd
                if k2<0:
                    k2=-k2
                if h2<0:
                    h2=-h2
                toopx=k2
                toopy=h2
        # updates
        if nobat=="Player2" and flag==1 and flag_t==0:
            to=to+2
            lo=lo+2
            if flag==1 and players_r[shomare].x<xp and flag_t==0:
                players_r[shomare].x=players_r[shomare].x+players_rv[shomare].vx
            if flag==1 and players_r[shomare].y<yp and flag_t==0:
                players_r[shomare].y=players_r[shomare].y+players_rv[shomare].vy
            if flag==1 and players_r[shomare].x>xp and flag_t==0:
                players_r[shomare].x=players_r[shomare].x-players_rv[shomare].vx
            if flag==1 and players_r[shomare].y>yp and flag_t==0:
                players_r[shomare].y=players_r[shomare].y-players_rv[shomare].vy
            players_rv[shomare].vx,players_rv[shomare].vy,k2,h2=barkhord(players_r , players_b,nobat,shomare,players_rv[shomare].vx,players_rv[shomare].vy,k2,h2,player_r_v,player_b_v)
            toop_gg=barkhord_t_m(players_r,players_b,ball1,nobat,shomare)
            if toop_gg=="true":
                flag_t=1
                if to!=k2 or to+1!=k2 or to-1!=k2:
                    if players_r[shomare].x<xp:
                            tvx=2
                    if players_r[shomare].x>xp:
                            tvx=-2
                    if players_r[shomare].x==xp:
                            tvx=0
                if lo!=h2 or lo+1!=h2 or lo-1!=h2:
                    if players_r[shomare].y<yp:
                        tvy=2
                    if players_r[shomare].y>yp:
                        tvy=-2
                    if players_r[shomare].y==yp:
                        tvy=0
            if (to==k2 or to+1==k2 or to-1==k2) and flag_t==0:
                flag1=1
            if (lo==h2 or lo+1==h2 or lo-1==h2) and flag_t==0:
                flag2=1
            if flag==1 and flag1==1 and flag2==1 and flag_t==0: 
                flag=0
                flag1=0
                flag2=0
                flag_t=0
                flag_t1=0
                flag_t2=0
                to=0
                lo=0
                k2=0
                h2=0
                vx_r=2
                vx_b=2
                vy_r=2
                vy_b=2
                tt=0
                lt=0
                toop_gg="false"
                players_rv[0].vx=2
                players_rv[1].vx=2
                players_rv[2].vx=2
                players_rv[3].vx=2
                players_rv[0].vy=2
                players_rv[1].vy=2
                players_rv[2].vy=2
                players_rv[3].vy=2
                players_bv[0].vx=2
                players_bv[1].vx=2
                players_bv[2].vx=2
                players_bv[3].vx=2
                players_bv[0].vy=2
                players_bv[1].vy=2
                players_bv[2].vy=2
                players_bv[3].vy=2
        if flag_t==1 and flag==1:
            txp=ball1.tx+toopx
            typ=ball1.ty+toopy
        if flag_t==1 and flag==1:
            tt=tt+2
            lt=lt+2
            if ball1.tx<txp:
                ball1.tx=ball1.tx+tvx
            if ball1.ty<typ:
                ball1.ty=ball1.ty+tvy
            if ball1.tx>txp:
                ball1.tx=ball1.tx-tvx
            if ball1.ty>typ:
                ball1.ty=ball1.ty-tvy
            tvx,tvy=barkhord_ball(ball1,tvx,tvy,nobat)
            goal=barkhord_g(ball1,goal)
        if goal==1:
            goal_sound.play()
            goal_barsa=goal_barsa+1
            flag=0
            flag1=0
            flag2=0
            flag1_t=0
            flag2_t=0
            flag_t=0
            to=0
            lo=0
            k2=0
            h2=0
            vx_r=2
            vx_b=2
            vy_r=2
            vy_b=2
            toopx=0
            toopy=0
            tt=0
            lt=0
            toop_gg="false"
            players_r[0].x=100
            players_r[1].x=400
            players_r[2].x=290
            players_r[3].x=290
            players_r[0].y=320
            players_r[1].y=320
            players_r[2].y=100
            players_r[3].y=550
            players_b[0].x=1085
            players_b[1].x=775
            players_b[2].x=810
            players_b[3].x=810
            players_b[0].y=320
            players_b[1].y=320
            players_b[2].y=100
            players_b[3].y=550
            ball1.tx=620
            ball1.ty=360
            goal=0
            players_rv[0].vx=2
            players_rv[1].vx=2
            players_rv[2].vx=2
            players_rv[3].vx=2
            players_rv[0].vy=2
            players_rv[1].vy=2
            players_rv[2].vy=2
            players_rv[3].vy=2
            players_bv[0].vx=2
            players_bv[1].vx=2
            players_bv[2].vx=2
            players_bv[3].vx=2
            players_bv[0].vy=2
            players_bv[1].vy=2
            players_bv[2].vy=2
            players_bv[3].vy=2
        if goal==2:
            goal_real=goal_real+1
            goal_sound.play()
            flag=0
            flag1=0
            flag2=0
            flag1_t=0
            flag2_t=0
            flag_t=0
            to=0
            lo=0
            k2=0
            h2=0
            vx_r=2
            vx_b=2
            vy_r=2
            vy_b=2
            toopx=0
            toopy=0
            tt=0
            lt=0
            toop_gg="false"
            players_r[0].x=100
            players_r[1].x=400
            players_r[2].x=290
            players_r[3].x=290
            players_r[0].y=320
            players_r[1].y=320
            players_r[2].y=100
            players_r[3].y=550
            players_b[0].x=1085
            players_b[1].x=775
            players_b[2].x=810
            players_b[3].x=810
            players_b[0].y=320
            players_b[1].y=320
            players_b[2].y=100
            players_b[3].y=550
            ball1.tx=620
            ball1.ty=360
            goal=0
            players_rv[0].vx=2
            players_rv[1].vx=2
            players_rv[2].vx=2
            players_rv[3].vx=2
            players_rv[0].vy=2
            players_rv[1].vy=2
            players_rv[2].vy=2
            players_rv[3].vy=2
            players_bv[0].vx=2
            players_bv[1].vx=2
            players_bv[2].vx=2
            players_bv[3].vx=2
            players_bv[0].vy=2
            players_bv[1].vy=2
            players_bv[2].vy=2
            players_bv[3].vy=2
        if goal_real==t_goal or goal_barsa==t_goal:
            winner=1
            flag=0
            flag1=0
            flag2=0
            flag1_t=0
            flag2_t=0
            flag_t=0
            to=0
            lo=0
            k2=0
            h2=0
            vx_r=2
            vx_b=2
            vy_r=2
            vy_b=2
            toopx=0
            toopy=0
            tt=0
            lt=0
            toop_gg="false"
            players_r[0].x=100
            players_r[1].x=400
            players_r[2].x=290
            players_r[3].x=290
            players_r[0].y=320
            players_r[1].y=320
            players_r[2].y=100
            players_r[3].y=550
            players_b[0].x=1085
            players_b[1].x=775
            players_b[2].x=810
            players_b[3].x=810
            players_b[0].y=320
            players_b[1].y=320
            players_b[2].y=100
            players_b[3].y=550
            ball1.tx=620
            ball1.ty=360
            goal=0
            done=True
            players_rv[0].vx=2
            players_rv[1].vx=2
            players_rv[2].vx=2
            players_rv[3].vx=2
            players_rv[0].vy=2
            players_rv[1].vy=2
            players_rv[2].vy=2
            players_rv[3].vy=2
            players_bv[0].vx=2
            players_bv[1].vx=2
            players_bv[2].vx=2
            players_bv[3].vx=2
            players_bv[0].vy=2
            players_bv[1].vy=2
            players_bv[2].vy=2
            players_bv[3].vy=2
        if (tt==toopx or tt+1==toopx or tt-1==toopx) and flag_t==1 and flag==1:
                flag1_t=1
        if (lt==toopy or lt+1==toopy or lt-1==toopy) and flag_t==1 and flag==1:
                flag2_t=1
        if flag==1 and flag1_t==1 and flag2_t==1 and flag_t==1:
                flag=0
                flag1=0
                flag2=0
                flag1_t=0
                flag2_t=0
                flag_t=0
                to=0
                lo=0
                k2=0
                h2=0
                vx_r=2
                vx_b=2
                vy_r=2
                vy_b=2
                toopx=0
                toopy=0
                tt=0
                lt=0
                toop_gg="false"
                players_rv[0].vx=2
                players_rv[1].vx=2
                players_rv[2].vx=2
                players_rv[3].vx=2
                players_rv[0].vy=2
                players_rv[1].vy=2
                players_rv[2].vy=2
                players_rv[3].vy=2
                players_bv[0].vx=2
                players_bv[1].vx=2
                players_bv[2].vx=2
                players_bv[3].vx=2
                players_bv[0].vy=2
                players_bv[1].vy=2
                players_bv[2].vy=2
                players_bv[3].vy=2
        if nobat=="Player1" and flag==1 and flag_t==0:
            to=to+2
            lo=lo+2
            if flag==1 and players_b[shomare].x<xp and flag_t==0:
                players_b[shomare].x=players_b[shomare].x+players_bv[shomare].vx
            if flag==1 and players_b[shomare].y<yp and flag_t==0:
                players_b[shomare].y=players_b[shomare].y+players_bv[shomare].vy
            if flag==1 and players_b[shomare].x>xp and flag_t==0:
                players_b[shomare].x=players_b[shomare].x-players_bv[shomare].vx
            if flag==1 and players_b[shomare].y>yp and flag_t==0:
                players_b[shomare].y=players_b[shomare].y-players_bv[shomare].vy
            players_bv[shomare].vx,players_bv[shomare].vy,k2,h2=barkhord(players_r , players_b,nobat,shomare,players_bv[shomare].vx,players_bv[shomare].vy,k2,h2,player_r_v,player_b_v)
            toop_gg=barkhord_t_m(players_r,players_b,ball1,nobat,shomare)
            if toop_gg=="true":
                flag_t=1
                if to!=k2 or to+1!=k2 or to-1!=k2:
                    if players_b[shomare].x<xp:
                        tvx=2
                    if players_b[shomare].x>xp:
                        tvx=-2
                    if players_b[shomare].x==xp:
                        tvx=0
                if lo!=h2 or lo+1!=h2 or lo-1!=h2:
                    if players_b[shomare].y<yp:
                        tvy=2
                    if players_b[shomare].y>yp:
                        tvy=-2
                    if players_b[shomare].y==yp:
                        tvy=0
            if (to==k2 or to+1==k2 or to-1==k2) and flag_t==0:
                flag1=1
            if (lo==h2 or lo+1==h2 or lo-1==h2) and flag_t==0:
                flag2=1
            if flag==1 and flag1==1 and flag2==1 and flag_t==0: 
                flag=0
                flag1=0
                flag2=0
                flag_t=0
                flag_t1=0
                flag_t2=0
                to=0
                lo=0
                k2=0
                h2=0
                vx_r=2
                vx_b=2
                vy_r=2
                vy_b=2
                tt=0
                lt=0
                toop_gg="false"
                players_rv[0].vx=2
                players_rv[1].vx=2
                players_rv[2].vx=2
                players_rv[3].vx=2
                players_rv[0].vy=2
                players_rv[1].vy=2
                players_rv[2].vy=2
                players_rv[3].vy=2
                players_bv[0].vx=2
                players_bv[1].vx=2
                players_bv[2].vx=2
                players_bv[3].vx=2
                players_bv[0].vy=2
                players_bv[1].vy=2
                players_bv[2].vy=2
                players_bv[3].vy=2
        if flag_t==1 and flag==1:
            txp=ball1.tx+toopx
            typ=ball1.ty+toopy
        if flag_t==1 and flag==1:
            tt=tt+2
            lt=lt+2
            if ball1.tx<txp:
                ball1.tx=ball1.tx+tvx
            if ball1.ty<typ:
                ball1.ty=ball1.ty+tvy
            if ball1.tx>txp:
                ball1.tx=ball1.tx-tvx
            if ball1.ty>typ:
                ball1.ty=ball1.ty-tvy
            tvx,tvy=barkhord_ball(ball1,tvx,tvy,nobat)
            goal=barkhord_g(ball1,goal)
        if goal==1:
            goal_barsa=goal_barsa+1
            goal_sound.play()
            flag=0
            flag1=0
            flag2=0
            flag1_t=0
            flag2_t=0
            flag_t=0
            to=0
            lo=0
            k2=0
            h2=0
            vx_r=2
            vx_b=2
            vy_r=2
            vy_b=2
            toopx=0
            toopy=0
            tt=0
            lt=0
            toop_gg="false"
            players_r[0].x=100
            players_r[1].x=400
            players_r[2].x=290
            players_r[3].x=290
            players_r[0].y=320
            players_r[1].y=320
            players_r[2].y=100
            players_r[3].y=550
            players_b[0].x=1085
            players_b[1].x=775
            players_b[2].x=810
            players_b[3].x=810
            players_b[0].y=320
            players_b[1].y=320
            players_b[2].y=100
            players_b[3].y=550
            ball1.tx=620
            ball1.ty=360
            goal=0
            players_rv[0].vx=2
            players_rv[1].vx=2
            players_rv[2].vx=2
            players_rv[3].vx=2
            players_rv[0].vy=2
            players_rv[1].vy=2
            players_rv[2].vy=2
            players_rv[3].vy=2
            players_bv[0].vx=2
            players_bv[1].vx=2
            players_bv[2].vx=2
            players_bv[3].vx=2
            players_bv[0].vy=2
            players_bv[1].vy=2
            players_bv[2].vy=2
            players_bv[3].vy=2
        if goal==2:
            goal_real=goal_real+1
            goal_sound.play()
            flag=0
            flag1=0
            flag2=0
            flag1_t=0
            flag2_t=0
            flag_t=0
            to=0
            lo=0
            k2=0
            h2=0
            vx_r=2
            vx_b=2
            vy_r=2
            vy_b=2
            toopx=0
            toopy=0
            tt=0
            lt=0
            toop_gg="false"
            players_r[0].x=100
            players_r[1].x=400
            players_r[2].x=290
            players_r[3].x=290
            players_r[0].y=320
            players_r[1].y=320
            players_r[2].y=100
            players_r[3].y=550
            players_b[0].x=1085
            players_b[1].x=775
            players_b[2].x=810
            players_b[3].x=810
            players_b[0].y=320
            players_b[1].y=320
            players_b[2].y=100
            players_b[3].y=550
            ball1.tx=620
            ball1.ty=360
            goal=0
            players_rv[0].vx=2
            players_rv[1].vx=2
            players_rv[2].vx=2
            players_rv[3].vx=2
            players_rv[0].vy=2
            players_rv[1].vy=2
            players_rv[2].vy=2
            players_rv[3].vy=2
            players_bv[0].vx=2
            players_bv[1].vx=2
            players_bv[2].vx=2
            players_bv[3].vx=2
            players_bv[0].vy=2
            players_bv[1].vy=2
            players_bv[2].vy=2
            players_bv[3].vy=2
        if goal_real==t_goal or goal_barsa==t_goal:
            winner=1
            flag=0
            flag1=0
            flag2=0
            flag1_t=0
            flag2_t=0
            flag_t=0
            to=0
            lo=0
            k2=0
            h2=0
            vx_r=2
            vx_b=2
            vy_r=2
            vy_b=2
            toopx=0
            toopy=0
            tt=0
            lt=0
            toop_gg="false"
            players_r[0].x=100
            players_r[1].x=400
            players_r[2].x=290
            players_r[3].x=290
            players_r[0].y=320
            players_r[1].y=320
            players_r[2].y=100
            players_r[3].y=550
            players_b[0].x=1085
            players_b[1].x=775
            players_b[2].x=810
            players_b[3].x=810
            players_b[0].y=320
            players_b[1].y=320
            players_b[2].y=100
            players_b[3].y=550
            ball1.tx=620
            ball1.ty=360
            goal=0
            done=True
            players_rv[0].vx=2
            players_rv[1].vx=2
            players_rv[2].vx=2
            players_rv[3].vx=2
            players_rv[0].vy=2
            players_rv[1].vy=2
            players_rv[2].vy=2
            players_rv[3].vy=2
            players_bv[0].vx=2
            players_bv[1].vx=2
            players_bv[2].vx=2
            players_bv[3].vx=2
            players_bv[0].vy=2
            players_bv[1].vy=2
            players_bv[2].vy=2
            players_bv[3].vy=2
        if (tt==toopx or tt+1==toopx or tt-1==toopx) and flag_t==1 and flag==1:
                flag1_t=1
        if (lt==toopy or lt+1==toopy or lt-1==toopy) and flag_t==1 and flag==1:
                flag2_t=1
        if flag==1 and flag1_t==1 and flag2_t==1 and flag_t==1:
                flag=0
                flag1=0
                flag2=0
                flag_t=0
                flag1_t=0
                flag2_t=0
                to=0
                lo=0
                k2=0
                h2=0
                vx_r=2
                vx_b=2
                vy_r=2
                vy_b=2
                toopx=0
                toopy=0
                tt=0
                lt=0
                toop_gg="false"
                players_rv[0].vx=2
                players_rv[1].vx=2
                players_rv[2].vx=2
                players_rv[3].vx=2
                players_rv[0].vy=2
                players_rv[1].vy=2
                players_rv[2].vy=2
                players_rv[3].vy=2
                players_bv[0].vx=2
                players_bv[1].vx=2
                players_bv[2].vx=2
                players_bv[3].vx=2
                players_bv[0].vy=2
                players_bv[1].vy=2
                players_bv[2].vy=2
                players_bv[3].vy=2
        nobat_ki=font.render("It's "+str(nobat)+" turn",True,(0,0,0))
        t_real=font.render("Player1 : "+str(goal_real),True,(0,0,0))
        t_barsa=font.render("Player2 : "+str(goal_barsa),True,(0,0,0))
        # draws
        disp.fill((255,255,255))
        disp.blit(p3,(0,50))
        for i in range(0,4):
            disp.blit(p1,(players_r[i].x,players_r[i].y))
            disp.blit(p2,(players_b[i].x,players_b[i].y))
            #کدام مهره
            if shomare==i and turn%2==1:
                pygame.draw.circle(disp,(0,0,0),(players_r[i].x+50,players_r[i].y+50),50,2)
            if shomare==i and turn%2==0:
                pygame.draw.circle(disp,(0,0,0),(players_b[i].x+50,players_b[i].y+50),50,2)
        #کشيدن توپ
        disp.blit(toop,(ball1.tx,ball1.ty))
        #کشيدن نوشته ها
        disp.blit(nobat_ki,(550,15))
        disp.blit(t_real,(20,15))
        disp.blit(t_barsa,(1160,15))
        #کشيدن مستطيل
        pygame.draw.rect(disp,(0,0,0),(0,0,1280,50),5)
        #پايان
        pygame.display.update()
        pygame.time.Clock().tick(120)
    #وايل برنده
    while winner==1:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_END:
                    pygame.quit()
                    sys.exit()
            if i.type==pygame.MOUSEBUTTONDOWN:
                xm,ym=i.pos
                if 590<=xm<=690 and 435<=ym<=505:
                    pygame.quit()
                if 590<=xm<=690 and 535<=ym<=605:
                    play=0
                    flag_from=0
                    p1=0
                    p2=0
                    p3=0
                    g_goal=0
                    start=0
                    done=False
                    winner=0
                    zamin=pygame.transform.scale(zamin,(300,200))
                    zamin1=pygame.transform.scale(zamin1,(300,200))
                    zamin2=pygame.transform.scale(zamin2,(300,200))
                    zamin3=pygame.transform.scale(zamin3,(300,200))
                    photo=pygame.transform.scale(photo,(1280,750))
                    up=pygame.transform.scale(up,(50,50))
                    down=pygame.transform.scale(down,(50,50))
                    ggg=pygame.transform.scale(ggg,(1280,750))
                    real=pygame.transform.scale(real,(100,100))
                    barsa=pygame.transform.scale(barsa,(100,100))
                    juventus=pygame.transform.scale(juventus,(100,100))
                    bayern=pygame.transform.scale(bayern,(100,100))
                    perspolis=pygame.transform.scale(perspolis,(100,100))
                    esteghlal=pygame.transform.scale(esteghlal,(100,100))
                    toop=pygame.transform.scale(toop,(50,50))
                    flag_player1=False
                    flag_player2=False
                    flag_player3=False
                    flag_play=False
                    flag_start=False
                    flag_from=0
                    play=0
                    start=0
                    p1=0
                    p2=0
                    p3=0
                    t_goal=1
                    g_goal=0
                    gh=0
                    nfont=0
                    x_box=1300
                    y_box=600
                    time=0
                    rang=(255,255,255)
                    s=0
                    flag=0
                    flag_t=0
                    flag1_t=0
                    flag2_t=0
                    shomare=5
                    tt=0
                    lt=0
                    turn=random.randint(1,2)
                    clk1=0
                    jahat=0
                    if turn==2:
                        nobat="Player1"
                    else:
                        nobat="Player2"
                    goal_real=0
                    goal_barsa=0
                    done = False
                    vx_r=2
                    vy_r=2
                    vx_b=2
                    vy_b=2
                    to=0
                    lo=0
                    flag1=0
                    flag2=0
                    goal=0
                    tvx=0
                    tvy=0
                    toopx=0
                    toopy=0
                    winner=0
                    toop_gg="false"
                    players_r[0].x=100
                    players_r[1].x=400
                    players_r[2].x=290
                    players_r[3].x=290
                    players_r[0].y=320
                    players_r[1].y=320
                    players_r[2].y=100
                    players_r[3].y=550
                    players_b[0].x=1085
                    players_b[1].x=775
                    players_b[2].x=810
                    players_b[3].x=810
                    players_b[0].y=320
                    players_b[1].y=320
                    players_b[2].y=100
                    players_b[3].y=550
                    ball1.tx=620
                    ball1.ty=360
                    players_rv[0].vx=2
                    players_rv[1].vx=2
                    players_rv[2].vx=2
                    players_rv[3].vx=2
                    players_rv[0].vy=2
                    players_rv[1].vy=2
                    players_rv[2].vy=2
                    players_rv[3].vy=2
                    players_bv[0].vx=2
                    players_bv[1].vx=2
                    players_bv[2].vx=2
                    players_bv[3].vx=2
                    players_bv[0].vy=2
                    players_bv[1].vy=2
                    players_bv[2].vy=2
                    players_bv[3].vy=2
        disp.fill((66, 245, 117))
        pygame.draw.rect(disp,(255, 255, 255),(590,435,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(590,435,100,70),5)
        pygame.draw.rect(disp,(255, 255, 255),(590,535,100,70),0)
        pygame.draw.rect(disp,(0, 0, 0),(590,535,100,70),5)
        if goal_barsa==t_goal:
            barsa_font=font.render("player2 is the winner.",True,(0,0,0))
            disp.blit(barsa_font,(540,210))
        if goal_real==t_goal:
            real_font=font.render("player1 is the winner.",True,(0,0,0))
            disp.blit(real_font,(540,210))
        play_font=font.render("Exit",True,(0,0,0))
        disp.blit(play_font,(620,460))
        play_font=font.render("Restart",True,(0,0,0))
        disp.blit(play_font,(605,560))
        pygame.display.update()
        pygame.time.Clock().tick(1000)
