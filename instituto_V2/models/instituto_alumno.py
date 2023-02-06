import datetime
from odoo import fields, models, api
from odoo.tools import format_datetime
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class institutoAlumno(models.Model):
    _name = "instituto.alumno"
    _description = "Objeto del alumno"

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    fechaNacimiento = fields.Date(string="Fecha Nacimiento",required=True)
    direccion = fields.Char(string="Direccion")
    codPostal = fields.Char(string="Codigo Postal")
    email = fields.Char(string="Email")
    coche = fields.Boolean(string="Coche")
    otros = fields.Char(string="Otros")
    notaMedia = fields.Float(string="Nota Media", default="5.0", required=True)
    notaString = fields.Char(string="Nota escrita")
    empresa = fields.Many2one('instituto.empresa', string='Empresa de practicas')

    cicloFormativo = fields.Selection(
        string='Ciclo Formativo',
        selection=[('dam', 'DAM'), ('daw', 'DAW'), ('asir', 'ASIR')],
        help="Tu coge uno y pista",
        default="dam")
    
    active = fields.Boolean('active',default=True)
    
    # Metodos privados
    @api.onchange("notaMedia")
    def _onchange_garden_on(self):
        for record in self:
            record.notaString = "Suspendido, sin practicas"
            if record.notaMedia >= 5 and record.notaMedia <= 6.9:
                record.notaString = "aprobado"
            if record.notaMedia >= 7 and record.notaMedia <= 8.9:
                record.notaString = "notable"
            if record.notaMedia >= 9:
                record.notaString = "sobresaliente"