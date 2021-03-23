from odoo import fields, models, api


class ResPartnerEpt(models.Model):
    _name = "res.partner.ept"
    _description = "Res Partner details"

    name = fields.Char(string="Name", required=True, help="Enter name")
    street1 = fields.Char(string="Street1", help="Enter street1")
    street2 = fields.Char(string="Street2", help="Enter street2")
    city = fields.Char(string="City", default="Newyork", help="Enter city name")
    state = fields.Char(string="State", help="Enter city name")
    zip_code = fields.Char(string="Zip_Code", help="Enter zip code")
    country = fields.Char(string="Country", help="Enter country name")
    birthdate = fields.Date(string="Birthdate", help="Enter birth date")
    age = fields.Integer(string="Age", help="Enter age")
    age_calculate = fields.Integer(string="Age Calculate", help="Age calculate", compute="_compute_age_calculate",
                                   search="age_calculate")
    age_calculate2 = fields.Integer(string="Age Calculate2", help="Age calculate2")
    weight = fields.Float(string="Weight", help="Enter weight")
    description = fields.Text(string="Description", help="Enter description")
    gender = fields.Selection(selection=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    ],
        string="Gender",
        default="Female",
        help="Select gender"
    )
    details = fields.Html(string="Details", help="Enter details")
    is_spectacles = fields.Boolean(string="Is Spectacles", help="Tick if have spectacles")
    photo = fields.Image(string="Photo", help="Select image")

    def _compute_age_calculate(self):
        today = fields.Date.today()
        for age in self:
            age.age_calculate = today.year - age.birthdate.year - (
                    (today.month, today.day) < (age.birthdate.month, age.birthdate.day))

    def search_age(self):
        age = self.env['res.partner.ept'].search([('age_calculate', '=', '23')])

    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        today = fields.Date.today()
        for age in self:
            age.age_calculate2 = today.year - age.birthdate.year - (
                    (today.month, today.day) < (age.birthdate.month, age.birthdate.day))
