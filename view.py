
from abc import ABC, abstractmethod

class IHospitalView(ABC):
    @abstractmethod
    def display_patient_details(self, patient_data):
        pass

    @abstractmethod
    def show_loading(self):
        pass

    @abstractmethod
    def hide_loading(self):
        pass

    @abstractmethod
    def show_error_message(self, message):
        pass

    @abstractmethod
    def clear_input_fields(self):
        pass

    @abstractmethod
    def display_appointments(self, appointments_data):
        pass

    @abstractmethod
    def get_patient_input(self):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def get_appointment_details_input(self):
        pass

    @abstractmethod
    def get_invoice_details_input(self):
        pass

    @abstractmethod
    def get_billing_calculation_input(self):
        pass

    @abstractmethod
    def display_billing_total(self, total):
        pass


class ConsoleView(IHospitalView):
    def display_patient_details(self, patient_data):
        print("\n--- Patient Details ---")
        if patient_data:
            print(f"ID: {patient_data.patient_id}")
            print(f"Name: {patient_data.name}")
            print(f"DOB: {patient_data.dob}")
            print(f"Address: {patient_data.address}")
            print(f"Phone: {patient_data.phone}")
        else:
            print("Patient not found.")
        print("-----------------------")

    def show_loading(self):
        print("Loading...")

    def hide_loading(self):
        print("Loading complete.")

    def show_error_message(self, message):
        print(f"ERROR: {message}")

    def clear_input_fields(self):
        print("Input fields cleared.")

    def display_appointments(self, appointments_data):
        print("\n--- Doctor's Appointments ---")
        if appointments_data:
            for appt in appointments_data:
                print(f"  Appointment ID: {appt.appointment_id}, Patient ID: {appt.patient_id}, Date: {appt.date}, Time: {appt.time}, Fee: {appt.consultation_fee}")
        else:
            print("No appointments found for this doctor.")
        print("-----------------------------")

    def get_patient_input(self):
        print("\nEnter Patient Details:")
        patient_id = input("Patient ID: ")
        name = input("Name: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        address = input("Address: ")
        phone = input("Phone: ")
        return {"patient_id": patient_id, "name": name, "dob": dob, "address": address, "phone": phone}

    def get_doctor_id_input(self):
        return input("Enter Doctor ID to load appointments: ")

    def get_appointment_details_input(self):
        print("\nEnter Appointment Details:")
        appointment_id = input("Appointment ID: ")
        patient_id = input("Patient ID: ")
        doctor_id = input("Doctor ID: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")
        consultation_fee = float(input("Consultation Fee: "))
        return {"appointment_id": appointment_id, "patient_id": patient_id, "doctor_id": doctor_id, "date": date, "time": time, "consultation_fee": consultation_fee}

    def get_invoice_details_input(self):
        print("\nEnter Invoice Details:")
        invoice_id = input("Invoice ID: ")
        patient_id = input("Patient ID: ")
        appointment_id = input("Appointment ID: ")
        medication_cost = float(input("Medication Cost: "))
        return {"invoice_id": invoice_id, "patient_id": patient_id, "appointment_id": appointment_id, "medication_cost": medication_cost}

    def get_billing_calculation_input(self):
        print("\nEnter Billing Calculation Details:")
        appointment_id = input("Appointment ID: ")
        medication_cost = float(input("Medication Cost: "))
        return {"appointment_id": appointment_id, "medication_cost": medication_cost}

    def display_billing_total(self, total):
        print(f"Calculated Billing Total: {total:.2f}")

    def show_message(self, message):
        print(message)
