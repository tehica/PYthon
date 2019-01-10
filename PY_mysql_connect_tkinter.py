from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = "root", password = "12345", database = "vvg")

mycursor = mydb.cursor()
    
root = Tk()
root.title("Toni tkinter")
root.geometry("1000x500")
root.wm_attributes("-topmost", 1)
root.attributes("-fullscreen", True)
Label(root, text = "Promjena podataka u tablici: ", fg = "Green", font = ("Courier", 16)).place(x = 1, y = 10)
E0_var = StringVar()
E1_var = StringVar()
E2_var = StringVar()
E3_var = StringVar()
E4_var = StringVar()

L = ["-"*12, "studenti", "gaudeamus"]
Entry_tablica = StringVar()
OP_Menu = OptionMenu(root, Entry_tablica, *L).place(x = 1, y = 46)

#variable = StringVar()
#w = OptionMenu(root, variable, "one").place(x = 1, y = 650)
#########################################################################################################################
def update_studenti():
        
    global E0_var, E1_var, E2_var, E3_var, E4_var, Entry_tablica
    
    def unos_podataka():
        
        try:
            
            v0 = E0_var.get() # get - koji stupac
            
            v1 = E1_var.get() # get - novi podatak
            
            v2 = E2_var.get()
            v3 = E3_var.get()
            v4 = E4_var.get()
            tablica = Entry_tablica.get()
            sql = "UPDATE {} SET {} = '{}' WHERE student_id = {} AND ime = '{}' AND prezime = '{}'".format(tablica,
                                                                                                           v0, v1, v2, v3, v4)

            mycursor.execute(sql)
            mydb.commit()

            L1 = Label(root, text = "Uspjesan unos u bazu podataka").place(x = 1, y = 590)
            
            E0_var.set(''); E1_var.set(''); E2_var.set(''); E3_var.set('');
            E4_var.set('')
        except mysql.connector.errors.ProgrammingError:
            L2 = Label(root, text = "Niste unijeli jedno od polja.").place(x = 1, y = 600)
        
    Label(root, text = "Naziv stupca u kojem zelimo update:", font = ("Arial", 12)).place(x = 1, y = 340)
    E0_var = StringVar()
    E0 = Entry(root, textvariable = E0_var).place(x = 340, y = 340)
    
    Label(root, text = "Update podataka u tablici", fg = "Red", font = ("Arial", 12)).place(x = 1, y = 370)
    F1 = Frame(root, width = 500, height = 240, bg = "Gray").place(x = 1, y = 400)
    
    Label(root, text = "Novi unos (set): ", font = ("Arial", 12)).place(x = 1, y = 405)   
    E1 = Entry(root, textvariable = E1_var, width = 25).place(x = 155, y = 405)
    
    Label(root, text = "Kod studenta s podacima: ", font = ("Courier", 14)).place(x = 1, y = 435)

    Label(root, text = "JMBAG studenta: ", font = ("Arial", 12)).place(x = 1, y = 467)
    E2 = Entry(root, textvariable = E2_var, width = 25).place(x = 173, y = 467)
    
    Label(root, text = "Ime studenta: ", font = ("Arial", 12)).place(x = 1, y = 497)
    E3 = Entry(root, textvariable = E3_var, width = 25).place(x = 137, y = 497)
    
    Label(root, text = "Prezime studenta: ", font = ("Arial", 12)).place(x = 1, y = 527)
    E4 = Entry(root, textvariable = E4_var, width = 25).place(x = 175, y = 527)
    
    Button(root, text = "Unesi novi podatak", command = unos_podataka).place(x = 1, y = 560)

    def entry_reset():
        E0_var.set(''); E1_var.set(''); E2_var.set(''); E3_var.set('');
        E4_var.set('')
    Button(root, text = "Brisanje polja", command = entry_reset).place(x = 385, y = 560)
################################################################################################################################    
#                     ||
#                     ||
# varijable za insert \/
E6_var = StringVar(); E7_var = StringVar()
E8_var = StringVar(); E9_var = StringVar()
E10_var = StringVar(); E11_var = StringVar(); E12_var = StringVar()

def input_studenti():
    
    global Entry_tablica
    def unos_podataka2():
        
        try:
            v6 = E6_var.get() # jmbag studenta
            v7 = E7_var.get() # ime
            v8 = E8_var.get() # prezime
            v9 = E9_var.get() # smjer(int)
            v10 = E10_var.get() # Telefon
            v11 = E11_var.get() # E-mail
            v12 = E12_var.get() # Adresa
            tablica2 = Entry_tablica.get()
            sql_2 = """INSERT INTO {} (student_id, ime, prezime, smjer, telefon, email, adresa) 
                       VALUES ({}, '{}', '{}', {}, '{}', '{}', '{}')""".format(tablica2, v6, v7, v8, v9, v10, v11, v12)
            
            mycursor.execute(sql_2)
            mydb.commit()

            L1 = Label(root, text = "Uspjesan unos u bazu podataka").place(x = 165, y = 920)
            
            E7_var.set(''); E8_var.set(''); E9_var.set(''); E10_var.set('');
            E11_var.set(''); E12_var.set('')
        except mysql.connector.errors.ProgrammingError:
            L2 = Label(root, text = "Niste unijeli jedno od polja.").place(x = 1, y = 600)
        
    Label(root, text = "Insert podataka u tablici:", fg = "Red", font = ("Arial", 12)).place(x = 1, y = 665)
    F1 = Frame(root, width = 500, height = 260, bg = "Gray").place(x = 1, y = 700)

    Label(root, text = "JMBAG studenta: ", font = ("Arial", 12)).place(x = 1, y = 705)
    E6 = Entry(root, textvariable = E6_var, width = 25, state = DISABLED).place(x = 172, y = 707)
    E6_var.set("NULL")
    
    Label(root, text = "Ime studenta: ", font = ("Arial", 12)).place(x = 1, y = 735)
    E7 = Entry(root, textvariable = E7_var, width = 25).place(x = 172, y = 737)
    
    Label(root, text = "Prezime studenta: ", font = ("Arial", 12)).place(x = 1, y = 765)
    E8 = Entry(root, textvariable = E8_var, width = 25).place(x = 174, y = 767)

    Label(root, text = "Smjer (broj 1-3): ", font = ("Arial", 12)).place(x = 1, y = 795)
    E9 = Entry(root, textvariable = E9_var, width = 25).place(x = 172, y = 797)

    Label(root, text = "Telefon: ", font = ("Arial", 12)).place(x = 1, y = 825)
    E10 = Entry(root, textvariable = E10_var, width = 25).place(x = 172, y = 825)

    Label(root, text = "E-mail: ", font = ("Arial", 12)).place(x = 1, y = 855)
    E11 = Entry(root, textvariable = E11_var, width = 25).place(x = 172, y = 855)

    Label(root, text = "Adresa: ", font = ("Arial", 12)).place(x = 1, y = 885)
    E12 = Entry(root, textvariable = E12_var, width = 25).place(x = 172, y = 885)

    Button(root, text = "Unesi nove podatake", command = unos_podataka2).place(x = 1, y = 920)

    def entry_reset2():
        E7_var.set(''); E8_var.set(''); E9_var.set(''); E10_var.set('');
        E11_var.set(''); E12_var.set('')
    Button(root, text = "Brisanje polja", command = entry_reset2).place(x = 385, y = 920)
    
##############################################################################################################################
E13_var = StringVar()
E14_var = StringVar()
E15_var = StringVar()
def update_gaudeamus():
    global Entry_tablica
    
    def unos_podataka3():
        
        try:
            v13 = E13_var.get()
            v14 = E14_var.get()
            v15 = E15_var.get()
            tablica3 = Entry_tablica.get()

            sql_3 = "UPDATE {} SET {} = '{}' WHERE gaud_id = {}".format(tablica3, v13, v14, v15)
            
            mycursor.execute(sql_3)
            mydb.commit()

            L1 = Label(root, text = "Uspjesan unos u bazu podataka").place(x = 1, y = 590)
            
            E13_var.set(''); E14_var.set(''); E15_var.set('')
        except mysql.connector.errors.ProgrammingError:
            L2 = Label(root, text = "Niste unijeli jedno od polja.").place(x = 1, y = 600)
        
    Label(root, text = "Update podataka u tablici:", fg = "Red", font = ("Arial", 12)).place(x = 1, y = 370)
    F1 = Frame(root, width = 500, height = 240, bg = "Gray").place(x = 1, y = 400)
    Label(root, text = "Naziv stupca u kojem zelimo update:", font = ("Arial", 12)).place(x = 1, y = 340)
    E13 = Entry(root, textvariable = E13_var).place(x = 340, y = 340)

    Label(root, text = "Novi unos (set): ", font = ("Arial", 12)).place(x = 1, y = 405)   
    E14 = Entry(root, textvariable = E14_var, width = 25).place(x = 155, y = 405)

    Label(root, text = "Kod reda s id brojem: ", font = ("Courier", 14)).place(x = 1, y = 435)

    Label(root, text = "ID reda(broj): ", font = ("Arial", 12)).place(x = 1, y = 467)
    E15 = Entry(root, textvariable = E15_var, width = 25).place(x = 173, y = 467)

    Button(root, text = "Unesi novi podatak", command = unos_podataka3).place(x = 1, y = 560)

    def entry_reset3():
        E13_var.set(''); E14_var.set(''); E15_var.set('')
    Button(root, text = "Brisanje polja", command = entry_reset3).place(x = 385, y = 560)
##############################################################################################################################
E16_var = StringVar()
E17_var = StringVar()
NULL = "NULL"
def insert_gaudeamus():
    global Entry_tablica, NULL
    def unos_podataka4():
        
        try:
            v16 = E16_var.get()
            v17 = E17_var.get()
            tablica4 = Entry_tablica.get()

            sql_4 = """INSERT INTO {} (gaud_id, piće, cijena) 
                       VALUES ({}, '{}', '{}')""".format(tablica4, NULL, v16, v17)

            mycursor.execute(sql_4)
            mydb.commit()

            L1 = Label(root, text = "Uspjesan unos u bazu podataka").place(x = 165, y = 920)
            
            E16_var.set(''); E17_var.set('')
        except mysql.connector.errors.ProgrammingError:
            L2 = Label(root, text = "Niste unijeli jedno od polja.").place(x = 1, y = 600)
            
    Label(root, text = "Insert podataka u tablici:", fg = "Red", font = ("Arial", 12)).place(x = 1, y = 665)
    F1 = Frame(root, width = 500, height = 260, bg = "Gray").place(x = 1, y = 700)

    Label(root, text = "Unos novog pića na popis: ", font = ("Arial", 12)).place(x = 1, y = 705)
    
    Label(root, text = "Naziv pića: ", font = ("Arial", 12)).place(x = 1, y = 735)
    E16 = Entry(root, textvariable = E16_var, width = 25).place(x = 172, y = 737)
    
    Label(root, text = "Cijena: ", font = ("Arial", 12)).place(x = 1, y = 765)
    E17 = Entry(root, textvariable = E17_var, width = 25).place(x = 172, y = 767)

    Button(root, text = "Unesi nove podatake", command = unos_podataka4).place(x = 1, y = 920)

    def entry_reset4():
        E16_var.set(''); E17_var.set('')
    Button(root, text = "Brisanje polja", command = entry_reset4).place(x = 385, y = 920)
    
def select_studenti_all():
    
    sql_5 = "SELECT * FROM studenti"
    mycursor.execute(sql_5)
        
    review_db = mycursor.fetchall()
    T = Text(root, width = 50, height = 30).place(x = 550, y = 10)
    T.insert(INSERT, "{} \n".format(review_db))
    
def select_studenti():
    Button(root, text = "ALL", command = select_studenti_all).place(x = 1, y = 165)
##############################################################################################################################    
def update():
    if (Entry_tablica.get() == "studenti"):
        update_studenti()
    elif (Entry_tablica.get() == "gaudeamus"):
        update_gaudeamus()
    else:
        print("Nepostojeca tablica.")

def insert():
    if (Entry_tablica.get() == "studenti"):
        input_studenti()
    elif (Entry_tablica.get() == "gaudeamus"):
        insert_gaudeamus()
    else:
        print("Nepostojeca tablica.")

def select():
    if (Entry_tablica.get() == "studenti"):
        select_studenti()
    else:
        print("Nije odabrana ni jedna tablica.")
#############################################################################################################################
def update_insert():
    counter = 5
    for i in range(1, 31):
        Label(root, text="|", font=("Arial", 12)).place(x = 495, y = counter)
        counter += 10
    Label(root, text = "-"*70, font = ("Arial", 12)).place(x = 1, y = 310)
    Button(root, text = "Update", command = update, width = 18, font = ("Arial", 12)).place(x = 1, y = 85)
    Button(root, text = "Insert", command = insert, width = 18, font = ("Arial", 12)).place(x = 220, y = 85)
    Button(root, text = "SELECT", width = 18, command = select, font = ("Arial", 12)).place(x = 1, y = 125)
    def exit_root():
        root.destroy()
    Button(root, text = "Exit", command = exit_root, width = 25).place(x = 220, y = 44)
    
update_insert()

root.mainloop()

