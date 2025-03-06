# -*- coding: utf-8 -*-
{
    'name': "medico",   # Nombre del módulo

    'summary': "Módulo para gestionar la información de un consultorio médico",     # Resumen del módulo

    'description': "Este módulo permite gestionar la información de un consultorio médico, como la información de los pacientes, médicos, citas, etc.",     # Descripción del módulo

    'author': "Alex Jiménez y Pau Alcaraz",     # Autor del módulo
    'website': "https://www.medico.com",        # Página web del módulo

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'category': 'Medico',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        
        # Vistas creadas
        'views/equipos_vieww.xml',  
        'views/eventos_view.xml',
        'views/personas_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # Información de la instalación del módulo
    'installable': True,
    'application': True,
}

