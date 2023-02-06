import datetime
from odoo import fields, models, api
from odoo.tools import format_datetime
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class institutoAlumno(models.Model):
    _name = "instituto.practicas"
    _description = "Objeto de la empresa"

    name = fields.Many2one('instituto.alumno', string="Nombre", required=True)
    anio = fields.Integer(String="Año", required=True)
    aprobado =fields.Boolean(String="Aprobado", required=True)

    empresa = fields.Many2one('instituto.empresa')
