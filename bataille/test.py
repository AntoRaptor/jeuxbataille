from tkinter import *
main = Tk()

def f (x=3):
    x = x * 2
    return x

def affichage(label):
    label["text"] = valeur

valeur = f(4)
valeur = str(valeur)

bouton = Button(main, command=affichage)
bouton.pack()

label1 = Label(main)
label1.pack()

main.mainloop()