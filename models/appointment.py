from odoo import fields, models, api
from datetime import datetime, time
from dateutil.relativedelta import relativedelta


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "patient_id"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(
        "hospital.patient", string="Patient", required=True, tracking=True
    )
    ref = fields.Char(
        string="Reference",
        related="patient_id.ref",
        help="Reference from patient record",
    )
    gender = fields.Selection(
        string="Gender",
        related="patient_id.gender",
    )
    appointment_time = fields.Datetime(
        string="Appointment Time",
        default=lambda self: datetime.combine(
            fields.Datetime.today() + relativedelta(months=1), time(13, 0)
        ),
        tracking=True,
    )
    booking_date = fields.Date(
        string="Booking Date", default=fields.Date.context_today, tracking=True
    )
    prescription = fields.Html(string="Prescription", tracking=True)
    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", "High"), ("3", "Very High")],
        string="Priority",
        tracking=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_consultation", "In Consultation"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
        string="Status",
        tracking=True,
    )

    def action_cancel(self):
        for record in self:
            record.state = "cancel"
        return {
            "effect": {
                "fadeout": "slow",
                "message": "Cancel Successful",
                "type": "rainbow_man",
            }
        }
