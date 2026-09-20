import tkinter as tk
from tkinter import ttk

from .patient_form_view import PatientFormView

class PatientView(tk.Frame):
    def __init__(self, master, patient_repo):
        super().__init__(master)

        self.repo = patient_repo
        self.name_filter = ''

        self._create_widgets()
        self._layout_widgets()
        self.update_patients()

    def _create_widgets(self):
        self.title_label = ttk.Label(
            self,
            text="Patients",
            font=("TkDefaultFont", 16, "bold")
        )

        self.new_button = ttk.Button(
            self,
            text="+ New Patient",
            command=self._create_patient
        )

        self.search_label = ttk.Label(
            self,
            text="Search:"
        )

        self.search_query = tk.StringVar()
        self.search_query.trace_add('write', self._on_text_changed)

        self.search_entry = ttk.Entry(self, textvariable=self.search_query)

        self.patient_list = ttk.Treeview(
            self,
            columns=("name", "phone", "dob"),
            show="headings"
        )

        self.patient_list.heading("name", text="Name")
        self.patient_list.heading("phone", text="Phone")
        self.patient_list.heading("dob", text="Date of Birth")

        self.patient_list.bind(
            "<<TreeviewSelect>>",
            self._on_patient_selected
        )

        self.details_frame = ttk.LabelFrame(
            self,
            text="Patient Details"
        )

        self.name_label = ttk.Label(self.details_frame)
        self.phone_label = ttk.Label(self.details_frame)
        self.dob_label = ttk.Label(self.details_frame)

        self.edit_button = ttk.Button(
            self.details_frame,
            text="Edit",
            command=self._edit_patient
        )

        self.delete_button = ttk.Button(
            self.details_frame,
            text="Delete",
            command=self._delete_patient
        )

    def _layout_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.title_label.grid(
            row=0, column=0,
            sticky="w",
            padx=10, pady=10
        )

        self.new_button.grid(
            row=0, column=1,
            padx=10, pady=10
        )

        self.search_label.grid(
            row=1, column=0,
            sticky="w",
            padx=(10, 0)
        )

        self.search_entry.grid(
            row=1, column=0,
            sticky="ew",
            padx=(60, 10),
            pady=5,
        )

        self.patient_list.grid(
            row=2, column=0,
            columnspan=2,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.details_frame.grid(
            row=3, column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=10
        )

        self.name_label.grid(
            row=0, column=0,
            sticky="w",
            padx=10, pady=5
        )

        self.phone_label.grid(
            row=1, column=0,
            sticky="w",
            padx=10, pady=5
        )

        self.dob_label.grid(
            row=2, column=0,
            sticky="w",
            padx=10, pady=5
        )

        self.edit_button.grid(
            row=0, column=1,
            padx=10
        )

        self.delete_button.grid(
            row=0, column=2,
            padx=10
        )


    def update_patients(self):
        if self.repo is None:
            return

        # Clear list
        for item in self.patient_list.get_children():
            self.patient_list.delete(item)
        
        patients = self.repo.get_with_filter(self.name_filter)
        for patient in patients:
            self.patient_list.insert('', tk.END, iid=str(patient.id), values=(patient.name, patient.phone_number, patient.date_of_birth))

    def _on_patient_selected(self, _):
        selected_patient = self.patient_list.selection()
        if not selected_patient:
            return

        self.show_patient_details(selected_patient[0])

    def show_patient_details(self, patient_id):
        patient = self.repo.get(patient_id)
        self.name_label['text'] = f"Name: {patient.name}"
        self.phone_label['text'] = f"Phone Number: {patient.phone_number}"
        self.dob_label['text'] = f"Age: {patient.age}"

    def _create_patient(self):
        PatientFormView(self, self.repo)

    def _edit_patient(self):
        selected_patients = self.patient_list.selection()
        if len(selected_patients) != 1:
            return

        patient = self.repo.get(selected_patients[0])

        PatientFormView(self, self.repo, patient)

    def _delete_patient(self):
        selected_patients = self.patient_list.selection()
        if not selected_patients:
            return

        self.repo.delete_multiple(selected_patients)
        self.update_patients()

    def _on_text_changed(self, *_):
        self.name_filter = self.search_query.get()
        self.update_patients()

if __name__ == '__main__':
    root = tk.Tk()
    p = PatientView(root, None)
    p.pack(fill='both', expand=True)
    root.mainloop()