# -----------------libraries--------------
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfile

# -----------------window------------------
root = Tk()
root.title("banana ripeness gui")


# -----------------functions-----------
def upload_file():
    global img
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((200, 100))  # new width & height
    img = ImageTk.PhotoImage(img_resized)
    b2 = tk.Button(root, image=img,relief=FLAT)  # using Button
    button1_canvas = canvas1.create_window(150, 100, anchor="nw", window=b2)

# --------------constants-----------------
bg = PhotoImage(file="bg_img.png")
but = PhotoImage(file="button_icon (1).png")
res = PhotoImage(file="image-removebg-preview (1) (1).png")
p = PhotoImage(file="image-removebg-preview.png")
font_col="#6B8E23"
label_bg="#ffe030"

# ----------------UI design----------------
canvas1 = Canvas( root, width=840, height=360)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")


up_button = Button(root, text="UPLOAD ", font=("Helvetica", 10, "bold"), image=but, compound=LEFT,
                   activebackground="yellow", command = lambda:upload_file())
button1_canvas = canvas1.create_window(200, 250, anchor="nw", window=up_button)

label1 = Label(text="Banana ripeness detection", font=("Helvetica",20 , "bold"),bg=label_bg,
               fg=font_col,highlightthickness=0)
label1_canvas = canvas1.create_window(320, 20, anchor="nw", window=label1)

res_button = Button(root, text="RESULT ", font=("Helvetica", 10, "bold"), image=res, compound=LEFT,
                    activebackground="yellow")
button2_canvas = canvas1.create_window(500, 250, anchor="nw", window=res_button)




root.mainloop()