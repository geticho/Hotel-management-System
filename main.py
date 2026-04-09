
from model import DatabaseHelper, Doctor
from view import ConsoleView
from presenter import HospitalPresenter

def main():
    db_helper = DatabaseHelper("hospital.db")
    view = ConsoleView()
    presenter = HospitalPresenter(view, db_helper)

    # Initialize sample data
    try:
        if not db_helper.get_doctor("D001"):
            db_helper.add_doctor(Doctor("D001", "Dr. Smith", "Cardiology"))
        if not db_helper.get_doctor("D002"):
            db_helper.add_doctor(Doctor("D002", "Dr. Doe", "Dermatology"))
    except Exception as e:
        print(f"Error adding doctors: {e}")

    print("--- Hospital Management System ---")
    while True:
        print("\n1. Save/Update Patient")
        print("2. Load Patient Details")
        print("3. Add Appointment")
        print("4. Load Appointments by Doctor")
        print("5. Calculate Billing Total")
        print("6. Add Invoice")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            presenter.on_save_patient_clicked()
        elif choice == "2":
            patient_id = input("Enter Patient ID: ")
            presenter.on_load_patient_details(patient_id)
        elif choice == "3":
            presenter.on_add_appointment_clicked()
        elif choice == "4":
            doctor_id = input("Enter Doctor ID: ")
            presenter.on_load_appointments(doctor_id)
        elif choice == "5":
            presenter.on_calculate_billing_total()
        elif choice == "6":
            presenter.on_add_invoice_clicked()
        elif choice == "7":
            presenter.close_db()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
