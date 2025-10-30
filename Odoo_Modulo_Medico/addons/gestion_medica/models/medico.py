from odoo import models, fields, api

# Modelo para los médicos (doctores)
class Medico(models.Model):
    _name = 'gestion.medico'                                                                                # Nombre del modelo
    _description = 'Médico'                                                                                 # Descripción del modelo
    _rec_name = 'nombre_completo'                                                                           # Nombre del campo para mostrar en la lista

    nombre = fields.Char(string='Nombre', required=True)                                                    # Nombre del médico
    apellidos = fields.Char(string='Apellidos', required=True)                                              # Apellidos del médico
    especialidad_id = fields.Many2one('gestion.especialidad', string='Especialidad', required=True)         # Especialidad del médico
    disponibilidad = fields.Char(string='Disponibilidad', required=True)                                    # Disponibilidad del médico
    
    # Campo computado para el nombre completo
    nombre_completo = fields.Char(string='Nombre completo', compute='_compute_nombre_completo', store=True)
    
    # Relación inversa con citas
    cita_ids = fields.One2many('gestion.cita', 'medico_id', string='Citas')
    
    # Campos computados para contadores
    cita_count = fields.Integer(string='Número de citas', compute='_compute_cita_count')
    paciente_count = fields.Integer(string='Número de pacientes', compute='_compute_paciente_count')
    
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
            
    @api.depends('cita_ids')
    def _compute_cita_count(self):
        for record in self:
            record.cita_count = len(record.cita_ids)
            
    @api.depends('cita_ids.paciente_id')
    def _compute_paciente_count(self):
        for record in self:
            pacientes = record.cita_ids.mapped('paciente_id')
            record.paciente_count = len(set(pacientes.ids))
            
    def action_view_citas(self):
        self.ensure_one()
        action = {
            'name': 'Citas del Médico',
            'type': 'ir.actions.act_window',
            'res_model': 'gestion.cita',
            'view_mode': 'calendar,tree,form',
            'domain': [('medico_id', '=', self.id)],
            'context': {'default_medico_id': self.id},
        }
        return action
        
    def action_view_pacientes(self):
        self.ensure_one()
        action = {
            'name': 'Pacientes del Médico',
            'type': 'ir.actions.act_window',
            'res_model': 'gestion.paciente',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.cita_ids.mapped('paciente_id').ids)],
        }
        return action 