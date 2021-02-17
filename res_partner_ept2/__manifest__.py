{
    'name': 'Restaurant Partner2',
    'version': '1.0.1',
    'author': 'Shankar Pariyar',
    'category': 'Restaurant',
    'description': """This module is to store the information of restaurant""",
    'depends': ['sales_team'],
    'data': ['views/view_res_partner2.xml',
             'data/customer_data2.xml',
             'security/ir.model.access.csv'
             ],
    'installable': True,
    'auto_install': False
}