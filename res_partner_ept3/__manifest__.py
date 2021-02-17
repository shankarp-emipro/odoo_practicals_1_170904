{
    'name': 'Restaurant Partner3',
    'version': '1.0.2',
    'description': """To save the data of restaurant partner.""",
    'author': 'Shankar Pariyar',
    'category': 'Restaurant',
    'depends': ['sales_team'],
    'data': [
        'views/view_res_partner3.xml',
        'data/customers_data3.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False
}