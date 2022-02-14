from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class TestModel(models.Model):
    _name = "test.model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Test Model"

    name = fields.Char(required=True)
    reference=fields.Char(string='Reference',required=True, copy=False, readonly=True,default=lambda self:_('New'))
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
    best_price = fields.Float(compute="_compute_price", string="Best Offer")
    _order = "id desc"
    image=fields.Binary(string="Property Image")


    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected price of a property should be greater than 0.'),
        ('check_selling_price', 'CHECK(selling_price > 0)',
         'The selling price of a property should be positive.')

    ]

    def action_sold(self):
        self.state = 'sold'

    def action_new(self):
        self.state='new'

    def action_received(self):
        self.state='offer_received'

    def action_accepted(self):
        self.state='offer_accepted'

    def action_cancel(self):
        self.state = 'cancelled'



    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        self.total_area = self.living_area + self.garden_area

    @api.depends('offer_ids.partner_id')
    def _compute_price(self):
        for record in self:
            if record.offer_ids.partner_id:
                record.best_price = max(i.price for i in record.offer_ids)
            else:
                record.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden is True:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ''

    @api.constrains('name')
    def check_name(self):
        for record in self:
            name = self.env['test.model'].search([('name', "=", record.name), ('id', '!=', record.id)])
            if name:
                raise ValidationError("Name  %s Already exists" % record.name)

    @api.constrains('name', 'description')
    def _check_description(self):
        for record in self:
            if record.name == record.description:
                raise ValidationError("Fields name and description must be different")

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for rec in self:
            if rec.selling_price != 0:
                value = 0.9 * rec.expected_price
                if rec.selling_price < value:
                    rec.selling_price = 0
                    raise ValidationError("The selling price should not be less than 90% of expected price.")

    @api.model
    def create(self, vals):
        if not vals.get('description'):
            vals['description'] = 'New Property'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('real.estate') or _('New')
        res = super(TestModel, self).create(vals)
        return res

    def unlink(self):
        if self.state not in ('new', 'cancelled'):
            raise ValidationError("You Can't delete property if it is not in New or Cancelled State.")
        for rec in self.offer_ids:
            rec.unlink()
        return super(TestModel, self).unlink()

    def check_offer(self, price):
        # current = self.env['test.model'].browse(self._context.get('active_id')).offer_ids
        if price < 0:
            raise ValidationError("Offer price must be positive.")
        elif price <= self.best_price:
            raise ValidationError("New offer price must be greater than present offers.")
        elif self.state == 'new':
            self.state = 'offer_received'
        return True

    def refuse_offer(self, price):
        print("hello", self.id.offer_ids)
        # current = self.env['estate.property.offer'].browse(self._context.get('active_id')).offer_ids
        for rec in self.id.offer_ids:
            if rec.price == price:
                pass
            rec.action_reject()
        return True











