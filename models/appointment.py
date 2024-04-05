from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one("hospital.patient", string="Patient")
