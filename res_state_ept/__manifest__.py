{
    'name': 'ResState',
    'version': '1.0.0',
    'category': 'ResState',
    'description': """
        This module is used to store the details of the res state.
    """,
    'author': 'Shankar Pariyar',
    'depends': ['sales_team'],
    'data': [
        'views/view_res_state.xml',
        'security/ir.model.access.csv',
        'data/res_state_demo_data.xml'
    ],
    'installable': True,
    'auto_install': False
}