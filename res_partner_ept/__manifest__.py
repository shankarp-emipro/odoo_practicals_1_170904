{
    'name': 'Res Partner',
    'version': '1.0.0',
    'author': 'Shankar Pariyar',
    'category': 'Restaurant',
    'description': """
    To store the details of the restaurant
    """,
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_res_partner.xml',
        'data/customers_demo.xml'
    ],
    'installable': True,
    'auto_install': False
}