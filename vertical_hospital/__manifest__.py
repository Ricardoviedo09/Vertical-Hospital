{
    'name': "Vertical Hospital",
    'summary': """""",
    'description': """
        Vertical Hospital Management System
    """,
    'author': "Ricardo Oviedo",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail'],
    'data': [
        'data/sequences.xml',
        'security/ir.model.access.csv',
        'views/intro.xml',
        'views/patients.xml',
        'views/treatments.xml',
        'views/res_config_settings_hospital.xml',
        'data/menus.xml',
        'reports/patients_report.xml',
        'reports/list_patients_report.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
# -*- coding: utf-8 -*-
