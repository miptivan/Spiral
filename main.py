from tkinter import *

tk = Tk()

canvas = Canvas(tk, height=500, width=500)
canvas.pack()
canvas.create_line(500, 500, 100, 100)


tk.mainloop()
