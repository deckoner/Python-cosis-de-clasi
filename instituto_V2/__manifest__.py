# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Instituto V2',
    'version': '1.4',
    'description': "Modulo que ayudara en la gestios de los alumnos en las practicas",
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
        'views/instituto_alumnos_views.xml',
        'views/instituto_empresas_views.xml',
        'views/instituto_menus.xml'
    ]
}