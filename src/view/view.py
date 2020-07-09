import tkinter as tk

#https://github.com/KeithGalli/GUI
#https://www.tutorialspoint.com/python/python_gui_programming.htm
#https://www.youtube.com/watch?v=D8-snVfekto

HEIGHT = 700
WIDTH = 800

def teste(entry):
    print(entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Fazer scrapping", font=40, command = lambda: teste(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
