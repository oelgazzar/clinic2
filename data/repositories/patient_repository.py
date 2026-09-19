from data.database import Database
from models.patient import Patient

class PatientRepository:
    __tablename__ = "patients"

    def __init__(self, db: Database):
        self.db = db

    def get_all(self):
        with self.db.connection as con:
            res = con.execute(f"SELECT * FROM {self.__tablename__}")
            return [self.patient_from_row(row) for row in res]

    def get(self, patient_id):
        with self.db.connection as con:
            res = con.execute(f"SELECT * FROM {self.__tablename__} WHERE id = ?", (patient_id,))
            return self.patient_from_row(res.fetchone())

    def patient_from_row(self, row):
        return Patient(*row)

    def create(self, patient: Patient):
        with self.db.connection as con:
            con.execute(f"INSERT INTO {self.__tablename__} (name, date_of_birth, phone_number) VALUES (?, ?, ?)",
                        (patient.name, patient.date_of_birth, patient.phone_number))

    def delete(self, patient: Patient):
        with self.db.connection as con:
            con.execute(f"DELETE FROM {self.__tablename__} WHERE id = ?", (patient.id,))