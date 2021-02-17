from odoo import fields, models


class ResPartnerEpt3(models.Model):
    _name = "res.partner.ept3"
    _description = "To store the data of res partner"

    name = fields.Char(string="Name", required=True, help="Enter your name")
    street1 = fields.Char(string="Street1", help="Enter street1")
    street2 = fields.Char(string="Street2", help="Enter street2")
    city = fields.Char(string="City", help="Enter city name")
    state = fields.Char(string="State", help="Enter state name")
    zip_code = fields.Char(string="Zip_Code", help="Enter zip code")
    country = fields.Char(string="Country", help="Enter country name")
    birthdate = fields.Date(string="Birthdate", help="Enter birthdate")
    age = fields.Integer(string="Age", help="Enter age")
    weight = fields.Float(string="Weight", help="Enter weight")
    description = fields.Text(string="Description", help="Enter brief description")
    gender = fields.Selection([
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Transgender', 'Transgender')
            ],
        string="Gender", help="Select gender"
        )
    details = fields.Html(string="Details", help="Enter details in brief")
    is_spectacles = fields.Boolean(string="Is Spectacles", help="Tick if spectacles")
    photo = fields.Image(string="Photo", help="Select image")
