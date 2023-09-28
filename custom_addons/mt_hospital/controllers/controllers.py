# -*- coding: utf-8 -*-
# from odoo import http


# class MtHospital(http.Controller):
#     @http.route('/mt_hospital/mt_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mt_hospital/mt_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mt_hospital.listing', {
#             'root': '/mt_hospital/mt_hospital',
#             'objects': http.request.env['mt_hospital.mt_hospital'].search([]),
#         })

#     @http.route('/mt_hospital/mt_hospital/objects/<model("mt_hospital.mt_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mt_hospital.object', {
#             'object': obj
#         })
