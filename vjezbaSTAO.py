from tkinter import *
from random import *
from time import *
import tkinter.messagebox
import webbrowser
from pygame import *
from functools import *

root = Tk()
root.title("Toni tkinter")
root.geometry("1825x990")
root.wm_attributes("-topmost", 1)
background_image=PhotoImage(file = "mvm.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def start():
    tkinter.messagebox.showinfo("Minecraft", "Dobrodošli u Minecraft! :)")
start()
M2 = tkinter.messagebox.askquestion(None, "Zelite li igrati singleplayer mod?")

def destroy_root():
    root.destroy()
    
def pitanje1():
    M3 = tkinter.messagebox.askquestion(None, "Zelite li igrati Multiplayer mod?")
    if M3 == "yes":
        tkinter.messagebox.showinfo("Dobrodošli", "Dobrodošli u Multiplayer mode!")
    if M3 == "no":
        tkinter.messagebox.showinfo(None, "Zao mi je, igra ce se zatvoriti za 5 sekundi.")
        sleep(5) # nakon sto stinem na ' u redu ' root ce se zatvoriti za 5 sekundi
        destroy_root()
if M2 == "yes":
    tkinter.messagebox.showinfo("Dobrodošli", "Dobrodošli u singleplayer mode!")
if M2 == "no":
    pitanje1()

def Info():
    tkinter.messagebox.showinfo("Info box", "Sve o igrici: https://minecraft.net/en-us/")
def run():
    Label1 = Label(root, text="Stisnite gumb dole za pokretanje igre.")
    Label1.grid(row = 1, column = 0, sticky = "W")
    Label2 = Label(root, text="----------------------")
    Label2.grid(row = 3, column = 0, sticky = "W")
    def exit_to_animate():
        But1 = Button(root, text = "Run Game", fg = "Red", bg = "White", command = novi_tk1)
        But1.grid(row = 2, column = 0, sticky = "W")
    exit_to_animate()
def help1():
    tkinter.messagebox.showinfo("Help box", "Help za igricu: https://minecraft.net/en-us/help/?ref=gm")
    
mainMenu = Menu(root)
root.configure(menu = mainMenu)
subMenu = Menu(mainMenu)
subMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label="Ulaz", menu = subMenu)
mainMenu.add_cascade(label="Postavke", menu = subMenu2) # ovako se dodaje nova glavna opcija na alatnoj traci
subMenu.add_command(label="Info", command = Info)
subMenu.add_command(label="Pokreni igru", command = run)
subMenu.add_separator()
subMenu.add_command(label="Help", command = help1)

B1 = Button(root, text = "Pozdrav", command = start)
B1.grid(row = 0, column = 0, sticky = "W") # W da zalijepi za lijevi dio ekrana gumb

novac = 20
index = 0
def novi_tk1():
    destroy_root()
    novi_tk()

def muzika():

    root2 = Tk()
    root2.geometry("1000x500")
    root2.configure(background='Green')

    def druga_lista_pjesama():
        B1.destroy()
        B2.destroy()
        root2.geometry("500x500")
        root2.configure(background='Blue')
        v = StringVar() # odnosi se na update label koji nije toliko bitan za pustanje muzike
        listofsongs = ["Matrica3.mp3", "Matrica4.mp3"]
        songlabel = Label(root2, textvariable = v, width = 35) # odnosi se na update label koji nije toliko bitan za pustanje muzike

        def nextsong(event):
            global index
            index += 1
            mixer.music.load(listofsongs[index])
            mixer.music.play()
            updatelabel() # odnosi se na update label koji nije toliko bitan za pustanje muzike

        def prevsong(event):
            global index
            index -= 1
            mixer.music.load(listofsongs[index])
            mixer.music.play()
            updatelabel() # odnosi se na update label koji nije toliko bitan za pustanje muzike

        def exit_from_music(event):
            mixer.music.stop()
            root2.destroy()

        def back():
            mixer.music.stop()
            root2.destroy()
            muzika()

        def updatelabel(): # odnosi se na update label koji nije toliko bitan za pustanje muzike
            global index
            global songname
            v.set(listofsongs[index])
            return songlabel

        def directorychooser():
            for i in listofsongs:
                mixer.init()
                mixer.music.load(i)
                mixer.music.play()
            mixer.init()
            mixer.music.load(listofsongs[0])
            #mixer.music.play()

        directorychooser()
        root2.wm_attributes("-topmost", 1)
    
        label = Label(root2, text = "Music Player")
        label.pack()
    
        listbox = Listbox(root2)
        listbox.pack() # odnosi se na update label koji nije toliko bitan za pustanje muzike

        for items in listofsongs:
            listbox.insert(0, items) # umetni u listbox iz liste 'listofsongs' indexe od 0 do koliko ih ima u listi

        nextbutton = Button(root2, text="Next song")
        nextbutton.pack()

        prevbutton = Button(root2, text ="Prev. song")
        prevbutton.pack()

        stopbutton = Button(root2, text="Stop and exit")
        stopbutton.pack()

        backbutton = Button(root2, text="Back", command = back)
        backbutton.pack()

        nextbutton.bind("<Button-1>", nextsong)
        prevbutton.bind("<Button-1>", prevsong)
        stopbutton.bind("<Button-1>", exit_from_music)

        songlabel.pack()

        root2.mainloop()
    
    def prva_lista_pjesama():
        B1.destroy()
        B2.destroy()
        root2.geometry("500x500")
        root2.configure(background='Red')
        v = StringVar() # odnosi se na update label koji nije toliko bitan za pustanje muzike
        listofsongs = ["Matrica1.mp3", "Matrica2.mp3"]
        songlabel = Label(root2, textvariable = v, width = 35) # odnosi se na update label koji nije toliko bitan za pustanje muzike

        def nextsong(event):
            global index
            index += 1
            mixer.music.load(listofsongs[index])
            mixer.music.play()
            updatelabel() # odnosi se na update label koji nije toliko bitan za pustanje muzike

        def prevsong(event):
            global index
            index -= 1
            mixer.music.load(listofsongs[index])
            mixer.music.play()
            updatelabel() # odnosi se na update label koji nije toliko bitan za pustanje muzike

        def exit_from_music(event):
            mixer.music.stop()
            root2.destroy()

        def back():
            mixer.music.stop()
            root2.destroy()
            muzika()

        def updatelabel(): # odnosi se na update label koji nije toliko bitan za pustanje muzike
            global index
            global songname
            v.set(listofsongs[index])
            return songlabel

        def directorychooser():
            for i in listofsongs:
                mixer.init()
                mixer.music.load(i)
                mixer.music.play()
            mixer.init()
            mixer.music.load(listofsongs[0])
            #mixer.music.play()

        directorychooser()
        root2.wm_attributes("-topmost", 1)
    
        label = Label(root2, text = "Music Player")
        label.pack()
    
        listbox = Listbox(root2)
        listbox.pack() # odnosi se na update label koji nije toliko bitan za pustanje muzike

        for items in listofsongs:
            listbox.insert(0, items) # umetni u listbox iz liste 'listofsongs' indexe od 0 do koliko ih ima u listi

        nextbutton = Button(root2, text="Next song")
        nextbutton.pack()

        prevbutton = Button(root2, text ="Prev. song")
        prevbutton.pack()

        stopbutton = Button(root2, text="Stop and exit")
        stopbutton.pack()

        backbutton = Button(root2, text="Back", command = back)
        backbutton.pack()

        nextbutton.bind("<Button-1>", nextsong)
        prevbutton.bind("<Button-1>", prevsong)
        stopbutton.bind("<Button-1>", exit_from_music)

        songlabel.pack()

        root2.mainloop()
    
    B1 = Button(root2, text ="1. lista pjesama", command = prva_lista_pjesama)
    B1.pack()
    B2 = Button(root2, text ="2. lista pjesama", command = druga_lista_pjesama)
    B2.pack()

def novi_tk():
    
    global novac
    def restart():
        root.destroy()
        sleep(0.5)
        novi_tk()
    
    root = Tk() 
    root.title("Toni tkinter")
    canvas = Canvas(root, width = 1825, height = 990) # sirina i visina prozora
    canvas.pack()
    canvas.create_rectangle(20, 60, 80, 80, fill = "Blue")
    canvas.create_rectangle(20, 100, 80, 120, fill = "Red")
    canvas.create_rectangle(20, 140, 80, 160, fill = "Green")
    canvas.create_rectangle(20, 180, 80, 200, fill = "Yellow")
    canvas.create_line(85, 45, 85, 215)
    canvas.create_text(110, 225, text="Start (utrka na 200m)", font=("Arial", 13), fill= "Black")
   
    def pokreni_trku():
        global novac
        rez1 = 0; rez2 = 0; rez3 = 0; rez4 = 0
        igrac1 = randrange(5, 10)
        igrac2 = randrange(5, 10)
        igrac3 = randrange(5, 10)
        igrac4 = randrange(5, 10)
        rez1 = igrac1 + rez1
        rez2 = igrac2 + rez2
        rez3 = igrac3 + rez3
        rez4 = igrac4 + rez4
        canvas.create_text(190, 250, text = "Brzina PLAVOG prvih 50m: {}m/s".format(igrac1), font = ("Arial", 15), fill = "Black")
        canvas.create_text(200, 300, text = "Brzina CRVENOG prvih 50m: {}m/s".format(igrac2), font = ("Arial", 15), fill = "Black")
        canvas.create_text(200, 350, text = "Brzina ZELENOG prvih 50m: {}m/s".format(igrac3), font = ("Arial", 15), fill = "Black")
        canvas.create_text(190, 400, text = "Brzina ŽUTOG prvih 50m: {}m/s".format(igrac4), font = ("Arial", 15), fill = "Black")
        n = 200
        for i in range(0, n):
            canvas.move(1, igrac1, 0)
            root.update()
            canvas.move(2, igrac2, 0)
            root.update()
            canvas.move(3, igrac3, 0)
            root.update()
            canvas.move(4, igrac4, 0)
            root.update()
            sleep(0.1)
            n -= 1
            if n == 150:
                igrac1 = randrange(5, 10)
                igrac2 = randrange(5, 10)
                igrac3 = randrange(5, 10)
                igrac4 = randrange(5, 10)
                rez1 = igrac1 + rez1
                rez2 = igrac2 + rez2
                rez3 = igrac3 + rez3
                rez4 = igrac4 + rez4
                canvas.create_text(523, 250, text = ", brzina 50-100m: {}m/s".format(igrac1), font = ("Arial", 15), fill = "Black")
                canvas.create_text(523, 300, text = ", brzina 50-100m: {}m/s".format(igrac2), font = ("Arial", 15), fill = "Black")
                canvas.create_text(523, 350, text = ", brzina 50-100m: {}m/s".format(igrac3), font = ("Arial", 15), fill = "Black")
                canvas.create_text(523, 400, text = ", brzina 50-100m: {}m/s".format(igrac4), font = ("Arial", 15), fill = "Black")
            if n == 100:
                igrac1 = randrange(5, 10)
                igrac2 = randrange(5, 10)
                igrac3 = randrange(5, 10)
                igrac4 = randrange(5, 10)
                rez1 = igrac1 + rez1
                rez2 = igrac2 + rez2
                rez3 = igrac3 + rez3
                rez4 = igrac4 + rez4
                canvas.create_text(820, 250, text = ", brzina 100-150m: {}m/s".format(igrac1), font = ("Arial", 15), fill = "Black")
                canvas.create_text(820, 300, text = ", brzina 100-150m: {}m/s".format(igrac2), font = ("Arial", 15), fill = "Black")
                canvas.create_text(820, 350, text = ", brzina 100-150m: {}m/s".format(igrac3), font = ("Arial", 15), fill = "Black")
                canvas.create_text(820, 400, text = ", brzina 100-150m: {}m/s".format(igrac4), font = ("Arial", 15), fill = "Black")
            if n == 50:
                igrac1 = randrange(5, 10)
                igrac2 = randrange(5, 10)
                igrac3 = randrange(5, 10)
                igrac4 = randrange(5, 10)
                rez1 = igrac1 + rez1
                rez2 = igrac2 + rez2
                rez3 = igrac3 + rez3
                rez4 = igrac4 + rez4
                canvas.create_text(1120, 250, text = ", brzina 150-200m: {}m/s".format(igrac1), font = ("Arial", 15), fill = "Black")
                canvas.create_text(1120, 300, text = ", brzina 150-200m: {}m/s".format(igrac2), font = ("Arial", 15), fill = "Black")
                canvas.create_text(1120, 350, text = ", brzina 150-200m: {}m/s".format(igrac3), font = ("Arial", 15), fill = "Black")
                canvas.create_text(1120, 400, text = ", brzina 150-200m: {}m/s".format(igrac4), font = ("Arial", 15), fill = "Black")
        print ("Ukupna brzina 1. igraca:", str(rez1))
        print ("Ukupna brzina 2. igraca:", str(rez2))
        print ("Ukupna brzina 3. igraca:", str(rez3))
        print ("Ukupna brzina 4. igraca:", str(rez4))
    
        def win():
            global novac
            novac += 20
            tkinter.messagebox.showinfo(None, "Čestitamo na pobjedi.")
            restart()
            
        if (rez1 > rez2) and (rez1 > rez3) and (rez1 > rez4):
            if button_start_utrke_1.has_been_called:
                canvas.create_text(200, 650, text = "Pobjeda plavog igraca!", font = ("Arial", 15), fill = "Blue")
                canvas.create_text(200, 673, text = "Pobijedili ste, uzmite novce:", font = ("Arial", 15), fill = "Black")
                b8 = Button(root, text = "+20$", command = win, anchor = W)
                b8.configure(width = 10, activebackground = "Blue") 
                b8_window = canvas.create_window(400, 650, anchor=NW, window=b8)
            
        elif (rez2 > rez1) and (rez2 > rez3) and (rez2 > rez4):
            if button_start_utrke_2.has_been_called:
                canvas.create_text(200, 650, text = "Pobjeda crvenog igraca!", font = ("Arial", 15), fill = "Red")
                canvas.create_text(200, 673, text = "Pobijedili ste, uzmite novce:", font = ("Arial", 15), fill = "Black")
                b9 = Button(root, text = "+20$", command = win, anchor = W)
                b9.configure(width = 10, activebackground = "Blue") 
                b9_window = canvas.create_window(400, 650, anchor=NW, window=b9)
            
        elif (rez3 > rez1) and (rez3 > rez2) and (rez3 > rez4):
            if button_start_utrke_3.has_been_called:
                canvas.create_text(200, 650, text = "Pobjeda zelenog igraca!", font = ("Arial", 15), fill = "Green")
                canvas.create_text(200, 673, text = "Pobijedili ste, uzmite novce:", font = ("Arial", 15), fill = "Black")
                b10 = Button(root, text = "+20$", command = win, anchor = W)
                b10.configure(width = 10, activebackground = "Blue") 
                b10_window = canvas.create_window(400, 650, anchor=NW, window=b10)
            
        elif (rez4 > rez1) and (rez4 > rez2) and (rez4 > rez3):
            if button_start_utrke_4.has_been_called:
                canvas.create_text(200, 650, text = "Pobjeda žutog igraca!", font = ("Arial", 15), fill = "Yellow")
                canvas.create_text(200, 673, text = "Pobijedili ste, uzmite novce:", font = ("Arial", 15), fill = "Black")
                b8 = Button(root, text = "+20$", command = win, anchor = W)
                b8.configure(width = 10, activebackground = "Blue") 
                b8_window = canvas.create_window(400, 650, anchor=NW, window=b8)
            
        elif (rez1 == rez2) or (rez1 == rez3) or (rez1 == rez4) or (rez2 == rez3) or (rez2 == rez4) or (rez3 == rez4):
            canvas.create_text(200, 650, text = "Nema pobjednika!", font = ("Arial", 15), fill = "Black")
            tkinter.messagebox.showinfo("Nema pobjednika!", "Nema pobjednika, novci su vam vračeni.")
            novac += 5
            root.destroy()
            sleep(0.5)
            novi_tk()
        else:
            pass

        if button_start_utrke_1.has_been_called:
            if (rez1 < rez2) or (rez1 < rez3) or (rez1 < rez4):
                canvas.create_text(350, 650, text = "Izgubili ste, za novu igru stisnite gore: 'Restartaj igru'",
                                             font = ("Arial", 15), fill = "Black")
                
        elif button_start_utrke_2.has_been_called:
            if (rez2 < rez1) or (rez2 < rez3) or (rez2 < rez4):
                canvas.create_text(350, 650, text = "Izgubili ste, za novu igru stisnite gore: 'Restartaj igru'",
                                             font = ("Arial", 15), fill = "Black")
        elif button_start_utrke_3.has_been_called:
            if (rez3 < rez1) or (rez3 < rez2) or (rez3 < rez4):
                canvas.create_text(350, 650, text = "Izgubili ste, za novu igru stisnite gore: 'Restartaj igru'",
                                             font = ("Arial", 15), fill = "Black")
        elif button_start_utrke_4.has_been_called:
            if (rez4 < rez1) or (rez4 < rez2) or (rez4 < rez3):
                canvas.create_text(350, 650, text = "Izgubili ste, za novu igru stisnite gore: 'Restartaj igru'",
                                             font = ("Arial", 15), fill = "Black")
        else:
            pass
           
    canvas.create_text(1000, 30, text = "Prije pocetka utrke kladi se na jednog od igraca.", font = ("Arial", 15), fill = "Black")
    canvas.create_text(100, 475, text = "Jedna igra = 5$", font = ("Arial", 15), fill = "Black")
    canvas.create_text(125, 495, text = "Vaš novac = {}$".format(novac), font = ("Arial", 15), fill = "Black")
    
    def button_start_utrke_1():
        global novac
        novac -= 5
        button_start_utrke_1.has_been_called = True
        b2.destroy()
        b3.destroy()
        b4.destroy()
        canvas.create_text(225, 450, text = "Kladili ste se na plavog igraca!", font = ("Arial", 20), fill = "Blue")
        button1 = Button(root, text = "START", command = pokreni_trku, anchor = W)
        button1.configure(width = 10, activebackground = "Blue") 
        button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)
        
    def button_start_utrke_2():
        global novac
        novac -= 5
        button_start_utrke_2.has_been_called = True
        b1.destroy()
        b3.destroy()
        b4.destroy()
        canvas.create_text(225, 450, text = "Kladili ste se na crvenog igraca!", font = ("Arial", 20), fill = "Red")
        button1 = Button(root, text = "START", command = pokreni_trku, anchor = W)
        button1.configure(width = 10, activebackground = "Blue") 
        button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)
        
    def button_start_utrke_3():
        global novac
        novac -= 5
        button_start_utrke_3.has_been_called = True
        b1.destroy()
        b2.destroy()
        b4.destroy()
        canvas.create_text(225, 450, text = "Kladili ste se na zelenog igraca!", font = ("Arial", 20), fill = "Green")
        button1 = Button(root, text = "START", command = pokreni_trku, anchor = W)
        button1.configure(width = 10, activebackground = "Blue") 
        button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)
        
    def button_start_utrke_4():
        global novac
        novac -= 5
        button_start_utrke_4.has_been_called = True
        b1.destroy()
        b2.destroy()
        b3.destroy()
        canvas.create_text(225, 450, text = "Kladili ste se na žutog igraca!", font = ("Arial", 20), fill = "Yellow")
        button1 = Button(root, text = "START", command = pokreni_trku, anchor = W)
        button1.configure(width = 10, activebackground = "Blue")
        button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)

    button_start_utrke_1.has_been_called = False
    button_start_utrke_2.has_been_called = False
    button_start_utrke_3.has_been_called = False
    button_start_utrke_4.has_been_called = False
    
    b1 = Button(root, text = "PLAVI", command = button_start_utrke_1, anchor = W)
    b1.configure(width = 10, activebackground = "Blue") 
    b1_window = canvas.create_window(100, 10, anchor=NW, window=b1)

    b2 = Button(root, text = "CRVENI", command = button_start_utrke_2, anchor = W)
    b2.configure(width = 10, activebackground = "Blue") 
    b2_window = canvas.create_window(200, 10, anchor=NW, window=b2)

    b3 = Button(root, text = "ZELENI", command = button_start_utrke_3, anchor = W)
    b3.configure(width = 10, activebackground = "Blue") 
    b3_window = canvas.create_window(300, 10, anchor=NW, window=b3)

    b4 = Button(root, text = "ŽUTI", command = button_start_utrke_4, anchor = W)
    b4.configure(width = 10, activebackground = "Blue") 
    b4_window = canvas.create_window(400, 10, anchor=NW, window=b4)

    b5 = Button(root, text = "Restartaj igru", command = restart, anchor = W)
    b5.configure(width = 11, activebackground = "Blue") 
    b5_window = canvas.create_window(500, 10, anchor=NW, window=b5)

    def izlaz_iz_igre():
        root.destroy()
        exit()
    b6 = Button(root, text = "Quit game", command = izlaz_iz_igre, anchor = W)
    b6.configure(width = 10, activebackground = "Blue") 
    b6_window = canvas.create_window(610, 10, anchor=NW, window=b6)

    b7 = Button(root, text = "Muzika", command = muzika, anchor = W)
    b7.configure(width = 6, activebackground = "Blue") 
    b7_window = canvas.create_window(1700, 10, anchor=NW, window=b7)

    def game_over():
        global novac
        canvas.delete("all")
        canvas.create_text(900, 260, text = "Ostali ste bez novaca", font = ("Arial", 85), fill = "Black")
        tkinter.messagebox.showinfo(None, "Ostali ste bez novaca.")
        sleep(2)
        P1 = tkinter.messagebox.askquestion(None, "Želite li opet igrati igru?")
        if P1 == "yes":
            root.destroy()
            novac += 20
            novi_tk()
        if P1 == "no":
            tkinter.messagebox.showinfo(None, "Doviđenja")
            sleep(1)
            root.destroy()
            exit()

    if novac == 0:
        game_over()
    #e1 = Entry(canvas)
    #canvas.create_window(115, 550, window=e1, height=50, width=100)
    
    root.mainloop()


root.mainloop()



