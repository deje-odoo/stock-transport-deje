from odoo import fields, models

class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    stock_transport = fields.Boolean('Dispatch Management System')
