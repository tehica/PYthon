# download pictures log.png , Login.png and xx.png
from tkinter import *
from time import *
import tkinter.messagebox
import webbrowser
root = Tk()
root.geometry("750x500")
root.title("Toni")
root.wm_attributes("-topmost", 1)

img = PhotoImage(file = "login.png")
img_label = Label(root, image = img)
img_label.place(x=0, y=0, relwidth=1, relheight=1)

L1 = Label(root, text="Username:", font = ("Arial 15 bold"))
L2 = Label(root, text="Password:", font = ("Arial 15 bold"))

E1 = Entry(root, textvariable = StringVar())
E2 = Entry(root, show ="*", textvariable = StringVar())

def potvrda():
  potvrda.has_been_called = True
  E1.config(state=DISABLED)
  E2.config(state=DISABLED)
B5 = Button(root, text = "Potvrdi prijavu", command = potvrda)
B5.grid(row=2, column = 1, sticky=W+N)

def odtvrda():
  potvrda.has_been_called = False
  E1.config(state=NORMAL)
  E2.config(state=NORMAL)
B6 = Button(root, text="Ukloni potvrdu prijave", command = odtvrda)
B6.grid(row=3, column = 1, sticky = W+N)
potvrda.has_been_called = False

def var():
  username = E1.get()
  password = E2.get()
  if (username == "Toni") and (password == "musa") and potvrda.has_been_called:
      print("Uspjesna prijava")
      def link(event):
        webbrowser.open_new(r"http://www.google.com")

      link_1 = Label(root, text="Dobrodošao Toni \nLista predmeta:", fg="blue", cursor="hand2")
      link_1.grid(row=4, column = 0, sticky = W)
      link_1.bind("<Button-1>", None)

      img.configure(file = "log.png")
      Predmeti = ["Engleski", "Psihologija stresa","Matematika", "Elektrotehnika", "Operacijski sustavi",
                  "Simbolicka logika", "Algoritmi i strukture podataka"]

      def onselect(evt):
        
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        # print (value)
        # print (index)
        
        if index == 0:
          info1 = "Opce informacije: \nECTS: 5 \nSemestar: 1 \nBroj sati predavanja: 2 \nBroj sati vjezbi: 3"
          predmeti.set(info1)
        if index == 1:
          info2 = "Opce informacije: \nECTS: 5 \nSemestar: 2 \nBroj sati predavanja: 2 \nBroj sati vjezbi: 2"
          predmeti.set(info2)
        if index == 2:
          info3 = "Opce informacije: \nECTS: 5 \nSemestar: 1 \nBroj sati predavanja: 2 \nBroj sati vjezbi: 3"
          predmeti.set(info3)
        if index == 3:
          info4 = str(value) + ", broj ECTS bodova: 5"
          predmeti.set(info4)
        if index == 4:
          info5 = str(value) + ", broj ECTS bodova: 5"
          predmeti.set(info5)
        if index == 5:
          info6 = str(value) + ", broj ECTS bodova: 3"
          predmeti.set(info6)
        if index == 6:
          info7 = str(value) + ", broj ECTS bodova: 2"
          predmeti.set(info7)
          
      
      listBox = Listbox(root, width = 25, height = 10, font=("Arial 10 bold"), bg = "Aqua", relief = RIDGE)
      listBox.grid(row=5, column = 0, sticky = W)
      for i in Predmeti:
        listBox.insert(0, i)

      predmeti = StringVar()
      
      listBox.bind('<<ListboxSelect>>', onselect)
      Lab = Label(root, textvariable = predmeti, font = ("Arial", 10)).grid(row=6, column=0, sticky = W)
      
  else:
    img.configure(file = "xx.png")
    print("Krivi username ili lozinka ili niste potvrdili prijavu")
    
B3 = Button(root, text="Log-in", command = var, fg = "White", bg = "Black")

def quitt():
  P1 = tkinter.messagebox.askquestion(None, "Želite li zatvoriti program?")
  if P1 == "yes":
    sleep(1)
    root.destroy()
  if P1 == "no":
    pass

B4 = Button(root, text="Quit", command = quitt, bg = "Gray")

var = IntVar()
var.set(0)
def CB():
  if var.get() == 1:
    E2.config(show="")
  if var.get() == 0:
    E2.config(show="*")
B7 = Checkbutton(root, text="Prikazi lozinku", variable = var,
                 command = CB)
B7.grid(row=1, column = 2)

                 
L1.grid(row=0, column = 0, sticky = W)
E1.grid(row=0, column = 1, sticky = W)

L2.grid(row=1, column = 0, sticky = W)
E2.grid(row=1, column = 1, sticky = W)

B3.grid(row=2, column = 0, sticky = W)
B4.grid(row=3, column = 0, sticky = W)

root.mainloop()
