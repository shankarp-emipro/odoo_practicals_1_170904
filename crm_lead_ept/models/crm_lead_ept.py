from odoo import fields, models


class CrmLeadEpt(models.Model):
    _name = "crm.lead.ept"
    _description = "To manage the crm lead"

    name = fields.Char(string="Customer Name", required=True, help="Enter customer name")
    email = fields.Char(string="Email", required=True, help="Enter email")
    phone = fields.Char(string="Phone", required=True, help="Enter phone")
    expected_revenue = fields.Float(string="Expected Revenue", digits=(6, 3), help="Enter expected revenue")
    sales_person = fields.Char(string="Sales Person", required=True, help="Enter sales person")
    sales_team = fields.Char(string="Sales Team", help="Enter sales team")
    campaign = fields.Char(string="Campaign", help="Enter campaign")
    channel = fields.Selection(selection=[
        ('Facebook', 'Facebook'),
        ('WhatsApp', 'WhatsApp'),
        ('Email', 'Email'),
        ('Newspaper', 'Newspaper'),
        ('Television', 'Television'),
        ('Phone Call', 'Phone Call'),
        ('SMS', 'SMS'),
        ('Google Ads', 'Google Ads')
    ], string="Channel", required=True, help="Select channel")
    state = fields.Selection(selection=[
        ('New', 'New'),
        ('Qualified', 'Qualified'),
        ('Proposition', 'Proposition'),
        ('Won', 'Won'),
        ('Lost', 'Lost')
    ], string="State", help="Select state")
    next_follow_up_date = fields.Date(string="Next Follow Up Date", required=True, help="Enter next follow up date")
    won_date = fields.Date(string="Won Date", help="Enter won date")
    lost_reason = fields.Text(string="Lost Reason", help="Enter lost reason")
