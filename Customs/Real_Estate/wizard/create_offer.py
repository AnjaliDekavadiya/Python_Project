from odoo import api,models,fields,_

class createOfferWizard(models.TransientModel):
    _name = 'create.offer.wizard'
    _description = 'Create Offer Wizard'

    '''name=fields.Char(string='Property Name' ,required=True)'''
    price=fields.Float(string="Property Price", tracking=True)
    partner_id = fields.Many2one('res.partner', required=True)
    validity = fields.Integer(string="Property Validity (days)", default="7")
    date_deadline = fields.Date(string="Property Deadline")
    status = fields.Selection(string="Status", selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    property_id = fields.Many2one('test.model', required=True)
    create_date = fields.Datetime(default=fields.Datetime.now())

    @api.depends("validity")
    def _compute_date(self):
        for rec in self:
            rec.date_deadline = fields.Datetime.add(rec.create_date.date(), days=rec.validity)

    def _inverse_date(self):
        for rec in self:
            rec.validity = (rec.date_deadline - rec.create_date.date()).days

    '''@api.model
    def create(self, vals):
        if vals.get('price'):
            self.env['test.model'].browse(vals['property_id']).check_offer(vals.get('price'))
        return super(createOfferWizard, self).create(vals)'''

    def action_create_offer(self):
        print("button is clicked")
        vals={
            'price':self.price,
            'partner_id':self.partner_id.id,
            'validity':self.validity,
            'date_deadline':self.date_deadline,
            'property_id':self.property_id.id

        }
        self.env['property.offer'].create(vals)




