from odoo import models,fields,api
from odoo.exceptions import ValidationError

class PropertyTag(models.Model):
    _name = "property.tag"
    _description = "Property Tag"

    name = fields.Char(required=True)

    @api.constrains('name')
    def check_name(self):
        for record in self:
            name = self.env['property.tag'].search([('name', "=", record.name), ('id', '!=', record.id)])
            if name:
                raise ValidationError(("Name  %s Already exists" % record.name))