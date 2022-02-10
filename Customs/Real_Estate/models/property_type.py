from odoo import models,fields,api
from odoo.exceptions import ValidationError

class PropertyType(models.Model):
    _name = "property.type"
    _description = "Property Type"

    name = fields.Char(required=True)
    property_ids = fields.One2many('test.model','property_type_id',string='Property')
    _order = "name"
    sequence = fields.Integer('Sequence', default=1)
    #offer_ids=fields.one2many()
    #offer_count=fields.Integer(compute='_number_of_offers')

    @api.constrains('name')
    def check_name(self):
        for record in self:
            name = self.env['property.type'].search([('name', "=", record.name), ('id', '!=', record.id)])
            if name:
                raise ValidationError(("Name  %s Already exists" % record.name))