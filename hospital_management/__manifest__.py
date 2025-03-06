{
    'name': 'Hospital Management',                                      # Nombre del módulo
    'version': '1.0',                                                   # Versión del módulo
    'category': 'Healthcare',                                           # Categoría del módulo
    'summary': 'Gestión de citas médicas y pacientes',                  # Resumen del módulo
    'description': """
        Módulo para la gestión de citas médicas que incluye:
        * Registro de pacientes
        * Gestión de citas
        * Gestión de doctores
        * Gestión de especialidades
    """,
    'author': 'Alex Jiménez y Pau Alcaraz',                             # Autor del módulo
    'depends': ['base', 'mail'],                                        # Dependencias del módulo
    'data': [
        'security/ir.model.access.csv',                                 # Acceso a los modelos
        'views/patient_views.xml',                                      # Vistas de pacientes
        'views/doctor_views.xml',                                       # Vistas de doctores
        'views/appointment_views.xml',                                  # Vistas de citas
        'views/specialty_views.xml',                                    # Vistas de especialidades
        'views/menu_views.xml',                                         # Vistas de menú
    ],
    'demo': [],                                                         # Demostraciones del módulo
    'installable': True,                                                # Instalable
    'application': True,                                                # Aplicación
    'auto_install': False                                               # Instalación automática
} 