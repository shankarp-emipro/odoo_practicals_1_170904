from odoo import fields, models


class EmployeeEpt(models.Model):
    _name = "employee.ept"
    _description = "To store the employee data"

    name = fields.Char(string="Employee Name", required=True, help="Enter employee name")
    department_name = fields.Char(string="Department Name", help="Enter department name")
    job_position = fields.Char(string="Job Position", help="Enter job position")
    salary = fields.Float(string="Salary", digits=(6, 2), help="Enter salary")
    hire_date = fields.Date(string="Hire Date", help="Enter hire date")
    gender = fields.Selection(selection=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    ], string="Gender", help="Select gender")
    job_type = fields.Selection(selection=[
        ('Permanent', 'Permanent'),
        ('Ad Hoc', 'Ad Hoc')
    ], string="Job Type", help="Select job type")