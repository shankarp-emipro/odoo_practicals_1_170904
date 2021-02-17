{
    'name': "Address Book",
    'version': '1.0.0',
    'author': 'Shankar Pariyar',
    'category': 'Address',
    'description': """
    To store employees' address.
    """,
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_address_book.xml'
    ]
}