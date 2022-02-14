from odoo import models,fields,api
from odoo.exceptions import ValidationError

class PropertyType(models.Model):
    _name = "property.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property Type"

    name = fields.Char(required=True)
    property_ids = fields.One2many('test.model','property_type_id',string='Property')
    _order = "name"
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many("property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offers", default=0)

    @api.constrains('name')
    def check_name(self):
        for record in self:
            name = self.env['property.type'].search([('name', "=", record.name), ('id', '!=', record.id)])
            if name:
                raise ValidationError(("Name  %s Already exists" % record.name))

    @api.depends("offer_ids")
    def _compute_offers(self):
        self.offer_count = len(self.offer_ids)