import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System" , font=("Arial", 22))
label.pack(padx=10, pady=12, )
                               
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(padx=10, pady=12)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(padx=10, pady=12)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(padx=10, pady=12)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(padx=10, pady=12)

root.mainloop()