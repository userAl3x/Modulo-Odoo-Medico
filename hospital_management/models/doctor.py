from odoo import models, fields, api

# Modelo de doctores
class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    surname = fields.Char(string='Apellidos', required=True, tracking=True)
    specialty_id = fields.Many2one('hospital.specialty', string='Especialidad', required=True)
    availability = fields.Char(string='Disponibilidad')
    active = fields.Boolean(default=True)
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Citas')
    appointment_count = fields.Integer(string='Número de citas', compute='_compute_appointment_count')

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids) 