import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        #This will help to make a menu bar at the top
        # self.menubar = tk.Menu(self.root)

        # self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # self.menubar.add_command(label="Close", command=self.on_closing)

        # self.menubar.add_cascade(menu=self.filemenu, label="File")
        # self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text='Your Message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 14))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 14), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial',16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        #The initial step before the funtion that calls before closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def show_message(self):
        # print(self.check_state.get())  if the checkbox if checked then it'll show 1 otherwise 0
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))  

        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    #this funtion is used when you want a popup before you close the interface
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()   
        

MyGUI()
