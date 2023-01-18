import datetime
from odoo import fields, models
from dateutil.relativedelta import relativedelta


class estateProperty(models.Model):
    _name = "estate.property"
    _description = "Prueba"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    dateAvailability = fields.Date(copy=False, default= datetime.date.today() + relativedelta(months=3))
    expectedPrice = fields.Float(required=True)
    sellingPrice = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    livingArea = fields.Integer()
    facades = fields.Integer()
    gardenArea = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Tu coge uno y pista")

    state = fields.Selection(
        string='Type',
        selection=[('new', 'New'), ('offerReceived', 'Offer Received'), ('offerAccepted', 'Offer Accepted'), ('soldCanceled', 'Sold and Canceled')],
        help="Tu coge uno y pista")

    active = fields.Boolean('active',default=True)