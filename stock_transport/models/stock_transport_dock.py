from odoo import fields, models


class TransportDock(models.Model):
    _name = "stock.transport.dock"
    _rec_name = 'dock'

    dock = fields.Char(required=True)
