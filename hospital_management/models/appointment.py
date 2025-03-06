from odoo import models, fields, api
from datetime import datetime, timedelta

# Modelo de citas médicas
class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Cita Médica'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_datetime desc, id desc'

    name = fields.Char(string='Número de cita', required=True, copy=False, readonly=True, default='Nuevo')
    patient_id = fields.Many2one('hospital.patient', string='Paciente', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_datetime = fields.Datetime(string='Fecha y hora', required=True)
    state = fields.Selection([
        ('scheduled', 'Programada'),
        ('cancelled', 'Cancelada'),
        ('done', 'Realizada')
    ], string='Estado', default='scheduled', tracking=True)
    
    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notas')
    prescription = fields.Text(string='Prescripción')

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'Nuevo'
        return super(HospitalAppointment, self).create(vals)

    @api.depends('appointment_datetime')
    def _compute_end_date(self):
        for appointment in self:
            if appointment.appointment_datetime:
                appointment.end_date = appointment.appointment_datetime + timedelta(hours=appointment.duration)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft' 