# -*- coding: utf-8 -*-
# __manifest__.py

{
    'name': 'Randevu Yönetimi',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Patient and doctor appointment management.',
    'description': """
    This module is used to organize appointments of patients and doctors.
    """,
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base', 'sale'],
    'data': [
        'views/appointment_wizard.xml',  # Sihirbaz görünümünü ekleyin
        # 'views/patient_list.xml',  # Doktor görünümünü ekleyin
        # 'views/doctor.xml',  # Hasta görünümünü ekleyin
        'views/menu.xml',  # Menü görünümünü ekleyin
    ],
    'installable': True,
    'application': True,
}
