from odoo import fields, models


class ResStateEpt(models.Model):
    _name = "res.state.ept"
    _description = "To store the res state"

    name = fields.Char(string="State Name", required=True, help="Enter state name")
    abbreviation = fields.Char(string="Abbreviation", help="Enter short code of state name")
    country_name = fields.Char(string="Country Name", copy=False, help="Enter country name")
    active = fields.Boolean(string="Active", help="Tick if active")
