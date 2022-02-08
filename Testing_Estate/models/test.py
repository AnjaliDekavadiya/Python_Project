from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char(required=True)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False,string="Available Form",default=lambda self:fields.Datetime.add(fields.Datetime.now(),months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    active=fields.Boolean(default=True)
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'),('east','East'),('west','West')],
        help="Type is used to separate Leads and Opportunities")
    state=fields.Selection(
        string='State',
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')],
        copy=False,
        default='new',
        required=True)
    property_type_id = fields.Many2one("property.type", string="Property Type")
    seller_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', tracking=True, copy=False)
    tag_ids = fields.Many2many(comodel_name="property.tag", string="Tags")
    offer_ids = fields.One2many("property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total", string="Total Area (sqm)")
    best_price = fields.Integer(compute="_compute_price", string="Best Offer")

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The percentage of an analytic distribution should be between 0 and 100.')
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        self.total_area = self.living_area + self.garden_area

    @api.depends('offer_ids.partner_id')
    def _compute_price(self):
        if self.offer_ids.partner_id:
            self.best_price = max(i.price for i in self.offer_ids)
        else:
            self.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden is True:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ''

    def action_sold(self):
        self.state = 'sold'

    def action_cancel(self):
        self.state = 'cancelled'

    @api.constrains('name')
    def check_name(self):
        for record in self:
            name = self.env['test.model'].search([('name', "=", record.name), ('id', '!=', record.id)])
            if name:
                raise ValidationError(("Name  %s Already exists" % record.name))

    @api.constrains('name', 'description')
    def _check_description(self):
        for record in self:
            if record.name == record.description:
                raise ValidationError("Fields name and description must be different")







