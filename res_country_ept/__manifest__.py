{
    'name': 'ResCountry',
    'version': '1.0.0',
    'category': 'ResCountry',
    'description': """
        Information about restaurant country.
    """,
    'author': 'Shankar Pariyar',
    'depends': ['sales_team'],
    'data': [
        'views/view_res_country.xml',
        'security/ir.model.access.csv',
        'data/res_country_demo_data.xml'
    ],
    'installable': True,
    'auto_install': False
}