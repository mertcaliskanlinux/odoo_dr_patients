from odoo import models, fields


class HospitalPatient(models.Model):
    
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",required=True)    

