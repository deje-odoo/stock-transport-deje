from odoo import models,fields

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.transport.dock" ,string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle",string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",string="Vehicle Category")
