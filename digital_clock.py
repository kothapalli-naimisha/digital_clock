from tkinter import *
import time
from datetime import datetime
root=Tk()
root.geometry("1300x750+0+0")
root.title("DIGITAL CLOCK")
root.config(bg="#8B4513")

title=Label(root,text="DIGITAL CLOCK", font=("times new roman",40,"bold"),bg="#8B4513",fg="white").place(x=0,y=20,relwidth=1)
def clock():
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
    d = datetime.today().strftime("%A")
    date = datetime.today().strftime("%B")
    y = datetime.today().strftime("%d")
    if int(h)>12 and int(m)>0:
        meri.config(text="PM")
    if int(h)>12:
        h=str(int(h)-12)
    hour.config(text=h)
    mins.config(text=m)
    secs.config(text=s)
    day.config(text=d)
    mon.config(text=date)
    yer.config(text=y)
    hour.after(200,clock)




#---hour---
hour=Label(root,text="12",bg="purple", fg="white", font=("times new roman",70,"bold"))
hour.place(x=250,y=150,width=150,height=150)
hour_txt=Label(root,text="HOURS",bg="purple", fg="white",font=("times new roman",25))
hour_txt.place(x=250,y=325,width=150,height=50)

#---minutes---
mins=Label(root,text="12",bg="#7e1412", fg="white", font=("times new roman",70,"bold"))
mins.place(x=450,y=150,width=150,height=150)
mins_txt=Label(root,text="MINUTES",bg="#7e1412", fg="white",font=("times new roman",25))
mins_txt.place(x=450,y=325,width=150,height=50)

#----seconds---
secs=Label(root,text="12",bg="#cc5500", fg="white", font=("times new roman",70,"bold"))
secs.place(x=650,y=150,width=150,height=150)
secs_txt=Label(root,text="SECONDS",bg="#cc5500", fg="white",font=("times new roman",25))
secs_txt.place(x=650,y=325,width=150,height=50)

#---meridiem----
meri=Label(root,text="AM",bg="#e2725b", fg="white", font=("times new roman",70,"bold"))
meri.place(x=850,y=150,width=150,height=150)
meri_txt=Label(root,text="MERIDIEM",bg="#e2725b", fg="white",font=("times new roman",25))
meri_txt.place(x=850,y=325,width=150,height=50)

#----Day----
day=Label(root,text="12",bg="#081923", fg="white", font=("times new roman",30,"bold"))
day.place(x=250,y=450,width=300,height=50)


#---Month----
mon=Label(root,text="12",bg="#081923", fg="white", font=("times new roman",30,"bold"))
mon.place(x=500,y=450,width=300,height=50)


#---Year---
yer=Label(root,text="12",bg="#081923", fg="white", font=("times new roman",30,"bold"))
yer.place(x=720,y=450,width=300,height=50)


clock()
root.mainloop()