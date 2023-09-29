# -*- coding: utf-8 -*-



from odoo import models, fields

class Appointment(models.Model):
    _name = "dr_patients.appointment"
    _description = "Appointment"

    appointment_date_time = fields.Datetime(string="Appointment Date & Time", required=True)
    code = fields.Char(string="Code",)
    doctor = fields.Many2one(comodel_name="dr_patients.doctor", string="Doctor", required=True)
    patient = fields.Many2one(comodel_name="dr_patients.patient", string="Patient", required=True)
    stage = fields.Selection(string="Stage", selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', required=True)
    treatment = fields.One2many(comodel_name="dr_patients.treatment", inverse_name="appointment", string="Treatment")
