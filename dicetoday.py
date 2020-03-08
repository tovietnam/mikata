import math
import tkinter as tk
import time

#ウィンドウ、キャンバス作成
win = tk.Tk()
cv = tk.Canvas(win, width = 600, height = 600,background="black")
cv.pack()

cv.create_text(300,200,
fill="white",font=("MS ゴシック",150),text="見方")

win.update()
time.sleep(9)

cv.delete("all")

cv['bg'] = "blue" 


def draw_line_around(gx,gy):
    ax=gx
    ay=gy-h
    bx=gx+(h/2)*s3
    by=gy-(h/2)
    cx=gx+(h/2)*s3
    cy=gy+(h/2)
    dx=gx
    dy=gy+h
    ex=gx-(h/2)*s3
    ey=gy+(h/2)
    fx=gx-(h/2)*s3
    fy=gy-(h/2)
    
    cv.create_line(ax,ay,bx,by,cx,cy,dx,dy,ex,ey,fx,fy,ax,ay,
    fill="white",width=3.0,tag="poly")


def draw_color(gx,gy,what):
    ax=gx
    ay=gy-h
    bx=gx+(h/2)*s3
    by=gy-(h/2)
    cx=gx+(h/2)*s3
    cy=gy+(h/2)
    dx=gx
    dy=gy+h
    ex=gx-(h/2)*s3
    ey=gy+(h/2)
    fx=gx-(h/2)*s3
    fy=gy-(h/2)

    cv.create_polygon(ax,ay,bx,by,cx,cy,dx,dy,ex,ey,fx,fy,ax,ay,
    fill=what,width=3.0,tag="iro")

def draw_c3(gx,gy):
    ax=gx
    ay=gy-h
    bx=gx+(h/2)*s3
    by=gy-(h/2)
    cx=gx+(h/2)*s3
    cy=gy+(h/2)
    dx=gx
    dy=gy+h
    ex=gx-(h/2)*s3
    ey=gy+(h/2)
    fx=gx-(h/2)*s3
    fy=gy-(h/2)

    #左面
    cv.create_polygon(fx,fy,gx,gy,dx,dy,ex,ey,
    fill="green3",width=3.0,tag="poly1")
    
    #右面
    cv.create_polygon(gx,gy,bx,by,cx,cy,dx,dy,
    fill="light pink",width=3.0,tag="poly2")
   
    #上面
    cv.create_polygon(ax,ay,bx,by,gx,gy,fx,fy,
    fill="white",width=3.0,tag="poly3")
    
def draw_ue(gx,gy,what):
    ax=gx
    ay=gy-h
    bx=gx+(h/2)*s3
    by=gy-(h/2)
    fx=gx-(h/2)*s3
    fy=gy-(h/2)
    #上面
    cv.create_polygon(ax,ay,bx,by,gx,gy,fx,fy,
    fill=what,width=3.0,tag="poly")
    
def draw_left(gx,gy,what):
    dx=gx
    dy=gy+h
    ex=gx-(h/2)*s3
    ey=gy+(h/2)
    fx=gx-(h/2)*s3
    fy=gy-(h/2)
    #左面
    cv.create_polygon(fx,fy,gx,gy,dx,dy,ex,ey,
    fill=what,width=3.0,tag="poly")
   
def draw_right(gx,gy,what):  
    bx=gx+(h/2)*s3
    by=gy-(h/2)
    cx=gx+(h/2)*s3
    cy=gy+(h/2)
    dx=gx
    dy=gy+h
    #右面
    cv.create_polygon(gx,gy,bx,by,cx,cy,dx,dy,
    fill=what,width=3.0,tag="poly")
   
def draw_11(gx,gy):
    gx=gx
    gy=gy-(h/2)
    
    cv.create_oval(gx+(h/10)*s3,gy+h/10,gx-(h/10)*s3,gy-h/10,
    outline="red",fill="red",width=3.0,tag="one")

def draw_onel(gx,gy):
    gx=gx-(h/4)*s3
    gy=gy+(h/4)
    
    cv.create_oval(gx+(h/8),gy+h/8,gx-(h/8),gy-h/8,
    outline="red",fill="red",width=3.0,tag="one")

def draw_oner(gx,gy):
    gx=gx+h*s3+(h/4)*s3
    gy=gy+(h/4)
    
    cv.create_oval(gx+(h/8),gy+h/8,gx-(h/8),gy-h/8,
    outline="red",fill="red",width=3.0,tag="one")

def draw_oner2(gx,gy):
    gx=gx-(h/2)*s3+(h/4)*s3
    gy=gy-3*(h/2)+(h/4)
    
    cv.create_oval(gx+(h/8),gy+h/8,gx-(h/8),gy-h/8,
    outline="red",fill="red",width=3.0,tag="one")

def draw_21(gx,gy):
    gx1=gx
    gy1=gy-(h/3)

    gx2=gx
    gy2=gy-2*(h/3)
    
    cv.create_oval(gx1+(h/16)*s3,gy1+h/16,gx1-(h/16)*s3,gy1-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*s3,gy2+h/16,gx2-(h/16)*s3,gy2-h/16,
    outline="black",fill="black",width=3.0)

#上段の右
def draw_13(gx,gy):
    gx1=gx+2*(h/3)
    gy1=gy-3*h

    gx2=gx+(h/3)
    gy2=gy-3*h+(h/2)
    
    cv.create_oval(gx1+(h/16)*(7/5),gy1+(h/16)*(7/5),gx1-(h/16)*(7/5),gy1-(h/16)*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

def draw_twor2(gx,gy):
    
    gx1=gx-h*s3+3*(h/8)*s3
    gy1=gy+h-(1.5*h/8)*s3*s3 

    gx2=gx-h*s3+(h/8)*s3 
    gy2=gy+h-(2.5*(h/8))*s3*s3

    cv.create_oval(gx1+(h/16)*(7/5),gy1+(h/16)*(7/5),gx1-(h/16)*(7/5),gy1-(h/16)*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

def draw_twol(gx,gy):
    gx1=gx+(h/2)*s3-2*(h/3)
    gy1=gy-(3/2)*h

    gx2=gx+(h/2)*s3-(h/3)
    gy2=gy-(3/2)*h+(h/2)

    cv.create_oval(gx1+(h/16)*(7/5),gy1+(h/16)*(7/5),gx1-(h/16)*(7/5),gy1-(h/16)*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

def draw_31(gx,gy):
  
    gx2=gx+(h/4)*s3
    gy2=gy-2*(h/4)

    gx3=gx
    gy3=gy-2*(h/4)

    gx4=gx-(h/4)*s3
    gy4=gy-2*(h/4)

    cv.create_oval(gx2+(h/16)*s3,gy2+h/16,gx2-(h/16)*s3,gy2-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*s3,gy3+h/16,gx3-(h/16)*s3,gy3-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx4+(h/16)*s3,gy4+h/16,gx4-(h/16)*s3,gy4-h/16,
    outline="black",fill="black",width=3.0)

def draw_12(gx,gy):
    gx1=gx-(h/8)*s3
    gy1=gy-2*h-(h/8)*s3*s3
    gx2=gx-(h/4)*s3
    gy2=gy-2*h-(h/4)*s3*s3
    gx3=gx-3*(h/8)*s3
    gy3=gy-2*h-3*(h/8)*s3*s3  
    
    cv.create_oval(gx1+(h/16)*(7/5),gy1+h/16*(7/5),gx1-(h/16)*(7/5),gy1-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*(7/5),gy3+h/16*(7/5),gx3-(h/16)*(7/5),gy3-h/16*(7/5),
    outline="black",fill="black",width=3.0)
 
def draw_sanl2(gx,gy):
    gx1=gx-(h/2)*s3 -(h/8)*s3
    gy1=gy-h -3*(h/8)
    gx2=gx-(h/2)*s3 -(h/4)*s3
    gy2=gy-h -(h/4)
    gx3=gx-(h/2)*s3 -3*(h/8)*s3
    gy3=gy-h -(h/8)
    
    cv.create_oval(gx1+(h/16)*(6/5),gy1+h/16*(6/5),gx1-(h/16)*(6/5),gy1-h/16*(6/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(6/5),gy2+h/16*(6/5),gx2-(h/16)*(6/5),gy2-h/16*(6/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*(6/5),gy3+h/16*(6/5),gx3-(h/16)*(6/5),gy3-h/16*(6/5),
    outline="black",fill="black",width=3.0)

def draw_26(gx,gy):
    gx1=gx+(h/2)*s3+(h/8)*s3
    gy1=gy-(h/2)-(h/8)*s3*s3
    gx2=gx+(h/2)*s3+(h/4)*s3
    gy2=gy-(h/2)-(h/4)*s3*s3
    gx3=gx+(h/2)*s3+3*(h/8)*s3
    gy3=gy-(h/2)-3*(h/8)*s3*s3  
    
    cv.create_oval(gx1+(h/16)*(7/5),gy1+h/16*(7/5),gx1-(h/16)*(7/5),gy1-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*(7/5),gy3+h/16*(7/5),gx3-(h/16)*(7/5),gy3-h/16*(7/5),
    outline="black",fill="black",width=3.0)
     
def draw_34(gx,gy):
    gx1=gx
    gy1=gy-(h/4)

    gx2=gx+(h/4)*s3
    gy2=gy-2*(h/4)

    gx3=gx-(h/4)*s3
    gy3=gy-2*(h/4)

    gx4=gx
    gy4=gy-3*(h/4)
    
    cv.create_oval(gx1+(h/16)*s3,gy1+h/16,gx1-(h/16)*s3,gy1-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*s3,gy2+h/16,gx2-(h/16)*s3,gy2-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*s3,gy3+h/16,gx3-(h/16)*s3,gy3-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx4+(h/16)*s3,gy4+h/16,gx4-(h/16)*s3,gy4-h/16,
    outline="black",fill="black",width=3.0)

def draw_fourl(gx,gy):
    #右下
    gx1=gx+h*s3-(h/8)*s3
    gy1=gy+h-(h/8)*s3*s3
    #右上
    gx2=gx+h*s3-(h/8)*s3
    gy2=gy+h-3*(h/8)*s3*s3+(h/4)
    
    gx3=gx+h*s3-3*(h/8)*s3
    gy3=gy+h-3*(h/8)*s3*s3  

    gx4=gx+h*s3-3*(h/8)*s3
    gy4=gy+h-(h/8)*s3*s3-(h/4)
    
    cv.create_oval(gx1+(h/16)*(7/5),gy1+h/16*(7/5),gx1-(h/16)*(7/5),gy1-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*(7/5),gy3+h/16*(7/5),gx3-(h/16)*(7/5),gy3-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx4+(h/16)*(7/5),gy4+h/16*(7/5),gx4-(h/16)*(7/5),gy4-h/16*(7/5),
    outline="black",fill="black",width=3.0)

def draw_37(gx,gy):
    gx1=gx
    gy1=gy-(h/4)

    gx2=gx+(h/4)*s3
    gy2=gy-2*(h/4)

    gx3=gx
    gy3=gy-2*(h/4)

    gx4=gx-(h/4)*s3
    gy4=gy-2*(h/4)

    gx5=gx
    gy5=gy-3*(h/4)
    
    cv.create_oval(gx1+(h/16)*s3,gy1+h/16,gx1-(h/16)*s3,gy1-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*s3,gy2+h/16,gx2-(h/16)*s3,gy2-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*s3,gy3+h/16,gx3-(h/16)*s3,gy3-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx4+(h/16)*s3,gy4+h/16,gx4-(h/16)*s3,gy4-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx5+(h/16)*s3,gy5+h/16,gx5-(h/16)*s3,gy5-h/16,
    outline="black",fill="black",width=3.0)

def draw_36(gx,gy):
    gx1=gx+2*(h/3)
    gy1=gy

    gx2=gx+(h/3)
    gy2=gy+(h/2)
    
    cv.create_oval(gx1+(h/16)*(7/5),gy1+(h/16)*(7/5),gx1-(h/16)*(7/5),gy1-(h/16)*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

def draw_24(gx,gy):
    gx1=gx
    gy1=gy-(h/4)
    gx2=gx+(h/4)*s3
    gy2=gy-2*(h/4)
    gx3=gx-(h/4)*s3
    gy3=gy-2*(h/4)
    gx4=gx
    gy4=gy-3*(h/4)
    gx5=gx+(h/8)*s3
    gy5=gy-(h/8)*3
    gx6=gx-(h/8)*s3
    gy6=gy-(h/8)*5
    
    cv.create_oval(gx1+(h/16)*s3,gy1+h/16,gx1-(h/16)*s3,gy1-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*s3,gy2+h/16,gx2-(h/16)*s3,gy2-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*s3,gy3+h/16,gx3-(h/16)*s3,gy3-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx4+(h/16)*s3,gy4+h/16,gx4-(h/16)*s3,gy4-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx5+(h/16)*s3,gy5+h/16,gx5-(h/16)*s3,gy5-h/16,
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx6+(h/16)*s3,gy6+h/16,gx6-(h/16)*s3,gy6-h/16,
    outline="black",fill="black",width=3.0)

def draw_sixl(gx,gy):
    #右下
    gx1=gx-(h/8)*s3
    gy1=gy-(h/8)*s3*s3
    
    #右中
    gx6=gx-(h/8)*s3
    gy6=gy-2*(h/8)*s3*s3+(h/8)
    
    #右上
    gx2=gx-(h/8)*s3
    gy2=gy-3*(h/8)*s3*s3+(h/4)
    
    #左上
    gx3=gx-3*(h/8)*s3
    gy3=gy-3*(h/8)*s3*s3 

    #左中
    gx5=gx-3*(h/8)*s3
    gy5=gy-2*(h/8)*s3*s3-(h/8)
    
    #左下
    gx4=gx-3*(h/8)*s3
    gy4=gy-(h/8)*s3*s3-(h/4)
    
    cv.create_oval(gx1+(h/16)*(7/5),gy1+h/16*(7/5),gx1-(h/16)*(7/5),gy1-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx2+(h/16)*(7/5),gy2+h/16*(7/5),gx2-(h/16)*(7/5),gy2-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx3+(h/16)*(7/5),gy3+h/16*(7/5),gx3-(h/16)*(7/5),gy3-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx4+(h/16)*(7/5),gy4+h/16*(7/5),gx4-(h/16)*(7/5),gy4-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx5+(h/16)*(7/5),gy5+h/16*(7/5),gx5-(h/16)*(7/5),gy5-h/16*(7/5),
    outline="black",fill="black",width=3.0)

    cv.create_oval(gx6+(h/16)*(7/5),gy6+h/16*(7/5),gx6-(h/16)*(7/5),gy6-h/16*(7/5),
    outline="black",fill="black",width=3.0)

#六角形内の三本線
def draw_line(gx,gy):
    ax=gx
    ay=gy-h

    bx=gx+(h/2)*s3
    by=gy-(h/2)

    cx=gx+(h/2)*s3
    cy=gy+(h/2)

    dx=gx
    dy=gy+h

    ex=gx-(h/2)*s3
    ey=gy+(h/2)

    fx=gx-(h/2)*s3
    fy=gy-(h/2)

    cv.create_line(fx,fy,gx,gy,fill="white",width=3.0,tag="line")
    cv.create_line(bx,by,gx,gy,fill="white",width=3.0,tag="line")
    cv.create_line(dx,dy,gx,gy,fill="white",width=3.0,tag="line")

    win.update()
    time.sleep(0.3)

#中央の三本線
def draw_line_center(gx,gy):
    cv.create_line(gx,gy-2*h,gx,gy-h,fill="white",width=3.0,tag="line")
    cv.create_line(gx-(h/2)*s3,gy-(h/2),gx,gy-h,fill="white",width=3.0,tag="line")
    cv.create_line(gx+(h/2)*s3,gy-(h/2),gx,gy-h,fill="white",width=3.0,tag="line")

    win.update()
    time.sleep(0.3)

#原点・一辺の長さを定義
gx=300
gy=450
h=100
s3=math.sqrt(3)

l=[[gx,gy-3*h],[gx-(h/2)*s3,gy-(3/2)*h],[gx-h*s3,gy],[gx,gy],[gx+h*s3,gy],[gx+(h/2)*s3,gy-(3/2)*h]]
c=["red","yellow","green","orange red","gold","forest green"]
c2=["green","orange red","gold","forest green","red","yellow"]
c3=["gold","forest green","red","yellow","green","orange red"]


#ここから動き
#輪郭の線
for i in range(6):
    draw_line_around(l[i][0],l[i][1])
    win.update()
    time.sleep(0.3)

#六角形ごとの塗分け
for i in range(6):
    draw_color(l[i][0],l[i][1],c[i])
    win.update()
    time.sleep(0.3)

win.update()
time.sleep(0.5)

cv.delete("iro")

win.update()
time.sleep(0.3)

#六角形ごとの塗分け2回目
for i in range(6):
    draw_color(l[i][0],l[i][1],c2[i])

win.update()
time.sleep(0.5)

cv.delete("iro")

win.update()
time.sleep(0.5)

#六角形ごとの塗分け3回目
for i in range(6):
    draw_color(l[i][0],l[i][1],c3[i])

win.update()
time.sleep(0.5)

cv.delete("iro")

win.update()
time.sleep(1)

#真ん中一色塗
draw_color(gx,gy-h,"green")

win.update()
time.sleep(0.5)

#中心六角形の周囲
#下パート
draw_left(gx,gy,"light pink")
draw_right(gx,gy,"light pink")
#右パート
draw_ue(gx+(h/2)*s3,gy-3*(h/2),"light pink")
draw_right(gx+(h/2)*s3,gy-3*(h/2),"light pink")
#左パート
draw_ue(gx-(h/2)*s3,gy-3*(h/2),"light pink")
draw_left(gx-(h/2)*s3,gy-3*(h/2),"light pink")

win.update()
time.sleep(0.5)

#外側三つの羽根
#下パート
draw_left(gx,gy-3*h,"DarkOrange1")
draw_right(gx,gy-3*h,"DarkOrange1")
#右パート
draw_ue(gx-h*s3,gy,"DarkOrange1")
draw_right(gx-h*s3,gy,"DarkOrange1")
#左パート
draw_ue(gx+h*s3,gy,"DarkOrange1")
draw_left(gx+h*s3,gy,"DarkOrange1")

win.update()
time.sleep(0.5)

#一番外側三つのひし形
draw_left(gx-h*s3,gy,"SpringGreen4")
draw_right(gx+h*s3,gy,"SpringGreen4")
draw_ue(gx,gy-3*h,"SpringGreen4")

win.update()
time.sleep(0.5)

#一番外側三つのひし形2
draw_left(gx-h*s3,gy,"orange red")
draw_right(gx+h*s3,gy,"orange red")
draw_ue(gx,gy-3*h,"orange red")

win.update()
time.sleep(0.5)

#外側三つの羽根2
#下パート
draw_left(gx,gy-3*h,"SpringGreen4")
draw_right(gx,gy-3*h,"SpringGreen4")
#右パート
draw_ue(gx-h*s3,gy,"SpringGreen4")
draw_right(gx-h*s3,gy,"SpringGreen4")
#左パート
draw_ue(gx+h*s3,gy,"SpringGreen4")
draw_left(gx+h*s3,gy,"SpringGreen4")

win.update()
time.sleep(0.5)

#中心六角形の周囲2
#下パート
draw_left(gx,gy,"DarkOrange1")
draw_right(gx,gy,"DarkOrange1")
#右パート
draw_ue(gx+(h/2)*s3,gy-3*(h/2),"DarkOrange1")
draw_right(gx+(h/2)*s3,gy-3*(h/2),"DarkOrange1")
#左パート
draw_ue(gx-(h/2)*s3,gy-3*(h/2),"DarkOrange1")
draw_left(gx-(h/2)*s3,gy-3*(h/2),"DarkOrange1")

win.update()
time.sleep(0.5)

#真ん中一色塗2
draw_color(gx,gy-h,"yellow")

win.update()
time.sleep(2)

cv.delete("poly")
cv.delete("iro")

win.update()
time.sleep(0.5)

#すべて緑
for i in range(6):
    draw_color(l[i][0],l[i][1],"green")

win.update()
time.sleep(2)

#三色塗り
for i in range(6):
    draw_c3(l[i][0],l[i][1])
win.update()
time.sleep(2)

#サイコロの目
draw_11(gx,gy-3*h)
draw_12(gx,gy)
draw_13(gx,gy)
draw_21(gx-(h/2)*s3,gy-(3*h)/2)
draw_24(gx+(h/2)*s3,gy-(3*h)/2)
draw_26(gx,gy)
draw_31(gx-h*s3,gy)
draw_34(gx,gy)
draw_36(gx,gy)
draw_37(gx+h*s3,gy)

#左面1
draw_onel(gx,gy)

#中段左の左面
draw_sanl2(gx,gy)

#下段左の右面
draw_twor2(gx,gy)

#下面右の右面
draw_oner(gx,gy)

#中段左の右面
draw_oner2(gx,gy)

#下段右の左面
draw_fourl(gx,gy)

#中段右の左面
draw_twol(gx,gy)

#下段左の左面
draw_sixl(gx-h*s3,gy+h)

win.mainloop()

