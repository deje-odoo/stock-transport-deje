from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit= "stock.picking"

    volume = fields.Float(compute = "_compute_vol", default =0, store= True)

    @api.depends("move_ids")
    def _compute_vol(self):
        for record in self:
            total_volume = 0
            for move in record.move_ids:
                total_volume += move.product_id.volume * move.quantity
            record.volume = total_volume
