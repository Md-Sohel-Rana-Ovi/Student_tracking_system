# -*- coding: utf-8 -*-
{
    'name': "sts",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/css_loader.xml',
        'views/student_dashboard_template.xml',
        'views/student_personal_info_template.xml',
        'views/student_educational_info_template.xml', 
        'views/student_academic_details_at_diu_template.xml', 
        'views/student_registration_exam_clearence_template.xml', 
        'views/student_financial_details_ledger_template.xml', 
        'views/waiver_and_scholarship_template.xml', 
        'views/student_extra_curriculam_activities_template.xml', 
        'views/student_disciplinary_action_template.xml', 
        'views/student_hall_info_template.xml', 
        'views/student_laptop_info_template.xml', 
        'views/student_mentoring_system_template.xml', 
        'views/student_alumni_data_template.xml', 
        'views/student_search_template.xml', 
       
                
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
