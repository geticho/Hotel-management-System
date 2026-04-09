
import sqlite3

class Patient:
    def __init__(self, patient_id, name, dob, address, phone):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, consultation_fee):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.consultation_fee = consultation_fee

class Invoice:
    def __init__(self, invoice_id, patient_id, appointment_id, medication_cost, total_amount):
        self.invoice_id = invoice_id
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.medication_cost = medication_cost
        self.total_amount = total_amount

class DatabaseHelper:
    def __init__(self, db_name="hospital.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self._create_tables()

    def _connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id TEXT PRIMARY KEY,
                name TEXT,
                dob TEXT,
                address TEXT,
                phone TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id TEXT PRIMARY KEY,
                name TEXT,
                specialization TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id TEXT PRIMARY KEY,
                patient_id TEXT,
                doctor_id TEXT,
                date TEXT,
                time TEXT,
                consultation_fee REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS invoices (
                invoice_id TEXT PRIMARY KEY,
                patient_id TEXT,
                appointment_id TEXT,
                medication_cost REAL,
                total_amount REAL
            )
        """)
        self.conn.commit()

    # CRUD Operations for Patient
    def add_patient(self, patient):
        self.cursor.execute("INSERT INTO patients VALUES (?, ?, ?, ?, ?)",
                            (patient.patient_id, patient.name, patient.dob, patient.address, patient.phone))
        self.conn.commit()

    def get_patient(self, patient_id):
        self.cursor.execute("SELECT * FROM patients WHERE patient_id=?", (patient_id,))
        row = self.cursor.fetchone()
        if row: return Patient(*row)
        return None

    def update_patient(self, patient):
        self.cursor.execute("UPDATE patients SET name=?, dob=?, address=?, phone=? WHERE patient_id=?",
                            (patient.name, patient.dob, patient.address, patient.phone, patient.patient_id))
        self.conn.commit()

    def delete_patient(self, patient_id):
        self.cursor.execute("DELETE FROM patients WHERE patient_id=?", (patient_id,))
        self.conn.commit()

    # CRUD Operations for Doctor
    def add_doctor(self, doctor):
        self.cursor.execute("INSERT INTO doctors VALUES (?, ?, ?)",
                            (doctor.doctor_id, doctor.name, doctor.specialization))
        self.conn.commit()

    def get_doctor(self, doctor_id):
        self.cursor.execute("SELECT * FROM doctors WHERE doctor_id=?", (doctor_id,))
        row = self.cursor.fetchone()
        if row: return Doctor(*row)
        return None

    def update_doctor(self, doctor):
        self.cursor.execute("UPDATE doctors SET name=?, specialization=? WHERE doctor_id=?",
                            (doctor.name, doctor.specialization, doctor.doctor_id))
        self.conn.commit()

    def delete_doctor(self, doctor_id):
        self.cursor.execute("DELETE FROM doctors WHERE doctor_id=?", (doctor_id,))
        self.conn.commit()

    # CRUD Operations for Appointment
    def add_appointment(self, appointment):
        self.cursor.execute("INSERT INTO appointments VALUES (?, ?, ?, ?, ?, ?)",
                            (appointment.appointment_id, appointment.patient_id, appointment.doctor_id, appointment.date, appointment.time, appointment.consultation_fee))
        self.conn.commit()

    def get_appointment(self, appointment_id):
        self.cursor.execute("SELECT * FROM appointments WHERE appointment_id=?", (appointment_id,))
        row = self.cursor.fetchone()
        if row: return Appointment(*row)
        return None

    def get_appointments_by_doctor(self, doctor_id):
        self.cursor.execute("SELECT * FROM appointments WHERE doctor_id=?", (doctor_id,))
        rows = self.cursor.fetchall()
        return [Appointment(*row) for row in rows]

    def update_appointment(self, appointment):
        self.cursor.execute("UPDATE appointments SET patient_id=?, doctor_id=?, date=?, time=?, consultation_fee=? WHERE appointment_id=?",
                            (appointment.patient_id, appointment.doctor_id, appointment.date, appointment.time, appointment.consultation_fee, appointment.appointment_id))
        self.conn.commit()

    def delete_appointment(self, appointment_id):
        self.cursor.execute("DELETE FROM appointments WHERE appointment_id=?", (appointment_id,))
        self.conn.commit()

    # CRUD Operations for Invoice
    def add_invoice(self, invoice):
        self.cursor.execute("INSERT INTO invoices VALUES (?, ?, ?, ?, ?)",
                            (invoice.invoice_id, invoice.patient_id, invoice.appointment_id, invoice.medication_cost, invoice.total_amount))
        self.conn.commit()

    def get_invoice(self, invoice_id):
        self.cursor.execute("SELECT * FROM invoices WHERE invoice_id=?", (invoice_id,))
        row = self.cursor.fetchone()
        if row: return Invoice(*row)
        return None

    def update_invoice(self, invoice):
        self.cursor.execute("UPDATE invoices SET patient_id=?, appointment_id=?, medication_cost=?, total_amount=? WHERE invoice_id=?",
                            (invoice.patient_id, invoice.appointment_id, invoice.medication_cost, invoice.total_amount, invoice.invoice_id))
        self.conn.commit()

    def delete_invoice(self, invoice_id):
        self.cursor.execute("DELETE FROM invoices WHERE invoice_id=?", (invoice_id,))
        self.conn.commit()

    def calculate_billing_total(self, appointment_id, medication_cost):
        appointment = self.get_appointment(appointment_id)
        if appointment:
            return appointment.consultation_fee + medication_cost
        return 0

    def close(self):
        self.conn.close()
