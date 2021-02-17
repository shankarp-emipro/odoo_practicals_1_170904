{
    'name': 'Employee Ept',
    'version': '1.0.0',
    'category': 'employee',
    'description': """
        This module is to store the details of the employee.
    """,
    'author': 'Shankar Pariyar',
    'depends': ['base'],
    'data': [
        'views/view_employee.xml',
        'security/employee_security.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False
}