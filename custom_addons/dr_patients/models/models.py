# -*- coding: utf-8 -*-

from odoo import models, fields, api,exceptions

#This is a sample case for Odoo technical training. In this use case you will develop an appointment system for Doctors and patients for appointments management.

#Note: Use constraint to not duplicate email. Auto calculate age when user enter date of birth using onchange decorator.
#Note: Use constraint to not duplicate National ID No. Also use Odoo’s ir.sequence to auto generate new code for Patient ID at the time of creation. Auto calculate age when user enter date of birth using onchange decorator

class Doctor(models.Model):

    _name="dr_patients.doctor"
    _description="Doctor"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name", compute="_compute_full_name")
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string="Age", readonly=True,compute="_compute_age")
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True,unique=True)
    department = fields.Many2one(comodel_name="dr_patients.department", string="Department", required=True)
    shift_start = fields.Float(string="Shift Start", required=True, widget='float_time')
    shift_end = fields.Float(string="Shift End", required=True, widget='float_time')

    @api.constrains('email')
    def _check_unique_email(self):
        for rec in self:
            if self.search_count([('email', '=', rec.email)]) > 1:
                raise exceptions.ValidationError("Email address must be unique.")
            

    @api.onchange('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = fields.Date.today().year - rec.date_of_birth.year

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
    
    @api.onchange('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = fields.Date.today().year - rec.date_of_birth.year

class Department(models.Model):
    _name = "dr_patients.department"
    _description = "Department"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True,unique=True)

    @api.constrains('code') 
    def _check_unique_code(self): 
        for rec in self:
            if self.search_count([('code', '=', rec.code)]) > 1:
                raise exceptions.ValidationError("Code must be unique.")

    @api.model
    def create(self, vals):
        if 'code' in vals and not vals.get('name'):
            vals['name'] = vals['code']
        return super(Department, self).create(vals)
    
class Appointment(models.TransientModel):
    _name = "dr_patients.appointment"
    _description = "Appointment"
    appointment_date_time = fields.Datetime(string="Appointment Date & Time", required=True)
    code = fields.Char(string="Code", required=True, unique=True)
    doctor = fields.Many2one(comodel_name="dr_patients.doctor", string="Doctor", required=True)
    patient = fields.Many2one(comodel_name="dr_patients.patient", string="Patient", required=True)
    stage = fields.Selection(string="Stage", selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', required=True)
    treament = fields.Many2many(comodel_name="dr_patients.treatment", string="Treatment",)

    def create_appointment(self):
        vals = {
            'appointment_date_time': self.appointment_date_time,
            'code': self.code,
            'doctor': self.doctor.id,
            'patient': self.patient.id,
            'stage': self.stage,
            'treatment': [(6, 0, [treatment.id for treatment in self.treatment])],  # Convert to valid format
        }
        self.env['dr_patients.appointment'].create(vals)



class Treatment(models.Model):

    _name = "dr_patients.treatment"
    _description = "Treatment"

    name = fields.Char(string="Name", required=True)
    is_done = fields.Boolean(string="Is Done", default=False)

