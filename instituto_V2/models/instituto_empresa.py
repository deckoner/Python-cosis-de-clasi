from odoo import fields, models



class institutoAlumno(models.Model):
    _name = "instituto.empresa"
    _description = "Objeto de la empresa"

    name = fields.Char(string="Nombre", required=True)
    direccion = fields.Char(string="Direccion")
    telefono = fields.Char(string="Telefono")
    cicloFormativo = fields.Selection(
        string='Ciclo Formativo',
        selection=[('informatica', 'Informatica'), ('comercio', 'Comercio'), ('marketing', 'Marketing'), ('administracion', 'Administracion')],
        help="Tu coge uno y pista",
        default="informatica")

    alumnos = fields.One2many('instituto.practicas', 'empresa')

    