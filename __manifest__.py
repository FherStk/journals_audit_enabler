# -*- coding: utf-8 -*-
{
    'name': "Journals Audit Enabler",

    'summary': """
        Enables the native 'Journals Audit' PDF report which is included within Odoo but not accessible since Odoo v12.
    """,

    'description': """
        Enables the native 'Journals Audit' PDF report which is included within Odoo but not accessible since Odoo v12. The option will appear within 'Invoicing / Reporting'.
    """,

    'author': "Fernando Porrino Serrano",
    'website': "https://github.com/fherstk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/account_report_print_journal_view.xml',
    ],  
    'installable': True,
    'application': True,
}