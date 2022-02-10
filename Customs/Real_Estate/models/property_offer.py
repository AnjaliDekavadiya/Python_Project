from odoo import fields, models,api



class PropertyOffer(models.Model):
    _name = "property.offer"
    _description = "Property Offer"

    price = fields.Float(string="Price", tracking=True)
    status = fields.Selection(string="Status", selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    validity = fields.Integer(string="Validity (days)", default="7")
    date_deadline = fields.Date(string="Deadline", compute="_compute_date", inverse="_inverse_date")
    property_id = fields.Many2one('test.model', required=True)
    create_date = fields.Datetime(default=fields.Datetime.now())
    _order = "price desc"
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)

    _sql_constraints=[('check_price','CHECK(price > 0)','Offer price must be positive.')]



    def action_reject(self):
        self.status = 'refused'
        self.property_id.selling_price=0


    @api.depends("validity")
    def _compute_date(self):
        for rec in self:
            rec.date_deadline = fields.Datetime.add(rec.create_date.date(), days=rec.validity)

    def _inverse_date(self):
        for rec in self:
            rec.validity = (rec.date_deadline - rec.create_date.date()).days

    @api.model
    def create(self, vals):
        if vals.get('price'):
            self.env['test.model'].browse(vals['property_id']).check_offer(vals.get('price'))
        return super(PropertyOffer, self).create(vals)

    def action_accept(self):
        refuse = self.env['test.model'].browse(self.property_id)
        refuse.refuse_offer(self.price)
        self.property_id.selling_price = self.price
        if self.property_id.selling_price != 0:
            self.status = 'accepted'
            self.property_id.buyer_id = self.partner_id
            self.property_id.state = 'offer_accepted'



