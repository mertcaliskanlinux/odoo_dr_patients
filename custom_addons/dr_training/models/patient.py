# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Patient(models.Model):
    _name = "dr_patients.patient"
    _description = "Patient"

    patient_id = fields.Char(string="Patient ID", required=True, copy=False, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('dr_patients.patient'))
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name", compute="_compute_full_name")
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string="Age", readonly=True,compute="_compute_age")
    address = fields.Text(string="Address", required=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    national_id_no = fields.Char(string="National ID No.", required=True,unique=True)
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
        
                today = fields.Date.today()
                birth_date = fields.Date.from_string(record.date_of_birth)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

