# -*- coding: utf-8 -*-
{
    'name': 'Product Variant UoM Conversion',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Empower your product management with precise UoM control at the variant level.',
    'description': '''
    Elevate your inventory management by assigning Unit of Measure (UoM) at the product variant level, transcending the limitations of product template-level UoM assignment.
    This module enables the precise allocation of UoM to individual product variants, ensuring accurate UoM usage in Sales Orders when quantity is a defining attribute.
    Experience seamless UoM conversions and enhanced operational efficiency with this indispensable tool.
    Simplify your inventory management and streamline your sales processes by harnessing the power of UoM at the variant level.
    ''',
    'author': 'Econodoo',
    'website': 'https://econodoo.odoo.com',
    'maintainer': '[Econodoo@gmail.com] Econodoo',
    'depends': ['sale', 'product', 'stock'],
    'data': [
        'views/product_variant_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
