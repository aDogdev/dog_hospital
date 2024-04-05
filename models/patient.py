from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", required=True, tracking=True)
    ref = fields.Char(string="Reference", tracking=True)
    age = fields.Integer(
        string="Age", tracking=True, compute="_compute_age", store=True
    )
    birth_date = fields.Date(string="Date of birth")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender",
        tracking=True,
        default="male",
    )
    active = fields.Boolean(default=True)

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = relativedelta(
                    fields.Date.context_today(record), record.birth_date
                ).years
            else:
                record.age = None
