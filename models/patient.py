from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True, tracking=True)
    ref = fields.Char(string="Reference", tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender", tracking=True
    )
    active = fields.Boolean(default=True)
