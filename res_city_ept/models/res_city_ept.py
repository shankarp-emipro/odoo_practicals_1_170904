from odoo import fields, models


class ResCityEpt(models.Model):
    _name = "res.city.ept"
    _description = "To store the res city info"

    name = fields.Char(string="City Name", required=True, help="Enter city name")
    state_name = fields.Char(string="State Name", copy=False, help="Enter state name")
    active = fields.Boolean(string="Active", help="Tick if active")
