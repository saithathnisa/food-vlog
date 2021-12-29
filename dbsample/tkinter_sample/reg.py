import tkinter
import tkinter.messagebox
from PIL import ImageTk,Image
from subprocess import call
t=tkinter.Tk()
t.title('profile')
t.geometry('500x500')

p=Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\tkinter_sample\\bg.jpg")
p=p.resize((500,500))
p=ImageTk.PhotoImage(p)

pic=tkinter.Label(t,image=p)
pic.place(x=0,y=0)

a=tkinter.Label(text="profile creation",bg="indigo",fg="white",font=('bradley hand itc',35,'bold'))
a.place(x=90,y=0)

b=tkinter.Label(text="first name",bg="blue",fg="white",font=('bradley hand itc',25,'bold'))
b.place(x=50,y=100)
c=tkinter.Entry(width=30)
c.place(x=275,y=120)

d=tkinter.Label(text="location",bg="blue",fg="white",font=('bradley hand itc',25,'bold'))
d.place(x=50,y=170)
e=tkinter.Entry(width=30)
e.place(x=275,y=190)

def abcd():
    name=c.get()
    place=e.get()
    
    if(name==""or place==""):
        
        tkinter.messagebox.showerror('error','please complete fields')
    else:
        import pymysql
        x=pymysql.connect(host='localhost',user='root',password='nichu',db='abcd')
        cur=x.cursor()
        cur.execute("insert into profile values('"+name+"','"+place+"')")
        x.commit()
        x.close()
        tkinter.messagebox.showinfo('thankyou','thanks for visiting')
        t.destroy()

        call(['python','next.py'])
    

f=tkinter.Button(text="submit",bg="red",fg="yellow",font=('times new roman',15,'bold'),command=abcd)
f.place(x=225,y=250)


t.mainloop()
