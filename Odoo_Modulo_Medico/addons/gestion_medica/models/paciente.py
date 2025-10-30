from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'gestion.paciente'                                                          # Nombre del modelo
    _description = 'Paciente'                                                           # Descripción del modelo
    _rec_name = 'nombre_completo'                                                       # Nombre del campo para mostrar en la lista

    nombre = fields.Char(string='Nombre', required=True)                                # Nombre del paciente
    apellidos = fields.Char(string='Apellidos', required=True)                          # Apellidos del paciente
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)         # Fecha de nacimiento del paciente
    telefono = fields.Char(string='Teléfono', required=True)                            # Teléfono del paciente
    email = fields.Char(string='Correo electrónico', required=True)                     # Correo electrónico del paciente
    
    # Campo computado para el nombre completo
    nombre_completo = fields.Char(string='Nombre completo', compute='_compute_nombre_completo', store=True)
    
    # Relación inversa con citas
    cita_ids = fields.One2many('gestion.cita', 'paciente_id', string='Citas')
    
    # Campo computado para el contador de citas
    cita_count = fields.Integer(string='Número de citas', compute='_compute_cita_count')
    
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"
            
    @api.depends('cita_ids')
    def _compute_cita_count(self):
        for record in self:
            record.cita_count = len(record.cita_ids)
            
    def action_view_citas(self):
        self.ensure_one()
        action = {
            'name': 'Citas del Paciente',
            'type': 'ir.actions.act_window',
            'res_model': 'gestion.cita',
            'view_mode': 'tree,form,calendar',
            'domain': [('paciente_id', '=', self.id)],
            'context': {'default_paciente_id': self.id},
        }
        return action 