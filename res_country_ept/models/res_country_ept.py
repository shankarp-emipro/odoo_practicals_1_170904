from odoo import fields, models


class ResCountryEpt(models.Model):
    _name = "res.country.ept"
    _description = "To store res country data"

    name = fields.Char(string="Country Name", required=True, help="Enter country name")
    abbreviation = fields.Char(string="Abbreviation", help="Enter abbreviation for country name")
    active = fields.Boolean(string="Active", help="Tick if active")
