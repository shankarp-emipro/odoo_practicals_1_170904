from odoo import fields, models


class ProductEpt(models.Model):
    _name = "product.ept"
    _description = "To store the product data"

    name = fields.Char(string="Product Name", required=True, help="Enter product name")
    sku = fields.Char(string="SKU", help="Enter sku")
    barcode = fields.Char(string="Barcode", help="Enter barcode")
    can_sell = fields.Boolean(string="Can Sell", help="Tick if can sell")
    product_type = fields.Selection(selection=[
        ('Storable', 'Storable'),
        ('Consumable', 'Consumable'),
        ('Service', 'Service')
    ], string="Product Type", help="Select product type")
    sale_price = fields.Float(string="Sale Price", digits=(6, 2), help="Enter sale price")
    cost_price = fields.Float(string="Cost Price", digits=(6, 2), help="Enter cost price")
    active = fields.Boolean(string="Active", help="Tick if active")
    warehouse = fields.Char(string="Warehouse", help="Enter warehouse name")
    product_image = fields.Image(string="Product Image", help="Select image")
    website_description = fields.Html(string="Website Description", help="Enter website description")
    internal_note = fields.Text(string="Internal Note", help="Enter some internal notes")