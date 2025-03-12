{
    'name': 'Gestión de Reservas Médicas',                                                               # Nombre del módulo
    'version': '1.0',                                                                                    # Versión del módulo
    'summary': 'Módulo para gestionar citas médicas',                                                    # Resumen del módulo
    'description': 'Sistema de gestión de citas médicas con pacientes, médicos y especialidades',        # Descripción detallada
    'category': 'Healthcare',                                                                            # Categoría del módulo
    'author': 'Alex Jiménez y Pau Alcaraz',                                                              # Autor del módulo
    'website': '',                                                                                       # Sitio web del módulo
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',                                                                  # Acceso a los modelos
        'views/paciente_views.xml',                                                                      # Vista de pacientes
        'views/medico_views.xml',                                                                        # Vista de médicos
        'views/especialidad_views.xml',                                                                  # Vista de especialidades
        'views/cita_views.xml',                                                                          # Vista de citas
        'views/menu_views.xml',                                                                          # Vista de menú
    ],
    'demo': [],                                                                                          # Demostración del módulo
    'installable': True,                                                                                 # Instalable
    'application': True,                                                                                 # Aplicación
    'auto_install': False,                                                                               # Instalación automática
} 