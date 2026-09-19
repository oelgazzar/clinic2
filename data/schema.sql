CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    date_of_birth TEXT,
    phone_number TEXT
);

CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    reason TEXT,
    notes TEXT,
    patient_id INTEGER,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);