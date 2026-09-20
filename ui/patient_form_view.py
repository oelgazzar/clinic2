import tkinter as tk
from tkinter import ttk

from models.patient import Patient

class PatientFormView(tk.Toplevel):
    def __init__(self, parent, patient_repo, patient=None):
        super().__init__(parent)

        self.repo = patient_repo
        self.patient = patient

        self.transient(parent)
        self.grab_set()

        self.title("New Patient" if self.patient is None else "Edit Patient")
        self.resizable(False, False)

        self.name_entry = ttk.Entry(self)
        self.phone_entry = ttk.Entry(self)
        self.dob_entry = ttk.Entry(self)

        ttk.Label(self, text="Name").grid(
            row=0, column=0, padx=10, pady=5
        )
        self.name_entry.grid(
            row=0, column=1, padx=10, pady=5
        )

        ttk.Label(self, text="Phone").grid(
            row=1, column=0, padx=10, pady=5
        )
        self.phone_entry.grid(
            row=1, column=1, padx=10, pady=5
        )

        ttk.Label(self, text="Date of birth").grid(
            row=2, column=0, padx=10, pady=5
        )
        self.dob_entry.grid(
            row=2, column=1, padx=10, pady=5
        )

        ttk.Button(
            self,
            text="Save",
            command=self._save
        ).grid(
            row=3, column=1,
            padx=10, pady=10
        )

        if self.patient is not None:
            self._populate_patient_data()

    def _populate_patient_data(self):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.patient.name)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, self.patient.phone_number)
        self.dob_entry.delete(0, tk.END)
        self.dob_entry.insert(0, self.patient.date_of_birth)

    def _save(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        dob = self.dob_entry.get()

        if not name or not phone_number or not dob:
            return

        if self.patient is None:
            new_patient = Patient.new(name, dob, phone_number)
            self.repo.create(new_patient)
        else:
            self.patient.name = name
            self.patient.phone_number = phone_number
            self.patient.date_of_birth = dob
            self.repo.update(self.patient)
        self.master.update_patients()
        self.destroy()