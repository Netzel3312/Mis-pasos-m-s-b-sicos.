import tkinter as tk 


root = tk.Tk()

root.title("mi primera gui")
root.config(bg="#008066")

#creo el Frame
frame=tk.Frame()
frame.pack(side="bottom", anchor="n")
frame.config(bg="#ffffff", width="600", height="600", relief="groove", cursor= "hand2", bd=35)

"""tk.Label(frame, text="mi primera etiqueta", fg="#000000", font=("verdana",18)).place(x=100, y=200)

tk.Entry(frame).place(x=200, y=300)

tk.Checkbutton(frame, text="para ve..." ).place(x=50, y =50)"""

nombre = tk.Label(frame, text="nombre",bg="#008066").grid(row=0, column=0, sticky="w")
edad = tk.Label(frame, text="edad:", bg="#008066").grid(row=1, column=0, sticky="w")
dni = tk.Label(frame, text="DNI:", bg="#008066").grid(row=2, column=0, sticky="w")

cuadro_nombre= tk.Entry(frame).grid(row=0, column=1)
cuadro_edad= tk.Entry(frame).grid(row=1, column=1)
cuadro_dni= tk.Entry(frame).grid(row=2, column=1)


# creo una raiz instanciando la clase tk()
root.mainloop()

#llamo al metodo mainloop para darle forma al gui a mi raiz root.mainloop()

 
