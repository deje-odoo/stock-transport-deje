{
    'name' : 'Stock Transport',
    'version' : '1.1',
    'summary': 'Stock Transport',
    'sequence': 10,
    'description': "",
    "depends": [
        "fleet",
        "stock",
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/dispatch_management.xml',
        'views/stock_picking_batch_view.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license':'LGPL-3'
}
