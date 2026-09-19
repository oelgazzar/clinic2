import tkinter as tk

from data.database import Database
from data.repositories.patient_repository import PatientRepository


db = Database("storage/clinic.db")
repo = PatientRepository(db)

root = tk.Tk()

start_frame = tk.Frame()
text = "\n".join(str(p) for p in repo.get_all())
label = tk.Label(start_frame, text=text)
label.pack()

new_frame = tk.Frame()
tk.Label(new_frame, text="name").grid(row=0, column=0)
tk.Entry(new_frame).grid(row=0, column=1)
tk.Button(new_frame, text="submit").grid(row=1, columnspan=2)

def show_create_window():
    new_frame.tkraise()

button = tk.Button(start_frame, text="Create", command=show_create_window)
button.pack()
start_frame.place(relwidth=1, relheight=1)
new_frame.place(relwidth=1, relheight=1)
start_frame.tkraise()
root.mainloop()