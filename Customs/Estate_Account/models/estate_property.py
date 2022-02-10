from odoo import models

class Test(models.Model):
    _inherit = "test.model"

    def action_sold(self):
        return super().action_sold()