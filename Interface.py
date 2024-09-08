import tkinter as tk

# for setting the initial interface
root = tk.Tk()
root.geometry("500x500")
root.title("My First GUI")

# for the heading (label) on the interface
label = tk.Label(root, text="WELCOME BUDDY", font=('Arial',20))
label.pack(padx=50, pady=50)

# for palcing a textbox of n number of lines
textbox = tk.Text(root, height=3, font=('Arial', 12))
textbox.pack(padx=10, pady=10)

# for putting a click button on the interface
# button = tk.Button(root, text="Click here!", font=("Arial", 14))
# button.pack(padx=10, pady=10)

# for making a frame of button in grid interface
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="2", font=('Arial', 16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="3", font=('Arial', 16))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="4", font=('Arial', 16))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text="5", font=('Arial', 16))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text="6", font=('Arial', 16))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

# .place funtion 
# anotherbtn = tk.Button(root, text='TEST')
# anotherbtn.place(x=300, y=300, height=150, width=150)

root.mainloop()
