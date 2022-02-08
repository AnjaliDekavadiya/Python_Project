from odoo import fields, models,api
import datetime


class TestModel(models.Model):
    _name = "property.offer"
    _description = "Property Offer"

    price = fields.Float(string="Price", tracking=True)
    status = fields.Selection(string="Status", selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    validity = fields.Integer(string="Validity (days)", default="7")
    date_deadline = fields.Date(string="Deadline", compute="_compute_date", inverse="_inverse_date")
    property_id = fields.Many2one('test.model', required=True)
    create_date = fields.Datetime(default=fields.Datetime.now())

    def action_accept(self):
        self.status = 'accepted'
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id

    def action_reject(self):
        self.status = 'refused'


    @api.depends("validity")
    def _compute_date(self):
        for rec in self:
            rec.date_deadline = fields.Datetime.add(rec.create_date.date(), days=rec.validity)

    def _inverse_date(self):
        for rec in self:
            rec.validity = (rec.date_deadline - rec.create_date.date()).days



