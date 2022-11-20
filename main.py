import tkinter
from tkinter import *

root=Tk()
root.title("To-Do Lista")
root.geometry("400x650+400+100")
root.resizable(False,False)

tasklist= []

def addTask():
    feladat = feladat_belepes.get()
    feladat_belepes.delete(0, END)


    if feladat:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{feladat}")
        tasklist.append(feladat)
        listbox.insert( END, feladat)

def deleteTask():
    global tasklist
    feladat = str(listbox.get(ANCHOR))
    if feladat in tasklist:
        tasklist.remove(feladat)
        with open("tasklist.txt",'w') as taskfile:
            for feladat in tasklist:
                taskfile.write(feladat+"\n")

        listbox.delete( ANCHOR)

def openTaskFile():

    try:
        global tasklist
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                tasklist.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()








#ikon

kepek_icon=PhotoImage(file="kepek/task.png")
root.iconphoto(False,kepek_icon)

#felsoresz

TopImage=PhotoImage(file="kepek/topbar.png")
Label(root, image=TopImage).pack()

dockImage=PhotoImage(file="kepek/dock.png")
Label(root, image=dockImage, bg="red").place(x=30,y=25)

noteImage=PhotoImage(file="kepek/task.png")
Label(root, image=noteImage, bg="pink").place(x=350, y=15)

heading=Label(root,text="Minden feladat",font="arial 20 bold", fg="white", bg="black")
heading.place(x=130,y=20)

#fo program

frame = Frame(root,width=700, height=280,bg="white")
frame.place(x=0,y=180)

feladat=StringVar()
feladat_belepes=Entry(frame, width=18, font="arial 20",bd=0)
feladat_belepes.place(x=10, y=7)

#gombok

button=Button(frame,text="Hozzáadás",font="arial 20", width=10, command=addTask)
button.place(x=235, y=0)

#listák
elso= Frame(root,bd=3, width=700, height=280,bg="white")
elso.pack(pady=(160,0))

listbox= Listbox(elso,font=('arial',12),width=40,height=16,bg="white")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar=Scrollbar(elso)
scrollbar.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()


#törlés

Delete_icon=PhotoImage(file="kepek/delete.png")
Button(root, image=Delete_icon,bd=0, command=deleteTask).pack(side=BOTTOM)


root.mainloop()