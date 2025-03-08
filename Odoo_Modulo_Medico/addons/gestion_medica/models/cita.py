from odoo import models, fields, api

# Modelo para las citas médicas
class Cita(models.Model):
    _name = 'gestion.cita'                                                                      # Nombre del modelo
    _description = 'Cita Médica'                                                                # Descripción del modelo   
    _rec_name = 'nombre_cita'                                                                   # Nombre del campo para mostrar en la lista

    paciente_id = fields.Many2one('gestion.paciente', string='Paciente', required=True)         # Paciente de la cita
    medico_id = fields.Many2one('gestion.medico', string='Médico', required=True)               # Médico de la cita
    fecha_hora = fields.Datetime(string='Fecha y hora', required=True)                          # Fecha y hora de la cita
    estado = fields.Selection([
        ('programada', 'Programada'),
        ('cancelada', 'Cancelada'),
        ('realizada', 'Realizada')
    ], string='Estado', default='programada', required=True)
    
    # Campo computado para el nombre de la cita
    nombre_cita = fields.Char(string='Nombre de la cita', compute='_compute_nombre_cita', store=True)
    
    @api.depends('paciente_id', 'medico_id', 'fecha_hora')
    def _compute_nombre_cita(self):
        for record in self:
            if record.paciente_id and record.medico_id and record.fecha_hora:
                record.nombre_cita = f"Cita: {record.paciente_id.nombre_completo} - " \
                                   f"Dr. {record.medico_id.nombre_completo} - " \
                                   f"{record.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
            else:
                record.nombre_cita = "Nueva Cita"