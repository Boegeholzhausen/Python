from tkinter import*
import time

root=Tk()
root.configure(background=("black"))
root.title("stopwatch")
root.geometry("1000x800")
time_elapsed1=0
time_elapsed2=0
time_elapsed3=0
i=0
j=0
time1=0

def create_label(text,_x,_y):
    label = Label(root, text=text,fg='white', bg="black",font=("default",10,"bold"))
    label.place(x=_x,y=_y,width=100,height=45)
def start():
    start_button.place_forget()
    stop_button.place(x = 20, y = 300, width=300, height=100)
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=str(time_elapsed3) + ":" + str(time_elapsed2)+ ":" + str(time_elapsed1))
        else:
            time_elapsed1=0
            if time_elapsed2<59:
                time_elapsed2+=1
                clock_frame.config(text=(str(time_elapsed3) + ":" + str(time_elapsed2)+ ":" + str(time_elapsed1)))
            else:
                time_elapsed2=0
                if time_elapsed3<23:
                    time_elapsed3+=1
                    clock_frame.config(text=(str(time_elapsed3) + ":" + str(time_elapsed2)+ ":" + str(time_elapsed1)))
                else:
                    print("you left it on for too long")
    self_job=root.after(1000,start)

def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job = None
    stop_button.place_forget()
    start_button.place(x = 20, y = 300, width=300, height=100)

def clear():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,label,i,j
    try:
        stop()
    except:
        start()
        stop()
    clock_frame.config(text="0:0:0")
    time_elapsed1=0
    time_elapsed2=0
    time_elapsed3=0
    time_1=0
    time_2=0
    i=0
    j=0
    wig=root.winfo_children()
    for b in wig:
        b.place_forget()
    start_button.place(x = 20, y = 300, width=300, height=100)
    lap_button.place(x = 660, y = 300, width=300, height=100)
    reset_button.place(x = 340, y = 300, width=300, height=100)
    clock_frame.place(x = 200, y = 50, width=600, height=200)


def lap():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,i,j
    if i<9:
        create_label((str(time_elapsed3)+":"+str(time_elapsed2)+ ":" + str(time_elapsed1)),20+(110*i),400+(j*50))
    else:
        j+=1
        i=0
        create_label((str(time_elapsed3)+":"+str(time_elapsed2)+ ":" + str(time_elapsed1)),20+(110*i),400+(j*50))
    i+=1





clock_frame=Label(text="0:0:0",bg="black",fg="blue",font=("default",100,"bold"))
start_button=Button(text="START",bg="green",fg="black",command=start,font=("default",50,"bold"))
stop_button=Button(text="STOP",bg="red",fg="black",command=stop,font=("default",50,"bold"))
lap_button=Button(text="LAP",bg="#4286f4",fg="black",command=lap,font=("default",50,"bold"))
reset_button=Button(text="RESET",bg="orange",fg="black",command=clear,font=("default",50,"bold"))


start_button.place(x = 20, y = 300, width=300, height=100)
lap_button.place(x = 660, y = 300, width=300, height=100)
reset_button.place(x = 340, y = 300, width=300, height=100)
clock_frame.place(x = 200, y = 50, width=600, height=200)


root.mainloop()