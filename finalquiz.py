from tkinter import *
total = 0



#Round one
q = [

"What is the input size for int ?",
" For which of the following, “PI++;” code will fail?",
"Which of the following is a User-defined data type?",
"What is the scope of an external variable?",
" What would happen if you create a file stdio.h and use #include “stdio.h”?"
]

000000#Round 2
q1 = [
"What is the advantage of recursive approach than an iterative approach?" ,
"What is the search complexity in direct addressing?",
"How many stacks are needed to implement a queue. Consider the situation where no other data structure like arrays, linked list is available to you.",
"Which of the following algorithmic paradigm is used in the merge sort?",
"What is the value of the postfix expression 6 3 2 4 + – *:"]


#Round 3
q2 = ["Which one is the highest reliable topology?", " The method of communication in which transmission takes place in both directions but only one direction at a time is called _____", 
      "Error detection at Data link layer is achieved by ____", "Which parallel TCP connection does the FTP use to transfer a file?", 
      "Which of the following performs  modulation  and demodulation?"
    ]


#C language
a0 = ["3 bytes","2 bytes","4 bytes","None of the above"]
a1 = ["#define PI 3.14","char *PI = “A”;","float PI = 3.14;"," none of the Mentioned"]
a2 = [" typedef int Boolean;","typedef enum {Mon, Tue, Wed, Thu, Fri} Workdays;","struct {char name[10], int age};","all of the mentioned "]
a3 = [" Whole source file in which it is defined","From the point of declaration to the end of the file in which it is defined"
      ," Any source file in a program","From the point of declaration to the end of the file being compiled "]
a4 = ["The predefined library file will be selected","The user-defined library file will be selected",
     "Both the files will be included","The compiler won’t accept the program"]


#datastructures
b0=["Consumes less memory","Less code and easy to implement","Consumes more memory",
"More code has to be written"]
b1=["O(n)","O(logn)","O(nlogn)","O(1)"]
b2=["1","2","3","4"]
b3=["Dynamic Programming","BackTracking","Greedy method ","Divide and Conquer"]
b4=["1","40","74","-18"]

#CN final round
c0 = ["Bus Topology", "Star Topology", "Ring Topology", "Mesh Topology"]
c1 = ["Simplex", "Fore Wire", "Half Duplex", "Full Duplex"]
c2 = ["Bit Stuffing", "Cyclic Redundancy", "Hamming Code", "Equilisation"]
c3 = ["1","2","3","4"]
c4 = ["Fibre Optic","Satellite","Coaxial Cable","Modem"]
 
def bnext():

   global windows
   windows = Toplevel(root)#widget
   windows.title("Round 1 - Question 1")
   windows.geometry()
   windows.configure(bg="#C6E2FF")
   root.withdraw()

   lbl1 = Label(windows,text = q[0],font = ('arial',25,'bold')).pack(side = TOP)#widget to display text and images
   cb1 = Radiobutton(windows, text=a0[0], value=0,variable = v0,command = checked).pack(side=TOP)
   cb2 = Radiobutton(windows, text=a0[1], value=1,variable = v0,command = checked).pack(side=TOP)#acquires all the available width
   cb3 = Radiobutton(windows, text=a0[2], value=2,variable = v0,command = checked).pack(side=TOP)
   cb4 = Radiobutton(windows, text=a0[3], value=3,variable = v0,command = checked).pack(side=TOP)
   btn1 = Button(windows,text = "next",font = ('arial',21,'bold'),fg = 'blue',
                 command = bnext2).pack(side = RIGHT)#widget interaction
   btn2 = Button(windows,text = "back",font = ('arial',21,'bold'),fg = 'blue',
                 command = bback).pack(side = LEFT)
   windows.mainloop()


def bnext2():

   global windows3
   windows3 = Toplevel(windows)
   windows3.title("Round 1 - Question 2")
   windows3.geometry()
   windows3.configure(bg="#C6E2FF")
   windows.withdraw()

   lbl2 = Label(windows3, text=q[1], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows3, text=a1[0], value=0,variable = v1,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows3, text=a1[1], value=1,variable = v1,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows3, text=a1[2], value=2,variable = v1,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows3, text=a1[3], value=3,variable = v1,command = checked).pack(side=TOP)

   btn3 = Button(windows3,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext3).pack(side=RIGHT)
   btn4 = Button(windows3,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback2).pack(side=LEFT)
   windows3.mainloop()


def bnext3():

   global windows4
   windows4 = Toplevel(windows3)
   windows4.title("Round 1 - Question 3")
   windows4.geometry()
   windows4.configure(bg="#C6E2FF")
   windows3.withdraw()

   lbl2 = Label(windows4, text=q[2], font=('arial', 25, 'bold')).pack(side=TOP)
   cb9 = Radiobutton(windows4, text=a2[0], value=0,variable = v2,command = checked).pack(side=TOP)
   cb10 = Radiobutton(windows4, text=a2[1], value=1,variable = v2,command = checked).pack(side=TOP)
   cb11 = Radiobutton(windows4, text=a2[2], value=2,variable = v2,command = checked).pack(side=TOP)
   cb12 = Radiobutton(windows4, text=a2[3], value=3,variable = v2,command = checked).pack(side=TOP)

   btn5 = Button(windows4,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext4).pack(side=RIGHT)
   btn6 = Button(windows4,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback3).pack(side=LEFT)
   windows4.mainloop()


def bnext4():

   global windows5
   windows5 = Toplevel(windows4)
   windows5.title("Round 1 - Question 4")
   windows5.geometry()
   windows5.configure(bg="#C6E2FF")
   windows4.withdraw()

   lbl2 = Label(windows5, text=q[3], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows5, text=a3[0], value=0,variable = v3,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows5, text=a3[1], value=1,variable = v3,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows5, text=a3[2], value=2,variable = v3,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows5, text=a3[3], value=3,variable = v3,command = checked).pack(side=TOP)

   btn7 = Button(windows5,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext5).pack(side=RIGHT)
   btn8 = Button(windows5,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback4).pack(side=LEFT)

   windows5.mainloop()

   
def bnext5():
   global windows6
   windows6 = Toplevel(windows5)
   windows6.title("Round 1 - Bonus Question!")
   windows6.geometry()
   windows6.configure(bg="#C6E2FF")
   windows5.withdraw()

   lbl2 = Label(windows6, text=q[4], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows6, text=a4[0], value=0,variable = v4,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows6, text=a4[1], value=1,variable = v4,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows6, text=a4[2], value=2,variable = v4,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows6, text=a4[3], value=3,variable = v4,command = checked).pack(side=TOP)

   btn9 = Button(windows6,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext6).pack(side=RIGHT)
   btn10 = Button(windows6,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback5).pack(side=LEFT)

   windows6.mainloop()



def bnext6():

   global windows7
   windows7 = Toplevel(windows6)
   windows7.title("Round 2 - Question 1")
   windows7.geometry()
   windows7.configure(bg="#C6E2FF")
   windows6.withdraw()

   lbl2 = Label(windows7, text=q1[0], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows7, text=b0[0], value=0,variable = v4,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows7, text=b0[1], value=1,variable = v4,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows7, text=b0[2], value=2,variable = v4,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows7, text=b0[3], value=3,variable = v4,command = checked).pack(side=TOP)

   btn11 = Button(windows7,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext7).pack(side=RIGHT)
   btn12= Button(windows7,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback6).pack(side=LEFT)
   windows7.mainloop()

def bnext7():

   global windows8
   windows8 = Toplevel(windows7)
   windows8.title("Round 2 - Question 2")
   windows8.geometry()
   windows8.configure(bg="#C6E2FF")
   windows7.withdraw()

   lbl2 = Label(windows8, text=q1[1], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows8, text=b1[0], value=0,variable = v5,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows8, text=b1[1], value=1,variable = v5,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows8, text=b1[2], value=2,variable = v5,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows8, text=b1[3], value=3,variable = v5,command = checked).pack(side=TOP)

   btn13 = Button(windows8,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext8).pack(side=RIGHT)
   btn14 = Button(windows8,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback7).pack(side=LEFT)
   windows8.mainloop()


def bnext8():

   global windows9
   windows9 = Toplevel(windows8)
   windows9.title("Round 2 - Question 3")
   windows9.geometry()
   windows9.configure(bg="#C6E2FF")
   windows8.withdraw()

   lbl2 = Label(windows9, text=q1[2], font=('arial', 16, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows9, text=b2[0], value=0,variable = v6,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows9, text=b2[1], value=1,variable = v6,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows9, text=b2[2], value=2,variable = v6,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows9, text=b2[3], value=3,variable = v6,command = checked).pack(side=TOP)

   btn15 = Button(windows9,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext9).pack(side=RIGHT)
   btn16= Button(windows9,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback8).pack(side=LEFT)
   windows9.mainloop()


def bnext9():

   global windows10
   windows10 = Toplevel(windows9)
   windows10.title("Round 2 - Question 4")
   windows10.geometry()
   windows10.configure(bg="#C6E2FF")
   windows9.withdraw()

   lbl2 = Label(windows10, text=q1[3], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows10, text=b3[0], value=0,variable = v7,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows10, text=b3[1], value=1,variable = v7,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows10, text=b3[2], value=2,variable = v7,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows10, text=b3[3], value=3,variable = v7,command = checked).pack(side=TOP)

   btn17 = Button(windows10,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext10).pack(side=RIGHT)
   btn18= Button(windows10,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback9).pack(side=LEFT)
   windows10.mainloop()



def bnext10():

   global windows11
   windows11= Toplevel(windows10)
   windows11.title("Round 2 - Bonus Question!")
   windows11.geometry()
   windows11.configure(bg="#C6E2FF")
   windows10.withdraw()

   lbl2 = Label(windows11, text=q1[4], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows11, text=b4[0], value=0,variable = v8,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows11, text=b4[1], value=1,variable = v8,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows11, text=b4[2], value=2,variable = v8,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows11, text=b4[3], value=3,variable = v8,command = checked).pack(side=TOP)

   btn19 = Button(windows11,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext11).pack(side=RIGHT)
   btn20= Button(windows11,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback10).pack(side=LEFT)
   windows11.mainloop()

def bnext11():

   global windows12
   windows12= Toplevel(windows11)
   windows12.title("Round 3 - Question 1")
   windows12.geometry()
   windows12.configure(bg="#C6E2FF")
   windows11.withdraw()

   lbl2 = Label(windows12, text=q2[0], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows12, text=c0[0], value=0,variable = v9,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows12, text=c0[1], value=1,variable = v9,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows12, text=c0[2], value=2,variable = v9,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows12, text=c0[3], value=3,variable = v9,command = checked).pack(side=TOP)

   btn19 = Button(windows12,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext12).pack(side=RIGHT)
   btn20= Button(windows12,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback11).pack(side=LEFT)
   windows12.mainloop()

def bnext12():

   global windows13
   windows13= Toplevel(windows12)
   windows13.title("Round 3 - Question 2")
   windows13.geometry()
   windows13.configure(bg="#C6E2FF")
   windows12.withdraw()

   lbl2 = Label(windows13, text=q2[1], font=('arial', 16, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows13, text=c1[0], value=0,variable = v10,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows13, text=c1[1], value=1,variable = v10,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows13, text=c1[2], value=2,variable = v10,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows13, text=c1[3], value=3,variable = v10,command = checked).pack(side=TOP)

   btn19 = Button(windows13,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext13).pack(side=RIGHT)
   btn20= Button(windows13,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback12).pack(side=LEFT)
   windows13.mainloop()

def bnext13():

   global windows14
   windows14= Toplevel(windows13)
   windows14.title("Round 3 - Question 3")
   windows14.geometry()
   windows14.configure(bg="#C6E2FF")
   windows13.withdraw()

   lbl2 = Label(windows14, text=q2[2], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows14, text=c2[0], value=0,variable = v11,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows14, text=c2[1], value=1,variable = v11,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows14, text=c2[2], value=2,variable = v11,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows14, text=c2[3], value=3,variable = v11,command = checked).pack(side=TOP)

   btn19 = Button(windows14,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext14).pack(side=RIGHT)
   btn20= Button(windows14,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback13).pack(side=LEFT)
   windows14.mainloop()

def bnext14():

   global windows15
   windows15= Toplevel(windows14)
   windows15.title("Round 3 - Question 4")
   windows15.configure(bg="#C6E2FF")
   windows15.geometry()
   
   windows14.withdraw()

   lbl2 = Label(windows15, text=q2[3], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows15, text=c3[0], value=0,variable = v12,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows15, text=c3[1], value=1,variable = v12,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows15, text=c3[2], value=2,variable = v12,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows15, text=c3[3], value=3,variable = v12,command = checked).pack(side=TOP)

   btn19 = Button(windows15,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext15).pack(side=RIGHT)
   btn20= Button(windows15,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback14).pack(side=LEFT)
   windows15.mainloop()

def bnext15():

   global windows16
   windows16= Toplevel(windows15)
   windows16.title("Round 3 - Bonus Question!")
   windows16.geometry()
   windows16.configure(bg="#C6E2FF")
   windows15.withdraw()

   lbl2 = Label(windows16, text=q2[4], font=('arial', 25, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows16, text=c4[0], value=0,variable = v13,command = checked).pack(side=TOP)
   cb6 = Radiobutton(windows16, text=c4[1], value=1,variable = v13,command = checked).pack(side=TOP)
   cb7 = Radiobutton(windows16, text=c4[2], value=2,variable = v13,command = checked).pack(side=TOP)
   cb8 = Radiobutton(windows16, text=c4[3], value=3,variable = v13,command = checked).pack(side=TOP)

   btn19 = Button(windows16,text = "next",font = ('arial',16,'bold'),fg = 'blue',command = bnext16).pack(side=RIGHT)
   btn20= Button(windows16,text = "back",font = ('arial',16,'bold'),fg = 'blue',command = bback15).pack(side=LEFT)
   windows16.mainloop()

def bnext16():

   global windows17
   windows17 = Toplevel(windows16)
   windows17.title("Final Result")
   windows17.geometry("400x500")
   windows17.configure(bg="#C6E2FF")
   windows16.withdraw()
   btn8 = Button(windows17, text="back", font=('arial', 16, 'bold'), fg='blue', command=bback16).pack(padx=5, pady=10,side=BOTTOM)
   bquit = Button(windows17, text="Quit", font=('arial', 16, 'bold'),
                  fg='blue', command=windows17.destroy).pack(padx=5, pady=10,side=BOTTOM)
   bf = Label(windows17,text = "YOUR SCORE IS " + str(total) + "/18",font = ("arial",28,"bold"),fg = "red")
   bf.pack(side = TOP)

   windows17.mainloop()


def bback():

    windows.withdraw()
    root.deiconify()
    root.mainloop()


def bback2():

    windows3.withdraw()
    windows.deiconify()
    windows.mainloop()


def bback3():

    windows4.withdraw()
    windows3.deiconify()
    windows3.mainloop()


def bback4():

    windows5.withdraw()
    windows4.deiconify()
    windows4.mainloop()

def bback5():

    windows6.withdraw()
    windows5.deiconify()
    windows5.mainloop()

def bback6():

    windows7.withdraw()
    windows6.deiconify()
    windows6.mainloop()

def bback7():

    windows8.withdraw()
    windows7.deiconify()
    windows7.mainloop()
def bback8():

    windows9.withdraw()
    windows8.deiconify()
    windows8.mainloop()


def bback9():

    windows10.withdraw()
    windows9.deiconify()
    windows9.mainloop()

def bback10():

    windows11.withdraw()
    windows10.deiconify()
    windows10.mainloop()


def bback11():

    windows12.withdraw()
    windows11.deiconify()
    windows11.mainloop()
    
def bback12():

    windows13.withdraw()
    windows12.deiconify()
    windows12.mainloop()

def bback13():

    windows14.withdraw()
    windows13.deiconify()
    windows13.mainloop()

def bback14():

    windows15.withdraw()
    windows14.deiconify()
    windows14.mainloop()

def bback15():

    windows16.withdraw()
    windows15.deiconify()
    windows15.mainloop()
    
def bback16():

    windows17.withdraw()
    windows16.deiconify()
    windows16.mainloop()
    
    



def checked():

    #global c
    #global w
    c=0

    if v0.get() == 1:

        c += 1

    if v1.get() == 0:

        c += 1

    if v2.get() == 3:

        c += 1

    if v3.get() == 3:

        c += 1

    if v4.get() == 2:

        c += 2

    if v5.get() == 1:

        c += 1

    if v6.get() == 3:

        c += 1

    if v7.get() == 1:

        c += 1

    if v8.get() == 3:

        c += 1

    if v9.get() == 3:

        c += 2
    
    if v10.get() == 3:

        c += 1

    if v11.get() == 2:

        c += 1

    if v12.get() == 1:

        c += 1

    if v13.get() == 1:

        c += 1


    if v14.get() == 3:

        c += 2

    global total
    total = c


root = Tk()#creates blank window

v0 = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()
v12 = IntVar()
v13 = IntVar()
v14 = IntVar()

root.title("Quiz Program")
root.geometry("700x200")
root.configure(bg='#C1FFC1')
lbl0 = Label(root,text = "Answer the following questions",font = ("arial",20,"bold"),fg = 'purple').pack(side = TOP)
lbl00 = Label(root,text = "about Computer Science!", font = ("arial",20,"bold"), fg = 'purple').pack(side = TOP)#display widget in required size

btn1 = Button(root,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext).pack(padx=5, pady=10,side = TOP)


root.mainloop()#keeps displaying the window until we manually close it





