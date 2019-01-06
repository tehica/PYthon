from Tkinter import *
from tkinter import scrolledtext
import time
import sys
root = Tk()
root.geometry("900x600")
root.wm_attributes("-topmost", 1)
root.title("Toni")
root.attributes("-fullscreen", True)
s = Style(root)
s.theme_use("clam")
#B = Button(root, text="A").grid(row=0, column = 1)
TABlabel = Notebook(root)
TABlabel.grid(ipadx = 3, ipady = 3)

tab1 = Frame(TABlabel)
tab2 = Frame(TABlabel)

TABlabel.add(tab1, text="Tab 1")
TABlabel.add(tab2, text="Tab 2")


Labframe1 = LabelFrame(tab1, text="Python ver. 3.6.3")
Labframe1.grid(row=0, column=0, padx = 8, pady = 4) # padx = 8 i pady = 4 znaci da se cijeli label odmakne od lijevog ruba ekrana
                                                    # i prema dole
Label(Labframe1, text="Choose font:").grid(row=0, column=0, sticky="W") # bez ovog reda nece se ni Python ver. 3.6.3 ispisati
"""
def CheckBut1():
    if Var2.get() == 1:
        entry1.configure(state = NORMAL)
        check1.configure(state = DISABLED)
        check2.configure(state = NORMAL)
Var2 = IntVar()
Var2.set(0)
Label(Labframe1, text="TextBox 1").grid(row=2, column = 0, sticky = W, padx = 3)
check1 = Checkbutton(Labframe1, text="Enable", variable = Var2, command = CheckBut1) # command = CheckBut1
check1.grid(row=2, column=0, sticky="W", padx=3)
"""
Label(Labframe1, text="TextBox 1").grid(row=2, column = 0, sticky = W, padx = 25)
Label(Labframe1, text="TextBox 2").grid(row=2, column = 4, sticky = W, padx = 25)
def CheckBut2():
    if Var3.get() == 1:
        entry1.configure(state = DISABLED)
        check1.configure(state = NORMAL)
        check2.configure(state = DISABLED)
Var3 = IntVar()
Var3.set(0)
check2 = Checkbutton(Labframe1, text="Disable", variable = Var3, command = CheckBut2) # command = CheckBut2
check2.grid(row=2, column=1, sticky="W", padx=30)
def CheckBut3():
    pass
Var4 = IntVar()
Var4.set(0)
check3 = Checkbutton(Labframe1, text="UnChecked", variable = Var4, command = CheckBut3) # command = CheckBut3
check3.grid(row=2, column=2, sticky="W")

Label(Labframe1, text="Choose font:").grid(row=0, column=1, sticky="W", padx=30)

B1 = Button(Labframe1, text="Click", command = None).grid(row=1, column=2, sticky="E")

v1 = 10
v2 = "TkDefaultFont"
v3 = "Black"
def combobox_select(event):
    global v1, v2
    v1 = number.get()
    text1.configure(font=(v2, v1))
number = StringVar()
numberChosen = Combobox(Labframe1, width=12, textvariable=number, values= (10, 12, 14, 16, 18, 20))
numberChosen.grid(row=1, column=1, sticky="WN", padx=30)
numberChosen.current(0)
numberChosen.bind("<<ComboboxSelected>>", combobox_select)

def combobox_select_2(event):
    global v1, v2 
    v2 = number2.get()
    text1.configure(font=(v2, v1))
number2 = StringVar()
numberChosen2 = Combobox(Labframe1, width=12, textvariable=number2, values= ("Arial", "Times",
                                                                             "Comic Sans MS", "Fixedsys",
                                                                             "MS Sans Serif",
                                                                             "MS Serif, Symbol", "System",
                                                                             "Verdana"))
numberChosen2.grid(row=1, column=0, sticky="WN")
numberChosen2.current(0)
numberChosen2.bind("<<ComboboxSelected>>", combobox_select_2)

def radCall():
    v = radVar.get()
    if v == 1:
        text1.configure(fg="Blue")
    if v == 2:
        text1.configure(fg="Gold")
    if v == 3:
        text1.configure(fg="Red")

radVar = IntVar()
Label(Labframe1, text="Text color:").grid(row=4, column=0, sticky = W)
def combobox_select_3(event):
    global v3
    v3= number3.get()
    text1.configure(fg=v3)
    
number3 = StringVar()
numberChosen3 = Combobox(Labframe1, width=12, textvariable=number3, values= ("Black", "Blue", "Red", "Gold", "Silver"))
numberChosen3.grid(row=4, column=1, sticky="WN", padx=30)
numberChosen3.current(0)
numberChosen3.bind("<<ComboboxSelected>>", combobox_select_3)

Arial = "TkDefaultFont"
fontSize = 10
def select_all(event): # oznaci cijeli tekst
    text1.tag_("sel", "1.0", "end-1c")
    
text1 = Text(Labframe1, width = 35, height = 15,
             bd = 10, relief = SUNKEN, selectbackground = '#000fff000',
             selectforeground = '#00ffff', spacing1 = 5,
             font=("{}" "{}".format(Arial, fontSize)))


text1.grid(row=3, column = 0, columnspan = 3)
text1.bind("<Control-a>", select_all)
# scrolledtext.ScrolledText
# text1.insert(INSERT, "my status here")

text2 = Text(Labframe1, width = 35, height = 14, bd = 10,
             relief = SUNKEN, selectbackground = '#000fff000',
             selectforeground = '#00ffff', spacing1 = 5)
text2.grid(row=3, column
           = 4, sticky = E, padx = 30)
def prenesi():
    global v1, v2, v3
    text2["state"] = NORMAL
    Vtext = StringVar()
    Vtext = text1.get("1.0", END)
    text2.insert(INSERT, Vtext)
    text2.configure(font=(v2, v1))
    text2.configure(fg=v3)
    text2["state"] = DISABLED
    
B3 = Button(Labframe1, text="Prenesi tekst", command = prenesi)
B3.grid(row=3, column= 5, sticky = N, padx = 30, pady = 10)
def clear_textBox2():
    text2["state"] = NORMAL
    text2.delete("1.0", END)
    text2["state"] = DISABLED
B4 = Button(Labframe1, text="Clear TextBox 2", command = clear_textBox2)
B4.grid(row=2, column = 5, sticky = N)

def tick():
    global time1
    
    time2 = time.strftime('%H:%M:%S')
    
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        
    clock.after(200, tick)
#def hide(event): # da se sakrije label
    #event.widget.grid_forget()


time1 = ''

clock = Label(Labframe1, font=('times', 14, 'bold'))
clock.grid(row=4, column=2, sticky = W) 
#clock.bind("<Button-1>", hide)

tick()



menuBar = Menu(root)
root.config(menu=menuBar)

fileMenu = Menu(menuBar)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Exit", command = root.destroy)

menuBar.add_cascade(label="File", menu = fileMenu)

root.mainloop()









                                              
