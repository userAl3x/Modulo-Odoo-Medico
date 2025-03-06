from odoo import models, fields # type: ignore

# Modelo de especialidades médicas
class HospitalSpecialty(models.Model):
    _name = 'hospital.specialty'
    _description = 'Especialidad Médica'

    name = fields.Char(string='Nombre', required=True)
    doctor_ids = fields.One2many('hospital.doctor', 'specialty_id', string='Doctores') 