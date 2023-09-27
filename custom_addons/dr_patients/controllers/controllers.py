# -*- coding: utf-8 -*-
# from odoo import http


# class DrPatients(http.Controller):
#     @http.route('/dr_patients/dr_patients', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dr_patients/dr_patients/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dr_patients.listing', {
#             'root': '/dr_patients/dr_patients',
#             'objects': http.request.env['dr_patients.dr_patients'].search([]),
#         })

#     @http.route('/dr_patients/dr_patients/objects/<model("dr_patients.dr_patients"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dr_patients.object', {
#             'object': obj
#         })
