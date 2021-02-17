{
    'name': 'ResCity',
    'version': '1.0.0',
    'category': 'City',
    'description': """
        This module is helpful to store the data of the res states.
    """,
    'author': 'Shankar Pariyar',
    'depends': ['sales_team'],
    'data': [
        'views/view_res_city.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False
}