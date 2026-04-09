
from model import Patient, Doctor, Appointment, Invoice, DatabaseHelper
from view import IHospitalView

class HospitalPresenter:
    def __init__(self, view: IHospitalView, db_helper: DatabaseHelper):
        self.view = view
        self.db_helper = db_helper

    def on_save_patient_clicked(self):
        self.view.show_loading()
        try:
            patient_data = self.view.get_patient_input()
            patient = Patient(patient_data["patient_id"], patient_data["name"], patient_data["dob"], patient_data["address"], patient_data["phone"])
            if self.db_helper.get_patient(patient.patient_id):
                self.db_helper.update_patient(patient)
                self.view.show_message("Patient updated successfully.")
            else:
                self.db_helper.add_patient(patient)
                self.view.show_message("Patient added successfully.")
            self.view.clear_input_fields()
        except Exception as e:
            self.view.show_error_message(f"Error saving patient: {e}")
        finally:
            self.view.hide_loading()

    def on_load_patient_details(self, patient_id):
        self.view.show_loading()
        try:
            patient = self.db_helper.get_patient(patient_id)
            self.view.display_patient_details(patient)
        except Exception as e:
            self.view.show_error_message(f"Error loading patient details: {e}")
        finally:
            self.view.hide_loading()

    def on_load_appointments(self, doctor_id):
        self.view.show_loading()
        try:
            appointments = self.db_helper.get_appointments_by_doctor(doctor_id)
            self.view.display_appointments(appointments)
        except Exception as e:
            self.view.show_error_message(f"Error loading appointments: {e}")
        finally:
            self.view.hide_loading()

    def on_calculate_billing_total(self):
        self.view.show_loading()
        try:
            billing_data = self.view.get_billing_calculation_input()
            total = self.db_helper.calculate_billing_total(billing_data["appointment_id"], billing_data["medication_cost"])
            self.view.display_billing_total(total)
        except Exception as e:
            self.view.show_error_message(f"Error calculating billing total: {e}")
        finally:
            self.view.hide_loading()

    def on_add_appointment_clicked(self):
        self.view.show_loading()
        try:
            appt_data = self.view.get_appointment_details_input()
            appointment = Appointment(appt_data["appointment_id"], appt_data["patient_id"], appt_data["doctor_id"], appt_data["date"], appt_data["time"], appt_data["consultation_fee"])
            self.db_helper.add_appointment(appointment)
            self.view.show_message("Appointment added successfully.")
            self.view.clear_input_fields()
        except Exception as e:
            self.view.show_error_message(f"Error adding appointment: {e}")
        finally:
            self.view.hide_loading()

    def on_add_invoice_clicked(self):
        self.view.show_loading()
        try:
            invoice_data = self.view.get_invoice_details_input()
            # Calculate total amount based on consultation fee and medication cost
            appointment = self.db_helper.get_appointment(invoice_data["appointment_id"])
            if appointment:
                total_amount = appointment.consultation_fee + invoice_data["medication_cost"]
                invoice = Invoice(invoice_data["invoice_id"], invoice_data["patient_id"], invoice_data["appointment_id"], invoice_data["medication_cost"], total_amount)
                self.db_helper.add_invoice(invoice)
                self.view.show_message("Invoice added successfully.")
            else:
                self.view.show_error_message("Appointment not found for invoice creation.")
            self.view.clear_input_fields()
        except Exception as e:
            self.view.show_error_message(f"Error adding invoice: {e}")
        finally:
            self.view.hide_loading()

    def close_db(self):
        self.db_helper.close()
