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
player1_x=[40,300,190,190]
player2_x=[860,600,710,710]
player1_y=[340,340,120,570]
player2_y=[340,340,120,570]
toop_x=480
toop_y=380
v_toop_x=2
v_toop_y=5
v_player1_x=[0,0,0,0]
v_player2_x=[0,0,0,0]
v_player1_y=[0,0,0,0]
v_player2_y=[0,0,0,0]
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

#تابع برخورد
def  barkhord(player1_x , player2_x , player1_y , player2_y , toop_x , toop_y , v_toop_x , v_toop_y):
    for i in range(0,4):
        if (player1_x[i] < toop_x < player1_x[i] - 100 and player1_y[i] < toop_y < player1_y[i] - 120) or (player2_x[i] < toop_x < player2_x[i] + 100 and player2_y[i] < toop_y < player2_y[i] + 120) or (toop_y == 50) or (toop_y == 600) or (toop_x == 0) or (toop_x == 960):
            v_toop_x = - v_toop_x
            v_toop_y = - v_toop_y
    return(v_toop_x,v_toop_y)
#ورودي ها
shomare=5
turn=random.randint(1,2)
clk1=0
if turn==2:
    nobat="Real madrid"
else:
    nobat="Barcelona"
goal_real=0
goal_barsa=0
done = False
while not done:
    # events
    for k in pygame.event.get():
        if k.type==pygame.QUIT:
            done=True
        if k.type==pygame.KEYDOWN:
            if k.key==pygame.K_END:
                done=True
        if k.type==pygame.MOUSEBUTTONDOWN:
            xm,ym=k.pos
            for i in range(0,4):
                if nobat=="Real madrid" and player2_x[i]<xm<player2_x[i]+100 and player2_y[i]<ym<player2_y[i]+120 or nobat=="Barcelona" and player1_x[i]<xm<player1_x[i]+100 and player1_y[i]<ym<player1_y[i]+120:
                    wait_sound.play()
                #پوزيشن دايره براي بارسا
                if player1_x[i]<xm<player1_x[i]+100 and player1_y[i]<ym<player1_y[i]+120 and turn%2==0:
                    shomare=i
                    turn+=1
                    nobat="Barcelona"
                    clk1=1
                    start_line=[xm,ym]
                #پوزيشن دايره براي مادريد 
                if player2_x[i]<xm<player2_x[i]+100 and player2_y[i]<ym<player2_y[i]+120 and turn%2==1:
                    shomare=i
                    turn+=1
                    nobat="Real madrid"
                    clk1=1
                    start_line=[xm,ym]
        if k.type==pygame.MOUSEMOTION and clk1==1:
            xw,yw=k.pos
            end_line=[xw,yw]
            pygame.draw.line(disp,(0,0,0),start_line,end_line,2)
            pygame.display.update()
        if k.type==pygame.MOUSEBUTTONUP:
            #power=((start_line[0]-end_line[0])**2+(start_line[1]-end_line[1])**2)**0.5
            clk1=0
    # updates
    toop_x=toop_x+v_toop_x
    toop_y=toop_y+v_toop_y
    (v_toop_x,v_toop_y)=barkhord(player1_x , player2_x , player1_y , player2_y , toop_x , toop_y , v_toop_x , v_toop_y)
    nobat_ki=font.render("It's "+str(nobat)+" turn",True,(0,0,0))
    t_real=font.render("Real madrid : "+str(goal_real),True,(0,0,0))
    t_barsa=font.render("Barcelona : "+str(goal_barsa),True,(0,0,0))
    # draws
    disp.fill((255,255,255))
    disp.blit(zamin,(0,50))
    for i in range(0,4):
        #کشيدن مهره ها
        disp.blit(real,(player1_x[i],player1_y[i]))
        disp.blit(barsa,(player2_x[i],player2_y[i]))
        #کدام مهره
        if shomare==i and turn%2==1:
            pygame.draw.circle(disp,(0,0,0),(player1_x[i]+50,player1_y[i]+60),53,2)
        if shomare==i and turn%2==0:
            pygame.draw.circle(disp,(0,0,0),(player2_x[i]+50,player2_y[i]+60),53,2)
    #کشيدن توپ
    disp.blit(toop,(toop_x,toop_y))
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
