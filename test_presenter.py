
import unittest
from unittest.mock import MagicMock
from presenter import HospitalPresenter
from model import Patient, DatabaseHelper, Appointment
from view import IHospitalView

class TestHospitalPresenter(unittest.TestCase):
    def setUp(self):
        self.mock_view = MagicMock(spec=IHospitalView)
        self.mock_db = MagicMock(spec=DatabaseHelper)
        self.presenter = HospitalPresenter(self.mock_view, self.mock_db)

    def test_on_save_patient_clicked_success(self):
        # Setup
        self.mock_view.get_patient_input.return_value = {
            "patient_id": "P001",
            "name": "John Doe",
            "dob": "1990-01-01",
            "address": "123 Main St",
            "phone": "555-1234"
        }
        self.mock_db.get_patient.return_value = None  # New patient

        # Execute
        self.presenter.on_save_patient_clicked()

        # Verify
        self.mock_view.show_loading.assert_called()
        self.mock_db.add_patient.assert_called()
        self.mock_view.show_message.assert_called_with("Patient added successfully.")
        self.mock_view.clear_input_fields.assert_called()
        self.mock_view.hide_loading.assert_called()

    def test_on_load_appointments_success(self):
        # Setup
        doctor_id = "D001"
        mock_appointments = [
            Appointment("A001", "P001", "D001", "2026-04-01", "10:00", 100.0)
        ]
        self.mock_db.get_appointments_by_doctor.return_value = mock_appointments

        # Execute
        self.presenter.on_load_appointments(doctor_id)

        # Verify
        self.mock_view.show_loading.assert_called()
        self.mock_db.get_appointments_by_doctor.assert_called_with(doctor_id)
        self.mock_view.display_appointments.assert_called_with(mock_appointments)
        self.mock_view.hide_loading.assert_called()

    def test_on_calculate_billing_total_success(self):
        # Setup
        self.mock_view.get_billing_calculation_input.return_value = {
            "appointment_id": "A001",
            "medication_cost": 50.0
        }
        self.mock_db.calculate_billing_total.return_value = 150.0

        # Execute
        self.presenter.on_calculate_billing_total()

        # Verify
        self.mock_view.show_loading.assert_called()
        self.mock_db.calculate_billing_total.assert_called_with("A001", 50.0)
        self.mock_view.display_billing_total.assert_called_with(150.0)
        self.mock_view.hide_loading.assert_called()

if __name__ == "__main__":
    unittest.main()
