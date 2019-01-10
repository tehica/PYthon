from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("500x300")
root.wm_attributes("-topmost", 1)
root.attributes("-fullscreen", True)

#Label(root, text = str(massag)).place(x = 5, y = 5)
#print(massag)

variable_1 = StringVar()
variable_2 = StringVar()

# DICTIONARY            
d = {}

def get():

    USER = variable_2.get()
    PASSWD = variable_1.get()
    
    upper = 0; lower = 0; number = 0
    for x in PASSWD:
            
        if x.isupper() == True:
            upper += 1
        elif x.islower() == True:
            lower += 1
        elif x.isdigit() == True:
            number += 1

    letter = 0     
    for x in USER:
        if x.isalpha() == True:
            letter += 1

    if (letter >= 3) and (len(USER) >= 5) and (len(USER) <= 10):
                
        if (upper >= 1) and (lower >= 1) and (number >= 1) and (len(PASSWD) >= 8) and (len(PASSWD) <= 30):
            L1 = Label(root, text = "Dobar unos.", fg = "Blue").place(x = 125, y = 250)
            
            d["{}".format(USER)] = "{}".format(PASSWD)
            print(d)
            
        else:
            L3 = Label(root, text = "Loš unos.", width = 12, fg = "Red").place(x = 125, y = 250)
            
    else:
        L3 = Label(root, text = "Loš unos.", width = 12, fg = "Red").place(x = 125, y = 250)

Label(root, text = "Password:", font = ("Arial", 12)).place(x = 170, y = 170)
E1 = Entry(root, textvariable = variable_1, width = 20).place(x = 275, y = 175) # password var

Label(root, text = "Username:", font = ("Arial", 12)).place(x = 170, y = 130)
E2 = Entry(root, textvariable = variable_2, width = 20).place(x = 275, y = 135) # username var

Button(root, text = "Spremi", command = get, width = 13, font = ("Arial", 12)).place(x = 5, y = 125)

def dest_root():
    root.destroy()
Button(root, text = "Exit", command = dest_root, width = 15, font = ("Arial", 12), fg = "White", bg = "Black").place(x = 1, y = 1)

Label(root, text = "Info:", font='Helvetica 15 bold', fg = "Red").place(x = 200, y = 2)

def username_info():
    
    massag = """
             1.) Zadajte username koji ce imati 5 - 10 znakova
             2.) Imati barem tri (3) slova
             """
    tkinter.messagebox.showinfo("Username info", "USERNAME\n {}".format(massag))

def password_info():
    
    massag = """
         1.) Zadajte lozinku koja ce imati 8 - 30 znakova
         2.) Imati barem jedno veliko slovo
         3.) Imati barem jedno malo slovo
         4.) imati barem jedan broj
         """
    tkinter.messagebox.showinfo("Password info", "LOZINKA\n {}".format(massag))
    
Button(root, text = "Username", command = username_info, width = 15, font = ("Arial", 12)).place(x = 265, y = 3)
Button(root, text = "Password", command = password_info, width = 15, font = ("Arial", 12)).place(x = 265, y = 45)

def ispis2():
    
    s = """ """
    with open('lista.txt', 'r') as f:
        s = f.read()
    tkinter.messagebox.showinfo("UNOSI", "USERNAMES / PASSWORDS\n {}".format( s ))
    print(s)
    
Button(root, text = "Ispis unosa", command = ispis2, width = 15, font = ("Arial", 12)).place(x = 470, y = 3)


def unos_file():
    
    with open('lista.txt', 'a') as f:
            for key, value in d.items():
                f.write("{} {}\n".format(key, value))	
    Label(root, text="Podaci uneseni u .txt").place(x = 1, y = 300)
    
Button(root, text = "Unos podataka", command = unos_file, width = 13, font = ("Arial", 12)).place(x = 5, y = 175)

root.mainloop()

#
#
#

# za ispis unesenih usrnamea i psswd-a na rootu u labelu
def ispis():
    L = []
    counter = 0
    yPOSITION = 70
    for key, value in d.items():
        L.append("Username: {} Password: {}".format(key, value))   
        Label(root, text = "{}".format(L[counter])).place(x = 500, y = yPOSITION)
        counter += 1
        yPOSITION += 30
    print(L)
    print(d)


"""
T = """ '{}' """.format(L[counter])
        TKBOX = tkinter.messagebox.showinfo( "USERS", "{}\n".format( T ) )
"""
"""
            L.append( str(PASSWD) )
            print(L)
                    
            with open('lista.txt', 'w') as f:
                for item in L:
                    f.write("%s\n" % item)
"""


def nebitna_funkcija():
            # Moze biti, a i ne mora, broji samo koliko sifra kakvih znakova ima.
            labelTEXT = """
                        -> Upper: {}
                        -> Lower: {}
                        -> Number: {}
                        """.format(upper, lower, number)
            Label(root, text = str(labelTEXT), font = ("Arial", 10)).place(x = -80, y = 170) 
         
