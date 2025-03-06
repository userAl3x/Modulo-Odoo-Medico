from odoo import models, fields, api

# Modelo de pacientes
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Paciente'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    surname = fields.Char(string='Apellidos', required=True, tracking=True)
    dni = fields.Char(string='DNI', required=True)
    birth_date = fields.Date(string='Fecha de nacimiento')
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Masculino'),
        ('female', 'Femenino'),
        ('other', 'Otro')
    ], required=True, default='male', tracking=True)
    
    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    address = fields.Text(string='Dirección')
    active = fields.Boolean(default=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Citas')
    appointment_count = fields.Integer(string='Número de citas', compute='_compute_appointment_count')
    
    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = fields.Date.from_string(fields.Date.today()).year - fields.Date.from_string(record.birth_date).year
            else:
                record.age = 0

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids) 