from odoo import fields, models


class ResPartnerEpt2(models.Model):
    _name = "res.partner.ept2"
    _description = "Restaurent Partner2"

    name = fields.Char(string="Name", required=True, help="Enter res partner name")
    street1 = fields.Char(string="Street1", help="Enter street1")
    street2 = fields.Char(string="Street2", help="Enter street2")
    city = fields.Char(string="City", help="Enter city")
    state = fields.Char(string="State", help="Enter state")
    zip_code = fields.Char(string="Zip_Code", help="Enter zip code")
    country = fields.Char(string="Country", help="Enter country name")
    birthdate = fields.Date(string="Birthdate", help="Enter birthdate")
    age = fields.Integer(string="Age", help="Enter age")
    weight = fields.Float(string="Weight", help="Enter weight")
    description = fields.Text(string="Description", help="Enter description")
    gender = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    ], string="Gender", help="Select gender")
    details = fields.Html(string="Details", help="Enter your details briefly")
    is_spectacles = fields.Boolean(string="Is_Spectacles", help="Tick if spectacles")
    photo = fields.Image(string="Photo", help="Select image")
