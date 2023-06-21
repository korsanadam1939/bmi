import tkinter
from tkinter import *

font=("Arial",15,"normal")


#ekran
ekran=Tk()
ekran.config(pady=50)
ekran.minsize(300,300)
ekran.title("vücüt kitle indexi hesaplayıcı")

#label1
label1=Label(text="kilonu gir(kg)",font=font)
label1.pack()

#entry 1
entry1=Entry(width=15)
entry1.pack()

#label2
label2=Label(text="boyunu gir(cm)",font=font)
label2.pack()

#entry2
entry2=Entry(width=15)
entry2.pack()

#buton1
def butona_tiklandiginda():

    try:
        kilo = float(entry1.get())

        boy = float(entry2.get())
        formul = kilo / (boy * boy)
        if formul < 18:
            label3.config(text="zayıf")
        elif 18.5 <= formul <= 24.9:
            label3.config(text="normal")
        elif 25 <= formul <= 29.9:
            label3.config(text="kilolu")
        elif 30 <= formul <= 34.9:
            label3.config(text="1.dereceden obez")
        elif 25 <= formul <= 29.9:
            label3.config(text="2.dereceden obez")
        elif 25 <= formul <= 29.9:
            label3.config(text="extra obez")
        else:
            label3.config(text="siz insan değilsiniz")


    except:
        label3.config(text="girdiler hatalı")



buton1=Button(text="hesapla",height=1,width=15,command=butona_tiklandiginda,bg="gray")
buton1.pack()

#label2
label3=Label(text="",font=font)
label3.pack()

mainloop()