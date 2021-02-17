{
    'name': 'CRM Lead',
    'version': '1.0.0',
    'category': 'crm_lead',
    'description': """
        This module is used to manage the crm lead.
    """,
    'author': 'Shankar Pariyar',
    'depends': ['base'],
    'data': [
        'security/employee_security.xml',
        'security/ir.model.access.csv',
        'views/view_crm_lead.xml'
    ],
    'installable': True,
    'auto_install': False
}
