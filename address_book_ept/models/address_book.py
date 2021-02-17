from odoo import models, fields, api


class AddressBook(models.Model):
    _name = "address.book"
    _description = "Address Book"

    name = fields.Char(string="Name", help="Enter name", required=True)
    city = fields.Char(string="City", help="Enter city")
    state = fields.Char(string="States", help="Enter state")