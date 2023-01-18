# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Prueba',
    'version': '1.0',
    'description': "Cosi para probar",
    'depends': ['base'],
    'data': [],
    'demo': [],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ]
}