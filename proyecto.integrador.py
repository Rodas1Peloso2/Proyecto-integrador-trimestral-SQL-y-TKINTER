import sqlite3
conn = sqlite3.connect("grupo1.db")
cursor = conn.cursor()

from tkinter import*
from tkinter import messagebox 
ventana=Tk()
ventana.title=("Recetario")
ventana.geometry("400x400")

# Variables
id_ingrediente=StringVar()
nombre_ingrediente=StringVar()
tiempo_coccion=StringVar()
dificultad=StringVar()
id_receta=StringVar()
id_receta2=StringVar()
nombre_clasificacion=StringVar()

id_ingrediente.set("")
nombre_ingrediente.set("")
tiempo_coccion.set("")
dificultad.set("")
id_receta.set("")
id_receta2.set("")
nombre_clasificacion.set("")

def alta_ingrediente():
    try:
        conn.execute('''INSERT INTO Ingredientes (id_ingredientes, nombre_ingrediente, tiempo_coccion, dificultad, id_receta) 
                     VALUES ('%s','%s','%s','%s','%s')'''%(id_ingrediente.get(),nombre_ingrediente.get(),tiempo_coccion.get(),dificultad.get(),id_receta.get()))
        conn.commit()
        messagebox.showinfo("OK","Ingrediente agregado")
    except:
        messagebox.showerror("Error","Datos incorrectos")
        id_ingrediente.set("")
        nombre_ingrediente.set("")
        tiempo_coccion.set("")
        dificultad.set("")
        id_receta.set("")

def alta_receta():
    try:
        conn.execute('''INSERT INTO Receta (id_receta, nombre_clasificacion) 
                     VALUES ('%s','%s')'''%(id_receta2.get(),nombre_clasificacion.get()))
        conn.commit()
        messagebox.showinfo("OK","Receta agregada")
    except:
        messagebox.showerror("Error","Datos incorrectos")
        id_receta2.set("")
        nombre_clasificacion.set("")

def mostrar_resultado():
    resultado=""
    cursor.execute('''SELECT Ingredientes.nombre_ingrediente, Receta.nombre_clasificacion, Ingredientes.dificultad 
                      FROM Ingredientes 
                      INNER JOIN Receta ON Ingredientes.id_receta=Receta.id_receta''')
    filas=cursor.fetchall()
    for fila in filas:
        resultado+=f"Ingr:{fila[0]} | Receta:{fila[1]} | Dificultad:{fila[2]}\n"
    messagebox.showinfo("INNER JOIN",resultado if resultado!="" else "No hay datos cargados")  

marco=Frame(ventana ,width=350,height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate(False)

# Ingredientes
Label(marco,text="ID Ingrediente").pack()
Entry(marco,textvariable=id_ingrediente,justify="center").pack()
Label(marco,text="Nombre Ingrediente").pack()
Entry(marco,textvariable=nombre_ingrediente,justify="center").pack()
Label(marco,text="Tiempo Coccion").pack()
Entry(marco,textvariable=tiempo_coccion,justify="center").pack()
Label(marco,text="Dificultad").pack()
Entry(marco,textvariable=dificultad,justify="center").pack()
Label(marco,text="ID Receta (relación)").pack()
Entry(marco,textvariable=id_receta,justify="center").pack()

# Receta
Label(marco,text="ID Receta").pack()
Entry(marco,textvariable=id_receta2,justify="center").pack()
Label(marco,text="Clasificacion").pack()
Entry(marco,textvariable=nombre_clasificacion,justify="center").pack()

# Botones
Button(marco,text="Alta Ingrediente", command=alta_ingrediente).pack(side="left", fill=X, expand=YES)
Button(marco,text="Alta Receta",command=alta_receta).pack(side="left", fill=X, expand=YES)
Button(marco,text="Mostrar Join",command=mostrar_resultado).pack(side="left", fill=X, expand=YES)

ventana.mainloop()