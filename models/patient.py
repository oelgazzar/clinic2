from datetime import datetime, date

class Patient:
    def __init__(self, id, name, date_of_birth,  phone_number):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

    @property
    def age(self):
        dob = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )
        return age

    def __repr__(self):
        return f"{self.name} ({self.age} years old)"