# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hostpital Management MERT',
    'version': '1.1',
    'category': 'Hospital',
    'author': 'this odoo',
    'sqeuence': -100,
    'summary': """Hospital Management MERT summary""",
    'description': "",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
