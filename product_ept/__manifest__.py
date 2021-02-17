{
    'name': 'Product Ept',
    'version': '1.0.0',
    'category': 'product',
    'description': """
        This module is to store the details of the product.
    """,
    'author': 'Shankar Pariyar',
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_product.xml',
    ],
    'installable': True,
    'auto_install': False
}