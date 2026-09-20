import tkinter as tk

from data.database import Database
from data.repositories.patient_repository import PatientRepository
from ui.patient_view import PatientView


db = Database("storage/clinic.db")
repo = PatientRepository(db)

root = tk.Tk()
root.title("Clinic")
p = PatientView(root, repo)
p.pack(fill='both', expand=True)
root.mainloop()