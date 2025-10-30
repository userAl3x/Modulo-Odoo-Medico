from odoo import models, fields

# Modelo para las especialidades médicas
class Especialidad(models.Model):
    _name = 'gestion.especialidad'                                                          # Nombre del modelo
    _description = 'Especialidad Médica'                                                    # Descripción del modelo
    _rec_name = 'nombre'                                                                    # Esto indica que el campo 'nombre' se usará para mostrar el registro, es decir, el nombre de la especialidad creada en Odo

    nombre = fields.Char(string='Nombre', required=True)                                    # Nombre de la especialidad
    
    # Relación inversa con médicos
    medico_ids = fields.One2many('gestion.medico', 'especialidad_id', string='Médicos')     # Relación con médicos